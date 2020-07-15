# -*- coding: utf-8 -*-
"""libranet_logging.filters."""
import logging
import re


class SimpleStringFilter(logging.Filter):
    """SimpleStringFilter is a logging-filter based in simple string occurence in the logmessage.
    """

    def __init__(self, name="", params=None) -> None:
        super().__init__(name=name)
        self.params = params

    def filter(self, record) -> bool:
        """Determine if the specified record is to be logged.

        Args:
            record:

        Returns:

        """
        if not self.params:
            return True

        for param in self.params:
            if param in record.msg:
                return False

        return True


class RegexFilter(logging.Filter):
    """RegexFilter is a logging-filter based in regular expressions.
    """

    def __init__(self, name="", params=None) -> None:
        super().__init__(name=name)
        self.params = params
        self.regexes = [re.compile(x) for x in self.params]

    def filter(self, record) -> bool:
        """Determine if the specified record is to be logged.


        Args:
            record:

        Returns:

        """
        if not self.params:
            return True

        is_matching = any(regex.search(record.getMessage()) for regex in self.regexes)
        if is_matching:
            return False

        return True
