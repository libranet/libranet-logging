# -*- coding: utf-8 -*-
"""conftest.py - custom pytest-plugins.

For more information about conftest.py, please see:

 - https://docs.pytest.org/en/latest/writing_plugins.html
 - https://pytest-flask.readthedocs.io/en/latest/tutorial.html

"""
import os
import pathlib

import pkg_resources
import pytest


@pytest.fixture(scope="session")
def tests_dir():
    tests_dir = os.path.dirname(os.path.realpath(__file__))
    return pathlib.Path(tests_dir)


@pytest.fixture(scope="session")
def pkg_dir():
    pkg_dir = pkg_resources.resource_filename("libranet_logging", "")
    return pathlib.Path(pkg_dir)


@pytest.fixture(scope="function")
def env(tmpdir):
    var_dir = tmpdir.mkdir("var")
    var_log_dir = var_dir.mkdir("log")
    # var_run_dir = var_dir.mkdir('run')
    # var_tmp_dir = var_dir.mkdir('tmp')

    # override any existing env-variable
    os.environ["PYTHON_LOG_DIR"] = str(var_log_dir)
    return tmpdir
