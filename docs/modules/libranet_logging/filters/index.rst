libranet_logging.filters
========================

.. py:module:: libranet_logging.filters

.. autoapi-nested-parse::

   libranet_logging.filters.



Classes
-------

.. autoapisummary::

   libranet_logging.filters.SimpleStringFilter
   libranet_logging.filters.RegexFilter


Module Contents
---------------

.. py:class:: SimpleStringFilter(name='', params=None)

   Bases: :py:obj:`logging.Filter`


   SimpleStringFilter is a logging-filter based in simple string occurence in the logmessage.


   .. py:attribute:: params
      :value: None



   .. py:method:: filter(record)

      Determine if the specified record is to be logged.

      :param record:

      Returns:




.. py:class:: RegexFilter(name='', params=None)

   Bases: :py:obj:`logging.Filter`


   RegexFilter is a logging-filter based in regular expressions.


   .. py:attribute:: params
      :value: None



   .. py:attribute:: regexes


   .. py:method:: filter(record)

      Determine if the specified record is to be logged.

      :param record:

      Returns:




