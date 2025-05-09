"""libranet_logging._version.

Fetch metadata from the package's pyproject.toml.
The package must be properly installed in order the metadata to be available.

"""

from __future__ import annotations  # make | in typing work in Python 3.8

import importlib.metadata

try:
    pkginfo: dict = importlib.metadata.metadata(__package__).json
except AttributeError:
    pkginfo: dict = dict(importlib.metadata.metadata(__package__))

except importlib.metadata.PackageNotFoundError:  # pragma: no cover
    # fallback if this package is not properly installed
    pkginfo = {}


__metadata__: dict = pkginfo

__author__: str | list[str] = pkginfo.get("author", "unknown")

__author_email__: str | list[str] = pkginfo.get("author_email", "unknown")

__copyright__: str | list[str] = pkginfo.get("license", "unknown")

__description__: str | list[str] = pkginfo.get("summary", "unknown")

__license__: str | list[str] = pkginfo.get("license", "unknown")

__pkg_name__: str | list[str] = pkginfo.get("name", "unknown")

__readme__: str | list[str] = pkginfo.get("description", "unknown")

__title__ = __package__

__url__: str | list[str] = pkginfo.get("project_url", "unknown")

__version__: str | list[str] = pkginfo.get("version", "unknown")
