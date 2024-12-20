"""libranet_logging.validate."""

import logging
import logging.config

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

log = logging.getLogger(__name__)

logging_schema = {
    "type": "object",
    "properties": {
        # "logdir": {"type": "string", "required": False},  # custom field
        "version": {"type": "integer", "enum": [1]},  # Version is required and must be 1
        "disable_existing_loggers": {"type": "boolean"},
        "formatters": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "format": {"type": "string"},
                    "datefmt": {"type": "string"},
                },
                "required": ["format"],  # At least "format" is required in formatters
            },
        },
        "handlers": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "class": {"type": "string"},  # Required
                    "level": {"type": "string"},
                    "formatter": {"type": "string"},
                    "stream": {"type": "string"},
                    "filename": {"type": "string"},
                    "encoding": {"type": "string"},
                    "mode": {"type": "string"},
                    "maxBytes": {"type": "integer"},
                    "backupCount": {"type": "integer"},
                    "delay": {"type": "boolean"},
                    "filters": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
                "required": ["class"],  # "class" is always required for handlers
            },
        },
        "loggers": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "level": {"type": "string"},
                    "handlers": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                    "propagate": {"type": "boolean"},
                    "filters": {
                        "type": "array",
                        "items": {"type": "string"},
                    },
                },
            },
        },
        "root": {
            "type": "object",
            "properties": {
                "level": {"type": "string"},
                "handlers": {
                    "type": "array",
                    "items": {"type": "string"},
                },
                "filters": {
                    "type": "array",
                    "items": {"type": "string"},
                },
            },
            "required": ["level", "handlers"],  # "level" and "handlers" are required for root
        },
        "filters": {
            "type": "object",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "args": {"type": "object"},
                },
            },
        },
    },
    "required": ["version"],  # "version" is always required
    "additionalProperties": True,  # Disallow unknown properties at the top level
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
