"""libranet_logging.validate."""

import logging
import logging.config

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

log = logging.getLogger(__name__)


logging_schema = {
    "logdir": {"type": "string", "required": False},
    "version": {"type": "integer", "required": True},
    "disable_existing_loggers": {"type": "integer"},
    "formatters": {
        "type": "dict",
        "required": True,
        "valuesrules": {
            "type": "dict",
            "schema": {
                "format": {"type": "string", "required": False},
                "datefmt": {"type": "string", "required": False},
            },
        },
    },
    "handlers": {
        "type": "dict",
        "required": True,
        "valuesrules": {
            "type": "dict",
            "schema": {
                "class": {"type": "string", "required": True},
                # logstash-handler sets the correct formatter via code
                # therefore the formatter-key in not required in logging.yml
                "formatter": {"type": "string", "required": False},
                "level": {"type": "string", "required": True},
                "encoding": {"type": "string", "required": False},
                "filename": {"type": "string", "required": False},
                "stream": {"type": "string", "required": False},
                "maxBytes": {"type": "integer", "required": False},
                "backupCount": {"type": "integer", "required": False},
            },
        },
    },
    "loggers": {
        "type": "dict",
        "required": True,
        "valuesrules": {
            "type": "dict",
            "schema": {
                "handlers": {"type": "list", "required": False},
                "level": {"type": "string", "required": False},
                "propagate": {"type": "boolean", "required": False},
            },
        },
    },
    "root": {
        "type": "dict",
        "required": True,
        "schema": {"handlers": {"type": "list", "required": True}, "level": {"type": "string"}},
    },
}


class SchemaValidationError(Exception):
    """SchemaValidationError-class."""


def validate_logging(log_config, path):
    """Validate the syntax of a logging.yml-file."""
    if not jsonschema:  # pragma: no cover
        return

    try:
        jsonschema.validate(instance=log_config, schema=logging_schema)
    except jsonschema.exceptions.ValidationError as exc:
        msg = f"logconfig {path} contains errors: {exc.message}"
        raise SchemaValidationError(msg)
