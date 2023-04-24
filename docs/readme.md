[![Testing](https://img.shields.io/github/actions/workflow/status/libranet/libranet-logging/testing.yaml?branch=main&longCache=true&style=flat-square&label=tests&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/libranet-logging/actions/workflows/testing.yaml)
[![Linting](https://img.shields.io/github/actions/workflow/status/libranet/libranet-logging/linting.yaml?branch=main&longCache=true&style=flat-square&label=Linting&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/libranet-logging/actions/workflows/linting.yaml)
[![Read the Docs](https://readthedocs.org/projects/libranet-logging/badge/?version=latest)](https://libranet-logging.readthedocs.io/en/latest/)
[![Codecov](https://codecov.io/gh/libranet/libranet-logging/branch/main/graph/badge.svg?token=5QL5P68B80)](https://codecov.io/gh/libranet/libranet-logging)
[![PyPi Package](https://img.shields.io/pypi/v/libranet-logging?color=%2334D058&label=pypi%20package)](https://pypi.org/project/libranet-logging/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/libranet/libranet-logging/blob/main/docs/license.md)


## Installation

Install via pip:

```bash
> bin/pip install libranet-logging
```

Or add to your poetry-based project:

```bash
> poetry add libranet-logging
```


# Why use logging?

Logfiles are your best-friend

  - during development, where debugmode is developmentmode

  - more important: while running in PRD,
    - it shows how the application is being used, by whom, and if it's successfull
    - allows to become pro-active. There is no need to wait for bugreports from users.

  - most important: during urgent troubleshooting on PRD (AKA panic-mode)
    - heisenbugs,  difficult to reproduce.


# Goal of libranet-logging

Make it as easy as possible to enable and properly use the full power of the python logging-framework

python logging-module contains:
  - loggers, hierarchical
  - handlers
    - formatters
    - filters

Think of logger=message-channel, handler=subscriber to a channel

Minimize the need to make changes in code

Move all config out of code and into a config-file "logging.yml"

  - logging to a file should be as simple as:

        ```python
        >>> import logging
        >>> logging.getLogger('panicmode')
        ```


# Usage

## In your deployment

You can use following env-variables:

    - LOGGING_YML_FILE, path to logging.yml, e.g  /opt/miniconda/envs/libranet/etc/logging.yml
    - LOG_DIR, path to log-directory where logfiles will be created, /var/tmp/python
    - PYTHON_ENABLE_LOGGING_TREE  1|0

  optional env-vars:
    - LOGLEVEL_ROOT
    - LOGLEVEL_libranet_logging
    - LOG_HANDLERS="console|debug_file|info_file|warning_file|error_file"


    If missing, these default to DEBUG


## In your code

To initialize the logging-infrastructure and set-up all configured
loggers, handlers, formatters and filters:

```python
  > import libranet_logging
  > libranet_logging.initialize()
    2018/06/01 10:00:00 - root - DEBUG   - Logging configured from <path-to>/logging.yml
```

You do this once in your application,
in the function that starts execution, not at the top of your module.

```python
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
```


# Features

 - load logging-configuration from a yaml-config

 - validate yaml-file for missing keys, invalid values

 - configurable via env-variables
   - sane defaults if env-var is not set

 - when logging to console, have colorized logging,
   - but nowhere else
   - configurable colors (avoid blue on black)

 - integrate python-warnings
 - add sample email-logger
 - add sample syslog-logger

 - avoid empty files that will remain empty
   - cleanup dedicated file-handlers based on root-loglevel

 - future ideas:
   - integrate with kibana
   - log as json, structlog

       - https://logmatic.io/blog/python-logging-with-json-steroids/
       - https://medium.com/@sanchitsokhey/centralised-logging-for-django-gunicorn-and-celery-using-elk-stack-76b13c54414c
       - https://logmatic.io/blog/beyond-application-monitoring-discover-logging-best-practices/


 - in code throw out all
   - formatting,
   - handler-config,
   - setting loglevel
   - debug-flags like::

        ```python
        >>> if DEBUG:
        >>>     log.debug(....)
        ```