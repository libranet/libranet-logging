# pylint: disable=missing-function-docstring
"""conftest.py - custom pytest-plugins.

For more information about conftest.py, please see:

 - https://docs.pytest.org/en/latest/writing_plugins.html
 - https://pytest-flask.readthedocs.io/en/latest/tutorial.html

"""

import os
import pathlib as pl

import pytest


@pytest.fixture(scope="session")
def tests_dir():
    tests_dir_ = os.path.dirname(os.path.realpath(__file__))
    return pl.Path(tests_dir_)


@pytest.fixture(scope="function")
def env(tmpdir):
    var_dir = tmpdir.mkdir("var")
    var_log_dir = var_dir.mkdir("log")
    # var_run_dir = var_dir.mkdir('run')
    # var_tmp_dir = var_dir.mkdir('tmp')

    # override any existing env-variable
    os.environ["LOG_DIR"] = str(var_log_dir)
    return tmpdir
