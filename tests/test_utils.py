# pylint: disable=missing-function-docstring
"""Testing of module libranet_logging.utils."""

import logging

import pytest

from libranet_logging.utils import ensure_dir, is_interactive_shell, print_loggers, print_tree, strtobool


def test_print_tree(capsys):
    print_tree()
    assert "<--" in capsys.readouterr().out  # logging_tree marks the root logger with '<--""'


def test_print_loggers(capsys):
    logging.getLogger("libranet_test_print_loggers").setLevel(logging.WARNING)
    # only creates a PlaceHolder for "libranet_test_placeholder", which must be skipped
    logging.getLogger("libranet_test_placeholder.child")

    print_loggers()

    out = capsys.readouterr().out
    assert "libranet_test_print_loggers - disabled: False - level: WARNING" in out
    assert "libranet_test_placeholder " not in out


@pytest.mark.parametrize("value", ["y", "yes", "t", "true", "on", "1", "TRUE", "Yes"])
def test_strtobool_true(value):
    assert strtobool(value) == 1


@pytest.mark.parametrize("value", ["n", "no", "f", "false", "off", "0", "FALSE", "No"])
def test_strtobool_false(value):
    assert strtobool(value) == 0


def test_strtobool_invalid():
    with pytest.raises(ValueError, match="invalid truth value maybe"):
        strtobool("maybe")


def test_is_interactive_shell(monkeypatch):
    monkeypatch.setenv("TERM", "xterm-256color")
    assert is_interactive_shell() is True


def test_is_not_interactive_shell(monkeypatch):
    monkeypatch.delenv("TERM", raising=False)
    assert is_interactive_shell() is False


def test_ensure_dir_creates_nested_dir_from_str(tmp_path):
    required_dir = tmp_path / "a" / "b"

    ensure_dir(str(required_dir))

    assert required_dir.is_dir()


def test_ensure_dir_existing_dir(tmp_path):
    ensure_dir(tmp_path)

    assert tmp_path.is_dir()


def test_ensure_dir_existing_file(tmp_path):
    existing_file = tmp_path / "file.txt"
    existing_file.write_text("")

    with pytest.raises(FileExistsError, match="already exists and is not a directory"):
        ensure_dir(existing_file)
