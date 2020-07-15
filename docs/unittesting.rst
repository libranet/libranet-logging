Unittesting
===========
.. _testing:


Introduction
------------
Our python-package ``libranet_logging`` comes with a series of tests to check
the validity of our code. Some are unittests, others are full integration-tests.
The distinction between the several types of tests is of lesser importance.

However we try to minimize the amount of *mocking* and/or *patching*.
The test-framework we use is ``pytest``.

- https://docs.pytest.org/en/latest/
- https://docs.pytest.org/en/latest/goodpractices.html#test-discovery
- https://pytest-cov.readthedocs.io/en/latest/

Pytest is an extensible framework, and has a whole series of addons and plugins available on `PyPi <https://pypi.python.org/pypi?%3Aaction=search&term=pytest>`_.

You just can pip-install these packages:

.. code-block:: sh

  <env-dir>/bin/pip install pytest pytest-cov pytest-flask pytest-mccabe pytest-mock


.. note::

    Since the tests are importing the code of libranet_logging, this package needs be installed in a virtualenv,
    together with all its dependencies. See :doc:`installation`.


Re-usable test-fixtures
-----------------------

For our package, we have several application-specific test-fixtures in ``tests/conftest.py``:

.. literalinclude:: ../tests/conftest.py


Run tests
---------

Run pytest via:

.. code-block:: sh

  > cd <env-dir>
  > bin/py.test src/libranet_logging/

  > cd <env-dir>src/libranet_logging
  > py.test

   (libranet) wouter@midgard: <env-dir>src/libranet_logging >  make py

    platform linux -- Python 3.5.5, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
    rootdir: /opt/miniconda/envs/libranet/src/libranet_logging, inifile: setup.cfg
    plugins: xdist-1.22.2, tap-2.2, forked-0.2, flask-0.10.0, flake8-1.0.0, cov-2.5.1, celery-4.0.2
    collected 15 items

    ========== test session starts =====================
    tests/test_cli.py .
    tests/test_filters.py ....
    tests/test_logconfig.py ........
    tests/test_loglevel.py ..
    ========== 15 passed in 0.33 seconds ===============



Run tests with code-coverage
----------------------------

.. code-block:: sh

   > pytest --cov=libranet_logging --cov-report html .


..
   image:: img/coverage.png
..   :scale: 80%
..   :alt: code-coverage for libranet_logging
..   :align: center
