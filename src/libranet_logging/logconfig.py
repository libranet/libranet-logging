# -*- coding: utf-8 -*-
"""libranet_logging.logconfig."""
import distutils.util
import logging
import logging.config
import operator
import os

import logging_tree
import pkg_resources

from libranet_logging.yaml import read_yaml

try:
    import cerberus
except ImportError:  # pragma: no cover
    cerberus = None

log = logging.getLogger(__name__)


logging_schema = {
    "logdir": {"type": "string", "required": False},
    "version": {"type": "integer", "required": True},
    "disable_existing_loggers": {"type": "integer"},
    "formatters": {
        "type": "dict",
        "required": True,
        "valuesrules": {
            "type": "dict",
            "schema": {
                "format": {"type": "string", "required": True},
                "datefmt": {"type": "string", "required": False},
            },
        },
    },
    "handlers": {
        "type": "dict",
        "required": True,
        "valuesrules": {
            "type": "dict",
            "schema": {
                "class": {"type": "string", "required": True},
                # logstash-handler sets the correct formatter via code
                # therefore the formatter-key in not required in logging.yml
                "formatter": {"type": "string", "required": False},
                "level": {"type": "string", "required": True},
                "encoding": {"type": "string", "required": False},
                "filename": {"type": "string", "required": False},
                "stream": {"type": "string", "required": False},
                "maxBytes": {"type": "integer", "required": False},
                "backupCount": {"type": "integer", "required": False},
            },
        },
    },
    "loggers": {
        "type": "dict",
        "required": True,
        "valuesrules": {
            "type": "dict",
            "schema": {
                "handlers": {"type": "list", "required": False},
                "level": {"type": "string", "required": False},
                "propagate": {"type": "boolean", "required": False},
            },
        },
    },
    "root": {
        "type": "dict",
        "required": True,
        "schema": {"handlers": {"type": "list", "required": True}, "level": {"type": "string"}},
    },
}


class CerberusValidationError(Exception):
    """CerberusValidationError-class."""


def is_interactive_shell():
    """Decide if this process is run in an interactive shell or not.

    If environment-variable $TERM is present,
    we are running this code in a interactive shell,
    else we are run from cron or called via nrpe as a nagios-check.

    Returns: boolean

    """
    if os.environ.get("TERM", None):
        return True
    return False



def get_sorted_lognames():
    """

    Returns:

    """
    loglevels = logging._levelToName.items()  # pylint: disable=protected-access
    sorted_loglevels = sorted(loglevels, key=operator.itemgetter(0))
    sorted_names = [lvl[1] for lvl in sorted_loglevels]
    return sorted_names


def remove_console(config, disable_console=False):
    """

    Args:
        config:
        disable_console:

    Returns:

    """
    if config.get("root") and "console" in config["root"]["handlers"]:
        if disable_console or not is_interactive_shell():
            config["root"]["handlers"].remove("console")
    return config


def ensure_dir(directory):
    """

    Args:
        directory:

    Returns:

    """
    if os.path.exists(directory):
        if not os.path.isdir(directory):
            raise OSError(
                f"The provided path to the log-directory exist but is not a directory: {directory}"
            )
    else:
        os.makedirs(directory)


def convert_filenames(config, logdir=""):
    """"Convert all relative filenames in the handlers to absolute paths.

    Args:
        config:
        logdir:

    Returns:

    """
    logdir = (
        str(logdir)
        or config.get("logdir")
        or os.environ.get("PYTHON_LOG_DIR")
        or os.path.expanduser("~/logs")
    )
    ensure_dir(logdir)

    for handler in config.get("handlers", []):
        filename = config["handlers"][handler].get("filename", "")
        if filename and not os.path.isabs(filename):
            config["handlers"][handler]["filename"] = os.path.join(logdir, filename)

    return config


def remove_lower_level_handlers(config):
    """Remove lower-level handlers from dedicated-level loggers.

    We have dedicated file-handlers for each logging-level
      - debug_file_handler
      - info_file_handler
      - warning_file_handler
      - error_file_handler

    If the root-level is set higher, we remove the lower-level handlers
    This avoids creating logfiles that will always remain empty.

    """
    available_levels = get_sorted_lognames()
    try:
        root_level = config["root"]["level"]
    except KeyError:
        return config

    for lvl in available_levels:
        if lvl == root_level:
            break

        # strip lower-level handlers
        config["handlers"] = {
            k: v for (k, v) in config["handlers"].items() if not k.startswith(lvl.lower())
        }
        config["root"]["handlers"] = [
            hdr for hdr in config["root"]["handlers"] if not hdr.startswith(lvl.lower())
        ]

    return config


def validate_logging(log_config, path):
    """Validate the syntax of a logging.yml-file."""
    if not cerberus:  # pragma: no cover
        return

    validator = cerberus.Validator(logging_schema, allow_unknown=True)
    success = validator.validate(log_config)
    if not success and validator.errors:
        sorted_errors = sorted(validator.errors.items())
        msg = f"logconfig {path} contains errors: {sorted_errors}"
        raise CerberusValidationError(msg)


def output_logging_tree(use_print=False):
    """

    Args:
        use_print:

    Returns:

    """
    env_var_string = os.environ.get("PYTHON_ENABLE_LOGGING_TREE", "false")
    visible = distutils.util.strtobool(env_var_string)
    if not visible:
        return

    configured_log_description = logging_tree.format.build_description()
    if use_print:
        print(configured_log_description)
    else:
        log.debug(configured_log_description)


def get_default_logging_yml():
    """

    Returns:

    """
    return pkg_resources.resource_filename("libranet_logging", "etc/logging.yml")


def initialize(
    path="",
    logdir="",
    capture_warnings=True,
    silent=False,
    use_print=False,
    variables=None,
):
    """Initialize logging configuration with a yaml-file.

    Args:
        path:
        logdir:
        capture_warnings:
        silent:
        use_print:
        variables:

    Returns:

    """
    variables = variables or {}
    path = str(path) or os.environ.get("PYTHON_LOG_CONFIG", "") or get_default_logging_yml()

    config = read_yaml(path, variables=variables)
    config = convert_filenames(config, logdir=logdir)
    config = remove_lower_level_handlers(config)
    validate_logging(config, path)

    logging.config.dictConfig(config)
    logging.captureWarnings(capture_warnings)
    output_logging_tree(use_print=use_print)

    if not silent:
        log.debug(f"Logging configured from {path}")
