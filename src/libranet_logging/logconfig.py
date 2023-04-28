"""libranet_logging.logconfig."""
import importlib.resources
import logging
import logging.config
import operator
import os

import logging_tree

from libranet_logging.utils import ensure_dir, is_interactive_shell, strtobool
from libranet_logging.validate import validate_logging
from libranet_logging.yaml import read_yaml

log = logging.getLogger(__name__)


def get_sorted_lognames() -> list[str]:
    """
    Returns a sorted list of loglevel-names.
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


def convert_filenames(config, logdir=""):
    """ "Convert relative filenames in the handlers to absolute paths.

    Args:
        config:
        logdir:

    Returns:

    """
    logdir = (
        str(logdir)
        or config.get("logdir")
        or os.environ.get("LOG_DIR")
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
        config["handlers"] = {k: v for (k, v) in config["handlers"].items() if not k.startswith(lvl.lower())}
        config["root"]["handlers"] = [hdr for hdr in config["root"]["handlers"] if not hdr.startswith(lvl.lower())]

    return config


def output_logging_tree(use_print=False):
    """

    Args:
        use_print:

    Returns:

    """
    env_var_string = os.environ.get("PYTHON_ENABLE_LOGGING_TREE", "false")
    visible = strtobool(env_var_string)
    if not visible:
        return

    configured_log_description = logging_tree.format.build_description()
    if use_print:
        print(configured_log_description)
    else:
        log.debug(configured_log_description)


def get_default_logging_yaml() -> importlib.abc.Traversable:
    """
    Returns the path to the default logging configuration file.

    Returns:
        A Traversable `Path` object representing the path to the default logging configuration file.
    """
    package_root = importlib.resources.files("libranet_logging")
    return package_root / "etc" / "logging.yaml"


def initialize(
    path="",
    logdir="",
    capture_warnings: bool = True,
    silent: bool = False,
    use_print: bool = False,
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
    path = str(path) or os.getenv("LOGGING_YML_FILE") or os.getenv("LOG_CONFIG") or str(get_default_logging_yaml())

    config = read_yaml(path, variables=variables)
    config = convert_filenames(config, logdir=logdir)
    config = remove_lower_level_handlers(config)
    validate_logging(config, path)

    logging.config.dictConfig(config)
    logging.captureWarnings(capture_warnings)
    output_logging_tree(use_print=use_print)

    if not silent:
        log.debug(f"Logging configured from {path}")
