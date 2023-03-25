[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/libranet/httpclient-logging/blob/main/docs/license.md) [![Read the Docs](https://readthedocs.org/projects/httpclient-logging/badge/?version=latest)](https://httpclient-logging.readthedocs.io/en/latest/) [![PyPi Package](https://img.shields.io/pypi/v/httpclient-logging?color=%2334D058&label=pypi%20package)](https://pypi.org/project/httpclient-logging/)


## Installation

Install via pip:

```bash
> bin/pip install httpclient_logging
```

Or add to your poetry-based project:

```bash
> poetry add httpclient_logging
```


## Usage

The only thing left to do for you is the create a ``.env`` in the root of your project.


## Registered sitecustomize-entrypoint

The ``httpclient_logging.entrypoint``-function is registered as a ``sitecustomize``-entrypoint in our pyproject.toml_:

``` toml
    [tool.poetry.plugins]
    [tool.poetry.plugins."sitecustomize"]
    httpclient_logging = "httpclient_logging:entrypoint"
```

Sitecustomize and all its registered entrypoints will be executed at the start of *every* python-process.
For more information, please see [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)


## Compatibility

 [![Python Version](https://img.shields.io/pypi/pyversions/httpclient-logging?:alt:PyPI-PythonVersion)](https://pypi.org/project/httpclient-logging/)
 [![PyPI - Implementation](https://img.shields.io/pypi/implementation/httpclient-logging?:alt:PyPI-Implementation)](https://pypi.org/project/httpclient-logging/)

``httpclient-logging``  works on Python 3.8+, including PyPy3. Tested until Python 3.11,


## Notable dependencies

- [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)
