:py:mod:`libranet_logging.validate`
===================================

.. py:module:: libranet_logging.validate

.. autoapi-nested-parse::

   libranet_logging.validate.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   libranet_logging.validate.validate_logging



Attributes
~~~~~~~~~~

.. autoapisummary::

   libranet_logging.validate.cerberus
   libranet_logging.validate.log
   libranet_logging.validate.logging_schema


.. py:data:: cerberus



.. py:data:: log



.. py:data:: logging_schema



.. py:exception:: CerberusValidationError

   Bases: :py:obj:`Exception`

   CerberusValidationError-class.


.. py:function:: validate_logging(log_config, path)

   Validate the syntax of a logging.yml-file.


