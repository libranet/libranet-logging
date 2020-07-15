# -*- coding: utf-8 -*-
"""Testing of module libranet_logging.yaml."""
from libranet_logging.yaml import read_yaml


def test_read_yaml(env, monkeypatch, tests_dir):
    monkeypatch.setenv("SMTP_SUBJECT", "my TEST subject")
    monkeypatch.setenv("SMTP_FROM", "testing@ondernemersnetwerk.be")
    monkeypatch.setenv("SMTP_TO", "xxx@ondernemersnetwerk.be;yyy@ondernemersnetwerk.be")

    existing_yaml_path = tests_dir / "logging_email_substitution.yml"
    data = read_yaml(existing_yaml_path)

    email = data["handlers"]["email"]
    assert email["fromaddr"] == "testing@ondernemersnetwerk.be"
    assert email["toaddrs"] == ["xxx@ondernemersnetwerk.be", "yyy@ondernemersnetwerk.be"]
    assert email["subject"] == "my TEST subject"


def test_read_yaml_unset_envvar(env, monkeypatch, tests_dir):
    monkeypatch.delenv("SMTP_SUBJECT", raising=False)
    monkeypatch.delenv("SMTP_FROM", raising=False)
    monkeypatch.delenv("SMTP_TO", raising=False)

    existing_yaml_path = tests_dir / "logging_email_substitution.yml"
    data = read_yaml(existing_yaml_path)

    email = data["handlers"]["email"]
    assert email["fromaddr"] == "application@ondernemersnetwerk.be"
    assert email["toaddrs"] == ["xxx@ondernemersnetwerk.be", "yyy@ondernemersnetwerk.be"]
    assert email["subject"] == ""
