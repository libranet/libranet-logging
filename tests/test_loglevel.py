# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_logging.loglevel."""
import logging

import pytest


def test_create_invalidloglevel(env):
    from libranet_logging.loglevel import create_loglevel

    level_num = "a"
    with pytest.raises(ValueError) as excinfo:
        create_loglevel(level_name="TRACE", level_num=level_num)
    assert str(excinfo.value) == f"Invalid numeric log level: {level_num}"


def test_create_loglevel(env):
    from libranet_logging.loglevel import create_loglevel

    create_loglevel(level_name="TRACE", level_num=5)

    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(5)
    log.trace("ee")

    assert logging._checkLevel("TRACE") == 5  # pylint: disable=protected-access
    assert log.getEffectiveLevel() == 5
    assert log.isEnabledFor(logging.DEBUG) is True
    assert log.isEnabledFor(5) is True
    assert log.isEnabledFor(0) is False
