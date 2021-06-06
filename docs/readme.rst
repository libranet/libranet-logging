Overview
========

``libranet_logging`` is an easy to use logging-configuration reading the configuration
for loggers, handlers, filters and formatters from a logging.yml-file.

Overview urls
-------------
  - git-repository: https://github.com/Libranet/libranet_logging
  - changelog:  <url>
  - sphinx-docs:  <url>
  - code-coverage: <url>
  - pypi: <url>


Why use logging?
----------------
Logfiles are your best-friend

  - during development, where debugmode is developmentmode

  - more important: while running in PRD,
    - it shows how the application is being used, by whom, and if it's successfull
    - allows to become pro-active. There is no need to wait for bugreports from users.

  - most important: during urgent troubleshooting on PRD (AKA panic-mode)
    - heisenbugs,  difficult to reproduce.


Goal of libranet_logging
------------------------
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
        >>> import logging
        >>> logging.getLogger('panicmode')


Features
--------

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

     if DEBUG:
        log.debug(....)
