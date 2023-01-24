# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
"""libranet_logging.cli"""
import logging
import os

import click
import logging_tree

from libranet_logging.logconfig import get_default_logging_yml, initialize


@click.command()
@click.argument("path", envvar="PYTHON_LOG_CONFIG", required=False, type=click.Path(exists=False))
def print_logging_tree(path) -> None:
    """Initializes the logging and print the configured logging-tree."""
    os.environ["PYTHON_ENABLE_LOGGING_TREE"] = "True"

    if not path:
        click.secho(
            "No path provided to a logging.yml and the env-var PYTHON_LOG_CONFIG is not set.",
            fg="yellow",
            bold=True,
        )
        click.secho(
            f"Using the packaged default from {get_default_logging_yml()}",
            fg="yellow",
            bold=True,
        )

    initialize(use_print=True)


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
    from logging_tree.nodes import tree

    _, _, children = tree()
    for node in children:
        name, logger, _ = node
        loglevelname = logging._levelToName[logger.level].upper()  # pylint: disable=protected-access
        print(f"{name} - disabled: {logger.disabled} - level: {loglevelname}")
