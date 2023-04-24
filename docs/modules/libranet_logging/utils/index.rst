:py:mod:`libranet_logging.utils`
================================

.. py:module:: libranet_logging.utils

.. autoapi-nested-parse::

   libranet_logging.utils



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   libranet_logging.utils.print_tree
   libranet_logging.utils.print_loggers
   libranet_logging.utils.strtobool
   libranet_logging.utils.is_interactive_shell
   libranet_logging.utils.ensure_dir



.. py:function:: print_tree()

   Returns:



.. py:function:: print_loggers()

   Returns:



.. py:function:: strtobool(val)

   Convert a string representation of truth to true (1) or false (0).

   True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
   are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
   'val' is anything else.


.. py:function:: is_interactive_shell()

   Decide if this process is run in an interactive shell or not.

   If environment-variable $TERM is present,
   we are running this code in a interactive shell,
   else we are run from cron or called via nrpe as a nagios-check.

   Returns: boolean



.. py:function:: ensure_dir(required_dir)

   Ensure the required directory exists.


