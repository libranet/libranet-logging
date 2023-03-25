# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_logging.logconfig."""
import logging

import pytest


# def test_is_interactive_shell_true(monkeypatch):
#     from libranet_logging.logconfig import is_interactive_shell

#     monkeypatch.setenv("TERM", "xterm")  # do not use: os.environ['TERM'] = 'xterm'
#     result = is_interactive_shell()
#     assert result


# def test_is_interactive_shell_false(monkeypatch):
#     from libranet_logging.logconfig import is_interactive_shell

#     monkeypatch.delenv("TERM")  # do not use: del os.environ['TERM']
#     result = is_interactive_shell()
#     assert not result


def test_initialize_non_logging_yml(tmpdir):
    from libranet_logging.logconfig import initialize

    non_logging_yml = tmpdir / "logging.yml"
    with pytest.raises(SystemExit) as excinfo:
        initialize(non_logging_yml)
    expected_msg = "\nThe configfile {} does not exist.\n".format(non_logging_yml)
    assert excinfo.value.code == expected_msg


def test_initialize_no_path():
    from libranet_logging.logconfig import initialize

    initialize("")
    expected = ["console", "debug_file", "info_file", "warning_file", "error_file"]
    assert [x.get_name() for x in logging.root.handlers] == expected


def test_initialize_with_invalid_yaml(tests_dir):
    from libranet_logging.logconfig import initialize

    logging_yml = tests_dir / "logging_invalid_yaml.yml"
    with pytest.raises(SystemExit) as excinfo:
        initialize(logging_yml)
    assert excinfo.value.code.startswith("Failed to load yml-file")


def test_initialize_with_invalid_yaml2(tests_dir):
    from libranet_logging.logconfig import initialize
    from libranet_logging.logconfig import CerberusValidationError

    logging_yml = tests_dir / "logging_invalid_schema.yml"

    with pytest.raises(CerberusValidationError) as excinfo:
        initialize(logging_yml)

    expected = (
        f"logconfig {logging_yml} contains errors: [('formatters', ['required field']), "
        "('handlers', ['required field']), ('loggers', ['required field']), "
        "('root', ['required field']), ('version', ['required field'])]"
    )
    assert excinfo.value.args[0] == expected


def test_initialize_with_valid_yaml(env, tests_dir):
    from libranet_logging.logconfig import initialize

    logging_yml = tests_dir / "logging_valid.yml"
    initialize(logging_yml)
    expected = ["console", "debug_file", "info_file", "warning_file", "error_file"]
    assert [x.get_name() for x in logging.root.handlers] == expected


def test_initialize_with_non_existing_logdir(monkeypatch, tests_dir, tmpdir):
    from libranet_logging.logconfig import initialize

    monkeypatch.delenv("PYTHON_LOG_DIR")
    monkeypatch.setenv("HOME", str(tmpdir))
    logging_yml = tests_dir / "logging_valid.yml"
    initialize(logging_yml, logdir=tmpdir / "log_non_default")
    assert (tmpdir / "log_non_default").exists()


def test_initialize_with_conflicting_logdir(monkeypatch, tests_dir, tmpdir):
    from libranet_logging.logconfig import initialize

    monkeypatch.delenv("PYTHON_LOG_DIR")
    monkeypatch.setenv("HOME", str(tmpdir))
    log_file = tmpdir.join("logs")
    log_file.write("content")
    logging_yml = tests_dir / "logging_valid.yml"
    with pytest.raises(OSError):
        initialize(logging_yml, logdir=tmpdir / "logs")
    assert (tmpdir / "logs").exists()
    assert (tmpdir / "logs").isfile()


# def test_initialize_noninteractive_with_valid_yaml(env, monkeypatch, tests_dir):
#     from libranet_logging.logconfig import initialize

#     monkeypatch.delenv("TERM")
#     logging_yml = tests_dir / "logging_valid.yml"
#     initialize(logging_yml)
#     expected = [
#         "console",
#         "debug_file",
#         "info_file",
#         "warning_file",
#         "error_file",
#     ]
#     assert [x.get_name() for x in logging.root.handlers] == expected


def test_initialize_with_logging_tree(capsys, env, monkeypatch, tests_dir):
    from libranet_logging.logconfig import initialize

    monkeypatch.setenv("PYTHON_ENABLE_LOGGING_TREE", "1")
    logging_yml = tests_dir / "logging_valid.yml"
    initialize(logging_yml)

    out, err = capsys.readouterr()
    substrings = [
        'o<--"libranet_logging"',
        "|   Level DEBUG",
        "|   |",
        '|   o<--"libranet_logging.logconfig"',
        "|       Level NOTSET so inherits level DEBUG",
        "|",
    ]
    assert err == ""
    for substring in substrings:
        assert substring in out


def test_initialize_without_logging_tree(capsys, env, monkeypatch, tests_dir):
    from libranet_logging.logconfig import initialize

    monkeypatch.delenv("PYTHON_ENABLE_LOGGING_TREE", raising=False)
    logging_yml = tests_dir / "logging_valid.yml"
    initialize(logging_yml)

    out, err = capsys.readouterr()
    substrings = [
        'o<--"libranet_logging"',
        "|   Level DEBUG",
        "|   |",
        '|   o<--"libranet_logging.logconfig"',
        "|       Level NOTSET so inherits level DEBUG",
        "|",
    ]
    assert err == ""
    for substring in substrings:
        assert substring not in out
