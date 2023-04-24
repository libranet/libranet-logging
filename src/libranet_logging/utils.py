"""libranet_logging.utils"""
import logging
import os
import pathlib as pl
import typing as tp

import logging_tree

# @click.command()
# @click.argument("path", envvar="PYTHON_LOG_CONFIG", required=False, type=click.Path(exists=False))
# def print_logging_tree(path) -> None:
#     """Initializes the logging and print the configured logging-tree."""
#     os.environ["PYTHON_ENABLE_LOGGING_TREE"] = "True"

#     if not path:
#         click.secho(
#             "No path provided to a logging.yml and the env-var PYTHON_LOG_CONFIG is not set.",
#             fg="yellow",
#             bold=True,
#         )
#         click.secho(
#             f"Using the packaged default from {get_default_logging_yml()}",
#             fg="yellow",
#             bold=True,
#         )

#     initialize(use_print=True)


def print_tree() -> None:
    """

    Returns:

    """
    msg = logging_tree.format.build_description()
    print(msg)


def print_loggers() -> None:
    """

    Returns:

    """
    _, _, children = logging_tree.nodes.tree()
    for node in children:
        name, logger, _ = node
        loglevelname = logging._levelToName[logger.level].upper()  # pylint: disable=protected-access
        print(f"{name} - disabled: {logger.disabled} - level: {loglevelname}")


def strtobool(val):  # copied from distutils.util.strtobool
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1

    if val in ("n", "no", "f", "false", "off", "0"):
        return 0

    raise ValueError(f"invalid truth value {val}")


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


def ensure_dir(required_dir: tp.Union[pl.Path, str]) -> None:
    """Ensure the required directory exists."""

    # convert to Path
    if isinstance(required_dir, str):
        required_dir = pl.Path(required_dir)

    # resolve any symlinks
    required_dir = required_dir.resolve()

    if required_dir.exists() and required_dir.is_dir():
        return

    if required_dir.exists() and not required_dir.is_dir():
        raise FileExistsError(f"{required_dir} already exists and is not a directory.")

    required_dir.mkdir(exist_ok=False, parents=True)
