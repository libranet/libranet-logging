Changelog
=========

1.3 (2023-01-24)
----------------

- No longer try to be smart about interactive mode or not.
  You can set the active logging-handlers by setting the env-var ``LOG_HANDLERS```

- Remove ``disable_console`` as input-parameter to ``libranet_logging.initialize()``.

- Change default separator from ``;`` to ``|``. Use set via env-var ``LOG_HANDLERS``.


1.2 (2021-06-06)
----------------

- Fix logo. [WVH]

- Add .gitlab-ci.yml [WVH]


1.1 (2020-02-13)
----------------

- Fix error ``ModuleNotFoundError: No module named 'libranet_logging.version'``. [WVH]


1.0 (2020-02-12)
----------------

- Move ``__version__``-attribute to ``__init__``. [WVH]

- Package ``libranet_logging`` forked from WVH's unreleased package. [WVH]


0.5 (2019-08-19)
----------------

- Add docstrings and type-hinting.

- Fix a series of issues reported by pylint.

- Change function-signature of ``libranet_logging.yaml.read_yml``: change ``vars`` into ``variables``
  to avoid shadowing the buitlin ``vars()``-function::

      >>> config = read_yaml(path, vars=None)
      >>> config = read_yaml(path, variables=None)


0.4 (2019-07-31)
----------------
- Add ``version.py`` with a ``__version__``-attribute, rework version-management.

- In ``setup.py`` set minimum-requirements for cerberus >=1.3.1. [WVH]


0.3 (2019-05-28)
----------------

- In sphinx-docs, add link to coverage-report
  on https://example.com/docs/libranet_logging-coverage [WVH]

- In ``Makefile`` add step`` copy-cov`` to copy coverage-report to apache-webdirectory. [WVH]

- In ``libranet_logging.yaml.read_yaml`` cdefault vars to empty dicts when not provided. [WVH]

- In ``libranet_logging.logconfig.logging_schema`` rename ``valueschema`` to ``valuesrules``
  to avoid DeprecationWarnings. [WVH]


0.2 (2019-03-28)
----------------

- Make ``libranet_logging.yaml.read_yaml`` compatible with PyYAML 5.1,
  but keep backwards-compatibility with older versions. [WVH]
  Cfr::

    - https://github.com/yaml/pyyaml/blob/master/CHANGES
    - https://github.com/yaml/pyyaml/pull/257
    - https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation


0.1 (2019-03-28)
----------------

- Add support for simple string-formatting in the loggin.yml. [WVH]

- Use ``isort`` to manage the imports. Add isort-config to ``setup.cfg``. [WVH]

- Introduce environment-variable ``PYTHON_CONSOLE_FORMATTER`` to select which
  console-formatter to use. [WVH]

- Rename ``colored``-console-formatter into ``console_color`` and add
  ``console_bw``-formatter for simpe black & white logging in the console. [WVH]

- Add ``flask_wtf``-handler in default ``logging.yml``. [WVH]

- If the log-directory does not yet exist, we now create it. [WVH]

- We should have a user-specific default location to avoid interference between users.
  The log-directory will be first taken from th direct function-parameters, then
  from the ``logging.yml`` if present. If not present, from the env-var
  ``PYTHON_LOG_CONFIG``, and in case of no env-var we default to ``$HOME/logs``
  instead of ``var/tmp/python``. [WVH]

- Support setting the log-directory via the ``initialize``-function. [WVH]

- Fix failing test ``test_initialize_without_logging_tree``.
  It was failing when the env-var ``PYTHON_ENABLE_LOGGING_TREE`` was not set. [WVH]

- Fix failing test of the click-command ``cli.print_logging_tree``. [WVH]

- Add new testing-dependency ``pytest-click``. [WVH]

- Convert ``cli.print_logging_tree`` to a ``click``-command, accepting an optional ``path``-argument.
  If the environment-variable ``PYTHON_LOG_CONFIG`` is set, we use that value as the path-default. [WVH]

- Add ``click`` as a new dependency. [WVH]

- Add documentation about unittesting. [WVH]

- We now support arrays in environment-variables. Environment-variables
  containing a ``;`` are now converted to a list similar to the
  default value if that env-variable was not set. [WVH]

- Fix ``filters.RegexFilter`` to use ``search()`` instead of ``match()``.
  Cfr. https://docs.python.org/3/library/re.html#search-vs-match [WVH]

- Add passing unit-tests. [WVH]

- In ``initialize()`` allow Path-parameters as input instead of only string-paths. [WVH]

- Generally make the code robust in case of loading a logging.yml with schema-errors. [WVH]

- Add console-entrypoint ``libranet-logging-print-logging-tree``
  to initialize the logging and print the logging-tree to the standard output.
  Add corresponding function in new ``libranet_logging.cli``-module. [WVH]

- Add function-paramater ``use_print=False`` to ``logconfig.show_logging_tree``
  to enable printing to standard output instead of logging to the configured loggers. [WVH]

- If we call ``initialize()`` without providing a path of setting the environmant-variable ``PYTHON_LOG_CONFIG``,
  we now use the default ``logging.yml`` shipped with this ``libranet_logging``-package. [WVH]

- Add logger ``libranet_logging`` to our default ``logging.yml``. [WVH]

- Instantiate the correct logger using ``__name__`` instead of logging to the root-logger. [WVH]

- Add ``recommonmark`` and update ``docs.conf.py`` to allow markdown in docs.
  Cfr.https://recommonmark.readthedocs.io/en/latest/  [WVH]

- In ``setup.py`` and ``docs/pip-requirements`` add ``sphinx``-related dependencies. [WVH]

- Simplify public api:

  - Rename function ``loglevel.create_loglevel`` into ``loglevel.create``.

  - Rename function ``logconfig.initialize_logging`` into ``logconfig.initialize``.

  [WVH]

- Run ``Black`` on the code. ``Black`` is a code-formatter for Python.
  Cfr. https://github.com/ambv/black [WVH]
- Add some basic Sphinx-based documentation. [WVH]

- Factor out creating new loglevels into its own ``loglevel``-module. [WVH]

- Factor out logging-filters into its own ``filters``-module. [WVH]

- Add third-party dependency ``colorlog``. This is not a code-dependency
  but rather a dependency of ``logging.yml``. [WVH]

- Add third-party dependencies ``cerberus``, ``logging_tree`` and ``PyYAML``. [WVH]

- Move logging-related code from ``libdl.utils`` into its own ``libranet_logging``-package. [WVH]

- Package created via ``cookiecutter templates/cookiecutter-libranet-python-package``.
  [Wouter Vanden Hove <wouter@wvhconsulting.org>]
