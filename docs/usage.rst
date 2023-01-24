Usage
=====

In your deployment
------------------

You can use following env-variables:

    - PYTHON_LOG_CONFIG, path to logging.yml, e.g  /opt/miniconda/envs/libranet/etc/logging.yml
    - PYTHON_LOG_DIR, path to log-directory where logfiles will be created, /var/tmp/python
    - PYTHON_ENABLE_LOGGING_TREE  1|0

  optional env-vars:
    - LOGLEVEL_ROOT
    - LOGLEVEL_libranet_logging
    - LOG_HANDLERS="console|debug_file|info_file|warning_file|error_file"


    If missing, these default to DEBUG


In your code
------------
To initialize the logging-infrastructure and set-up all configured
loggers, handlers, formatters and filters:

.. code-block:: python

  > import libranet_logging
  > libranet_logging.initialize()
    2018/06/01 10:00:00 - root - DEBUG   - Logging configured from <path-to>/logging.yml

You do this once in your application,
in the function that starts execution, not at the top of your module.

.. code-block:: python

  # Calling getLogger without arguments returns the root-logger,
  # of which all other loggers descend.
  # Normally you do NOT need this logger.
  > import logging
  > root_log = logging.getLogger()

  # You normally use the module-logger
  > log = logging.getLogger(__name__)


  # and starting using it
  > log.debug('This is debugging-information.')
  > log.info('This is useful information.')
  > log.warning('This is a warning.')
  > log.error('This is a warning.')

  # You can log a full-traceback by providing the exception to log.exception().
  > try:
  >     import foo
  > except ImportError as e:
  >     log.exception(e)

