# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module libranet_logging.cli."""


def test_print_logging_tree(cli_runner, env, tmpdir):
    from libranet_logging.cli import print_logging_tree

    result = cli_runner.invoke(print_logging_tree, [])
    assert result.exit_code == 0
    assert len(result.output) > 2000

    substrings = [
        "Logging configured from",
        "Level DEBUG",
        # "Handler Stream <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>",
        "Handler Stream ",
        "  Level DEBUG",
        "  Filter <libranet_logging.filters.RegexFilter object at 0x",
        # "  Formatter <colorlog.colorlog.ColoredFormatter object at 0x",
        f"Handler RotatingFile '{tmpdir}",
        "  Level DEBUG",
        "  Filter <libranet_logging.filters.RegexFilter object at 0x",
        "  Formatter fmt='%(asctime)s - %(name)s - %(levelname)-7s - %(message)s' datefmt='%Y/%m/%d %H:%M:%S'",
        f"Handler RotatingFile '{tmpdir}",
        "  Level INFO",
        "  Filter <libranet_logging.filters.RegexFilter object at 0x",
        "  Formatter fmt='%(asctime)s - %(name)s - %(levelname)-7s - %(message)s' datefmt='%Y/%m/%d %H:%M:%S'",
        f"Handler RotatingFile '{tmpdir}",
        "  Level WARNING",
        "  Filter <libranet_logging.filters.RegexFilter object at 0x",
        "  Formatter fmt='%(asctime)s - %(name)s - %(levelname)-7s - %(message)s' datefmt='%Y/%m/%d %H:%M:%S'",
        f"Handler RotatingFile '{tmpdir}",
        "  Level ERROR",
        "  Filter <libranet_logging.filters.RegexFilter object at 0x",
        "  Formatter fmt='%(asctime)s - %(name)s - %(levelname)-7s - %(message)s' datefmt='%Y/%m/%d %H:%M:%S'",
        "|",
        'o<--"libranet_logging"',
        "|   Level DEBUG",
        "|   |",
        '|   o<--"libranet_logging.logconfig"',
        "|       Level NOTSET so inherits level DEBUG",
        "|",
        'o<--"requests"',
        "|   Level DEBUG",
        "|",
        'o<--"sh"',
        "|   Level DEBUG",
        "|",
        'o<--"sqlalchemy"',
        "|   Level DEBUG",
        "|",
        'o<--"urllib3"',
        "|   Level DEBUG",
    ]
    for substring in substrings:
        assert substring in result.output
