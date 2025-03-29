libranet_logging.loglevel
=========================

.. py:module:: libranet_logging.loglevel

.. autoapi-nested-parse::

   libranet_logging.loglevel.



Attributes
----------

.. autoapisummary::

   libranet_logging.loglevel.create_loglevel_trace


Functions
---------

.. autoapisummary::

   libranet_logging.loglevel.create_loglevel


Module Contents
---------------

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

