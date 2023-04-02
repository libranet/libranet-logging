:py:mod:`libranet_logging`
==========================

.. py:module:: libranet_logging

.. autoapi-nested-parse::

   libranet_logging.__init__



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cli/index.rst
   filters/index.rst
   logconfig/index.rst
   loglevel/index.rst
   yaml/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   libranet_logging.print_loggers
   libranet_logging.print_tree
   libranet_logging.initialize
   libranet_logging.output_logging_tree
   libranet_logging.create_loglevel



Attributes
~~~~~~~~~~

.. autoapisummary::

   libranet_logging.__version__
   libranet_logging.create_loglevel_trace


.. py:data:: __version__
   :value: '1.4.dev0'



.. py:function:: print_loggers()

   Returns:



.. py:function:: print_tree()

   Returns:



.. py:function:: initialize(path='', logdir='', capture_warnings=True, silent=False, use_print=False, variables=None)

   Initialize logging configuration with a yaml-file.

   :param path:
   :param logdir:
   :param capture_warnings:
   :param silent:
   :param use_print:
   :param variables:

   Returns:



.. py:function:: output_logging_tree(use_print=False)

   :param use_print:

   Returns:



.. py:function:: create_loglevel(level_name='', level_num=0)

   Create a custom loglevel.

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

   :param level_name: logger-name
   :param level_num: numeric level of the custom logger, positive integer

   :returns: None

   Side-effect:
       adds attribute to Logger-class




.. py:data:: create_loglevel_trace



