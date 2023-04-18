"""libranet_logging.validate."""

import logging
import logging.config

try:
    import cerberus
except ImportError:  # pragma: no cover
    cerberus = None

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


class CerberusValidationError(Exception):
    """CerberusValidationError-class."""


def validate_logging(log_config, path):
    """Validate the syntax of a logging.yml-file."""
    if not cerberus:  # pragma: no cover
        return

    validator = cerberus.Validator(logging_schema, allow_unknown=True)
    success = validator.validate(log_config)
    if not success and validator.errors:
        sorted_errors = sorted(validator.errors.items())
        msg = f"logconfig {path} contains errors: {sorted_errors}"
        raise CerberusValidationError(msg)
