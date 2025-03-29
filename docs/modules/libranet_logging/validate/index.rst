libranet_logging.validate
=========================

.. py:module:: libranet_logging.validate

.. autoapi-nested-parse::

   libranet_logging.validate.



Attributes
----------

.. autoapisummary::

   libranet_logging.validate.jsonschema
   libranet_logging.validate.log
   libranet_logging.validate.logging_schema


Exceptions
----------

.. autoapisummary::

   libranet_logging.validate.SchemaValidationError


Functions
---------

.. autoapisummary::

   libranet_logging.validate.validate_logging


Module Contents
---------------

.. py:data:: jsonschema
   :value: None


.. py:data:: log
   :value: None


.. py:data:: logging_schema

.. py:exception:: SchemaValidationError

   Bases: :py:obj:`Exception`


   SchemaValidationError-class.


.. py:function:: validate_logging(log_config, path)

   Validate the syntax of a logging.yml-file.


