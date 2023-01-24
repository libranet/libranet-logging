# -*- coding: utf-8 -*-
"""libranet_logging.yaml.

In pyyaml 5.1 some incompatibilies were introduced with regard to ``yaml.load``
to make it more safe by default.

please see:
  - https://github.com/yaml/pyyaml/blob/master/CHANGES
  - https://github.com/yaml/pyyaml/pull/257
  - https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation

"""
import json
import os

import yaml


def constructor_env(loader, node):
    """YAML-Constructor to load a value from a env-variable.

    Usage in yml:
        > !env ENVVAR_NAME, DEFAULTVALUE_IF_ENVVAR_NOT_SET

    """

    if "," not in node.value:
        # no default-value provided
        envname = loader.construct_scalar(node)
        default = ""
    else:
        envname, default = loader.construct_scalar(node).split(",", 1)
        default = default.replace('"', "").replace("'", "").strip()

        try:
            # "null" -> None
            default = json.loads(default)
        except json.JSONDecodeError:
            pass

    value = os.environ.get(envname) or default

    sep = os.getenv("LIBRANET_LOGGING_SEPARATOR","|")
    if value and sep in value:
        # env-variable as array, convert to list
        value = [x.strip() for x in value.split(sep) if x]

    return value


def read_yaml(path, variables=None):
    """Read the yaml-file.

    Returns: dict
    """
    path = str(path)
    if not variables:
        variables = {}

    if not os.path.exists(path):
        msg = f"\nThe configfile {path} does not exist.\n"
        raise SystemExit(msg)

    try:  # Pyyaml >= 5.1
        loader = yaml.loader.FullLoader
        loader.add_constructor(u"!env", constructor_env)
    except AttributeError:  # pragma: no cover, PyYaml < 5.0
        loader = None
        yaml.add_constructor(u"!env", constructor_env)

    with open(path, "r") as stream:
        try:
            data = stream.read()
            if variables:
                data = data.format(**variables)  # TODO, will break on %s() in yml
            if loader:
                data_yml = yaml.load(data, Loader=loader)
            else:  # pragma: no cover, PyYaml < 5.0
                data_yml = yaml.load(data)
        except Exception as exc:
            msg = f"Failed to load yml-file {path}: {exc}"
            raise SystemExit(msg)

    return data_yml
