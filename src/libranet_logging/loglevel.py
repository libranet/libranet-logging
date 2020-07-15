# -*- coding: utf-8 -*-
"""libranet_logging.loglevel."""
import functools
import logging


def create_loglevel(level_name="", level_num=0):
    """Create a custom loglevel.

    Defining your own levels is possible, but should not be necessary, as the existing levels
    have been chosen on the basis of practical experience. However, if you are convinced that
    you need custom levels, great care should be exercised when doing this, and it is possibly
    a very bad idea to define custom levels if you are developing a library. That’s because if
    multiple library authors all define their own custom levels, there is a chance that the
    logging output from such multiple libraries used together will be difficult for the using
    developer to control and/or interpret, because a given numeric value might mean different
    things for different libraries.
    Cfr. https://docs.python.org/3/howto/logging.html#custom-levels

    Default levels:
        0 NOTSET
        10 DEBUG
        20 INFO
        30 WARNING
        40 ERROR
        50 CRITICAL

    Args:
        level_name: logger-name
        level_num:  numeric level of the custom logger, positive integer

    Returns:
        None

    Side-effect:
        adds attribute to Logger-class


    """
    # level_name = level_name.replace('-', '_').lower()

    if not isinstance(level_num, int):
        raise ValueError("Invalid numeric log level: %s" % level_num)

    def handler(self, message, *args, **kwargs):
        # logger takes its '*args' as 'args'
        if self.isEnabledFor(level_num):
            self._log(level_num, message, args, **kwargs)  # pylint: disable=protected-access

    logging.addLevelName(level_num, level_name.upper())
    setattr(logging.Logger, level_name.lower(), handler)


create_loglevel_trace = functools.partial(create_loglevel, level_name="TRACE", level_num=5)
