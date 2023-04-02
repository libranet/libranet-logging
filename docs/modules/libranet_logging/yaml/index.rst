:py:mod:`libranet_logging.yaml`
===============================

.. py:module:: libranet_logging.yaml

.. autoapi-nested-parse::

   libranet_logging.yaml.

   In pyyaml 5.1 some incompatibilies were introduced with regard to ``yaml.load``
   to make it more safe by default.

   please see:
     - https://github.com/yaml/pyyaml/blob/master/CHANGES
     - https://github.com/yaml/pyyaml/pull/257
     - https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   libranet_logging.yaml.constructor_env
   libranet_logging.yaml.add_constructor
   libranet_logging.yaml.read_yaml



.. py:function:: constructor_env(loader, node)

   YAML-Constructor to load a value from a env-variable.

   Usage in yml:
       > !env ENVVAR_NAME, DEFAULTVALUE_IF_ENVVAR_NOT_SET



.. py:function:: add_constructor()


.. py:function:: read_yaml(path, variables=None)

   Read the yaml-file.

   Returns: dict


