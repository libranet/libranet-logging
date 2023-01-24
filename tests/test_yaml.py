# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_logging.yaml."""


def test_read_yaml(env, monkeypatch, tests_dir):
    from libranet_logging.yaml import read_yaml

    monkeypatch.setenv("SMTP_SUBJECT", "my TEST subject")
    monkeypatch.setenv("SMTP_FROM", "test@example.com")
    monkeypatch.setenv("SMTP_TO", "xxx@example.com|yyy@example.com")

    existing_yaml_path = tests_dir / "logging_email_substitution.yml"
    data = read_yaml(existing_yaml_path)

    email = data["handlers"]["email"]
    assert email["fromaddr"] == "testg@example.com"
    assert email["toaddrs"] == ["xxx@example.com", "yyy@example.com"]
    assert email["subject"] == "my TEST subject"


def test_read_yaml_unset_envvar(env, monkeypatch, tests_dir):
    from libranet_logging.yaml import read_yaml

    monkeypatch.delenv("SMTP_SUBJECT", raising=False)
    monkeypatch.delenv("SMTP_FROM", raising=False)
    monkeypatch.delenv("SMTP_TO", raising=False)

    existing_yaml_path = tests_dir / "logging_email_substitution.yml"
    data = read_yaml(existing_yaml_path)

    email = data["handlers"]["email"]
    assert email["fromaddr"] == "app@example.com"
    assert email["toaddrs"] == ["xxx@example.com", "yyy@example.com"]
    assert email["subject"] == ""
