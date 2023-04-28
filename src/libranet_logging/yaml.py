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
import typing as tp

import yaml


def constructor_env(loader: tp.Any, node: tp.Any) -> tp.Union[str, tp.List[str]]:
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

    sep = os.getenv("LIBRANET_LOGGING_SEPARATOR", "|")
    if value and sep in value:
        # env-variable as array, convert to list
        value = [val.strip() for val in value.split(sep) if val]  # type: ignore[assignment]

    return value


def add_constructor() -> None:
    """Register the !env-constructor with pyyaml."""
    # breakpoint()
    # loader = yaml.loader.FullLoader
    # loader.add_constructor("!env", constructor_env)
    # print("add_constructor")
    yaml.add_constructor("!env", constructor_env, yaml.SafeLoader)

    # try:
    #    import ruamel.yaml
    #    import ruamel.yaml.constructor

    #    # ruamel.yaml.constructor.add_constructor("!env", constructor_env, Loader=ruamel.yaml.YAML(typ="safe"))
    #    ruamel.yaml.add_constructor("!env", constructor_env)
    #    # print("succes")

    # except ImportError as exc:
    #    print(exc)


def read_yaml(yaml_path: str, variables: tp.Optional[tp.Dict[str, str]] = None) -> tp.Dict:
    """Read the yaml-file.

    Returns: dict
    """
    if not variables:
        variables = {}

    if not os.path.exists(yaml_path):
        msg = f"\nThe configfile {yaml_path} does not exist.\n"
        raise SystemExit(msg)

    loader = yaml.loader.FullLoader
    loader.add_constructor("!env", constructor_env)
    # yaml.add_constructor("!env", constructor_env, yaml.SafeLoader)

    with open(yaml_path, "r", encoding="utf-8") as stream:
        try:
            data = stream.read()
            if variables:
                data = data.format(**variables)  # TODO, will break on %s() in yaml

            data_yaml = yaml.load(data, Loader=loader)
            # data_yaml = yaml.safe_load(data)

        except yaml.YAMLError as exc:
            msg = f"Failed to load yml-file {yaml_path}: {exc}"
            raise SystemExit(msg)

    return data_yaml
