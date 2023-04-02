:py:mod:`libranet_logging.logconfig`
====================================

.. py:module:: libranet_logging.logconfig

.. autoapi-nested-parse::

   libranet_logging.logconfig.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   libranet_logging.logconfig.is_interactive_shell
   libranet_logging.logconfig.get_sorted_lognames
   libranet_logging.logconfig.remove_console
   libranet_logging.logconfig.ensure_dir
   libranet_logging.logconfig.convert_filenames
   libranet_logging.logconfig.remove_lower_level_handlers
   libranet_logging.logconfig.validate_logging
   libranet_logging.logconfig.strtobool
   libranet_logging.logconfig.output_logging_tree
   libranet_logging.logconfig.get_default_logging_yml
   libranet_logging.logconfig.initialize



Attributes
~~~~~~~~~~

.. autoapisummary::

   libranet_logging.logconfig.cerberus
   libranet_logging.logconfig.log
   libranet_logging.logconfig.logging_schema


.. py:data:: cerberus



.. py:data:: log



.. py:data:: logging_schema



.. py:exception:: CerberusValidationError

   Bases: :py:obj:`Exception`

   CerberusValidationError-class.


.. py:function:: is_interactive_shell()

   Decide if this process is run in an interactive shell or not.

   If environment-variable $TERM is present,
   we are running this code in a interactive shell,
   else we are run from cron or called via nrpe as a nagios-check.

   Returns: boolean



.. py:function:: get_sorted_lognames()

   Returns:



.. py:function:: remove_console(config, disable_console=False)

   :param config:
   :param disable_console:

   Returns:



.. py:function:: ensure_dir(directory)

   :param directory:

   Returns:



.. py:function:: convert_filenames(config, logdir='')

   "Convert all relative filenames in the handlers to absolute paths.

   :param config:
   :param logdir:

   Returns:



.. py:function:: remove_lower_level_handlers(config)

   Remove lower-level handlers from dedicated-level loggers.

   We have dedicated file-handlers for each logging-level
     - debug_file_handler
     - info_file_handler
     - warning_file_handler
     - error_file_handler

   If the root-level is set higher, we remove the lower-level handlers
   This avoids creating logfiles that will always remain empty.



.. py:function:: validate_logging(log_config, path)

   Validate the syntax of a logging.yml-file.


.. py:function:: strtobool(val)

   Convert a string representation of truth to true (1) or false (0).

   True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
   are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
   'val' is anything else.


.. py:function:: output_logging_tree(use_print=False)

   :param use_print:

   Returns:



.. py:function:: get_default_logging_yml()

   Returns the path to the default logging configuration file.

   :returns: A `Path` object representing the path to the default logging configuration file.


.. py:function:: initialize(path='', logdir='', capture_warnings=True, silent=False, use_print=False, variables=None)

   Initialize logging configuration with a yaml-file.

   :param path:
   :param logdir:
   :param capture_warnings:
   :param silent:
   :param use_print:
   :param variables:

   Returns:



