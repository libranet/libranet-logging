# pylint: disable=unused-import
# pylint: disable=wrong-import-position
# pylint: disable=invalid-name
# ruff: noqa: INP001 (implicit part of namespace package)
# ruff: noqa: E402 (module level import not at top of file)
# ruff: noqa: F401 (unused import)
"""IPython startup-file, outside of PYTHONPATH.

Files in this startup-folder will be run in lexicographical order,
so you can control the execution order of files with a prefix, e.g.::

    00-foo.py
    10-baz.py
    20-bar.py

return-statements are not allowed.

"""

print(f"\nRunning {__file__}")

import logging
import os
import sys

import libranet_logging

# setup the logging according to etc/logging.yml
libranet_logging.initialize()

log = logging.getLogger("ipython-startup")  

log.debug("debug-message")
log.info("info-message")
log.warning("warning-message")
log.error("error-message")
log.critical("critical-message")
