import click

from assistant.command import cli
from assistant.translator.command import translate


def add_subcommands(
        _cli: click.Group,
):
    _cli.add_command(translate)


if __name__ == '__main__':
    add_subcommands(cli)
    cli()
