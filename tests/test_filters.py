# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
"""Testing of module libranet_logging.loglevel."""


class LogRecord:
    def __init__(self, msg):
        self.msg = msg

    def getMessage(self):
        return self.msg


def test_simple_stringfilter_without_params():
    from libranet_logging.filters import SimpleStringFilter

    params = []
    simple_string_filter = SimpleStringFilter(params=params)
    assert simple_string_filter.filter(LogRecord("xx AA yy")) is True
    assert simple_string_filter.filter(LogRecord("xx BB yy")) is True
    assert simple_string_filter.filter(LogRecord("")) is True


def test_simple_stringfilter():
    from libranet_logging.filters import SimpleStringFilter

    params = ["AA", "BB"]
    simple_string_filter = SimpleStringFilter(params=params)
    # matching
    assert simple_string_filter.filter(LogRecord("xx AA yy")) is False
    assert simple_string_filter.filter(LogRecord("xx BB yy")) is False
    # non-matching
    assert simple_string_filter.filter(LogRecord("xx CC yy")) is True
    assert simple_string_filter.filter(LogRecord("")) is True


def test_regexfilter_without_params():
    from libranet_logging.filters import RegexFilter

    params = []
    regex_filter = RegexFilter(params=params)
    # non-matching
    assert regex_filter.filter(LogRecord("xx AA yy")) is True
    assert regex_filter.filter(LogRecord("xx BB yy")) is True
    assert regex_filter.filter(LogRecord("")) is True


def test_regexfilter():
    from libranet_logging.filters import RegexFilter

    params = ["^AA", "BB$"]
    regex_filter = RegexFilter(params=params)
    # matching
    assert regex_filter.filter(LogRecord("AA yy")) is False
    assert regex_filter.filter(LogRecord("AA BB")) is False
    assert regex_filter.filter(LogRecord("xx BB")) is False
    # non-matching
    assert regex_filter.filter(LogRecord("xx AA yy")) is True
    assert regex_filter.filter(LogRecord("xx BB yy")) is True
    assert regex_filter.filter(LogRecord("xx CC yy")) is True
    assert regex_filter.filter(LogRecord("")) is True
