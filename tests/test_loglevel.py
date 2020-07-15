# -*- coding: utf-8 -*-
"""Testing of module libranet_logging.loglevel."""
import logging

import pytest

from libranet_logging.loglevel import create_loglevel


def test_create_invalidloglevel(env):
    level_num = "a"
    with pytest.raises(ValueError) as excinfo:
        create_loglevel(level_name="TRACE", level_num=level_num)
    assert str(excinfo.value) == "Invalid numeric log level: {}".format(level_num)


def test_create_loglevel(env):
    create_loglevel(level_name="TRACE", level_num=5)

    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(5)
    log.trace("ee")

    assert logging._checkLevel("TRACE") == 5
    assert log.getEffectiveLevel() == 5
    assert log.isEnabledFor(logging.DEBUG) is True
    assert log.isEnabledFor(5) is True
    assert log.isEnabledFor(0) is False
