# -*- coding: utf-8 -*-
"""A setuptools based setup module.

For more information, please see:
- https://pypi.python.org/pypi/setuptools
- https://pythonhosted.org/setuptools
- https://python-packaging-user-guide.readthedocs.io/en/latest/distributing/
- https://packaging.python.org/en/latest/distributing.html
- https://github.com/pypa/sampleproject
- https://packaging.python.org/guides/single-sourcing-package-version

Important note: Please avoid importing any module of this package.

"""
import glob
import io
import os

import setuptools


def read(*names, **kwargs):
    r"""Return the contents of a file.

    Default encoding is UTF-8, unless specified otherwise.

    Args:
        - names (list, required): list of strings, parts of the path.
          the path might be relative to the current file.

    Keyword Args:
        **kwargs: Arbitrary keyword arguments.

    Returns:
      String containing the content of the file.

    Examples:
        >>> read('docs/readme.rst')
            u'Overview\n--------\n...'

        >>> read('docs', 'readme.rst')
            u'Overview\n--------\n...'

    """
    fn = os.path.join(os.path.dirname(__file__), *names)
    with io.open(fn, encoding=kwargs.get("encoding", "utf8")) as stream:
        return stream.read()


def read_version(*names):
    """
    Returns:
          str: the version-number of the package.

    Examples:
        >>> read_version("src/libranet_logging/__init__.py")
            "0.1dev0"

    """
    lines = read(*names).split("\n")
    for line in lines:
        if line.startswith("__version__"):
            version_ = line.split("=")[1].strip().strip('"').strip("'")
            return version_
    raise RuntimeError("Unable to find version string.")


version = read_version("src/libranet_logging/__init__.py")

long_description = (
    read("docs/readme.rst")
    + "\n\n"
    + read("docs/changes.rst")
    + "\n\n"
    + read("docs/contributors.rst")
)


classifiers = [
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
]
install_requires = [
    "cerberus>=1.3.1",
    "click",
    "colorlog",  # used directly in logging.yml
    "logging_tree",
    "PyYAML",
    "setuptools",
]

tests_require = ["coverage", "pytest", "pytest-click", "pytest-cov"]

sphinx_require = ["recommonmark", "Sphinx", "sphinx-rtd-theme"]

extras_require = {
    "testing": tests_require,  # install via ``pip install ".[testing]"``
    "sphinx": sphinx_require,  # install via ``pip install ".[sphinx]"``
}


setuptools.setup(
    name="libranet_logging",
    version=version,
    description="Easy-to-use logging-configuration using a logging.yml-file.",
    long_description=long_description,
    classifiers=classifiers,
    keywords="python logging yaml loggers handlers filters",
    author="Wouter Vanden Hove",
    author_email="wouter@wvhconsulting.org",
    url="https://github.com/Libranet/libranet_logging",
    license="MIT",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[
        os.path.splitext(os.path.basename(path))[0] for path in glob.glob("src/*.py")
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "libranet-print-logging-tree = libranet_logging.cli:print_logging_tree"
        ]
    },
    scripts=glob.glob("scripts/*"),
)
