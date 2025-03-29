libranet_logging.logconfig
==========================

.. py:module:: libranet_logging.logconfig

.. autoapi-nested-parse::

   libranet_logging.logconfig.



Attributes
----------

.. autoapisummary::

   libranet_logging.logconfig.log


Functions
---------

.. autoapisummary::

   libranet_logging.logconfig.get_sorted_lognames
   libranet_logging.logconfig.remove_console
   libranet_logging.logconfig.convert_filenames
   libranet_logging.logconfig.remove_lower_level_handlers
   libranet_logging.logconfig.output_logging_tree
   libranet_logging.logconfig.get_default_logging_yaml
   libranet_logging.logconfig.get_default_logging_yaml
   libranet_logging.logconfig.get_dict_config
   libranet_logging.logconfig.initialize


Module Contents
---------------

.. py:data:: log
   :value: None


.. py:function:: get_sorted_lognames()

   Return a sorted list of loglevel-names.


.. py:function:: remove_console(config, disable_console = False)

   :param config:
   :param disable_console:

   Returns:



.. py:function:: convert_filenames(config, logdir='')

   Convert relative filenames in the handlers to absolute paths.


.. py:function:: remove_lower_level_handlers(config)

   Remove lower-level handlers from dedicated-level loggers.

   We have dedicated file-handlers for each logging-level
     - debug_file_handler
     - info_file_handler
     - warning_file_handler
     - error_file_handler

   If the root-level is set higher, we remove the lower-level handlers
   This avoids creating logfiles that will always remain empty.



.. py:function:: output_logging_tree(use_print=False)

   :param use_print:

   Returns:



.. py:function:: get_default_logging_yaml()

   Returns the path to the default logging configuration file.

   :returns: A Traversable `Path` object representing the path to the default logging configuration file.


.. py:function:: get_default_logging_yaml()

   Returns the path to the default logging configuration file.

   :returns: A Traversable `Path` object representing the path to the default logging configuration file.


.. py:function:: get_dict_config(path = '', logdir='', variables=None)

   Return a fully resolved logging configuration as a dictionary.


.. py:function:: initialize(path='', logdir='', capture_warnings = True, silent = False, use_print = False, variables=None)

   Initialize logging configuration with a yaml-file.

   :param path:
   :param logdir:
   :param capture_warnings:
   :param silent:
   :param use_print:
   :param variables:

   Returns:



