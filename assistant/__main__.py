import click

from assistant.command import cli
from assistant.price_generator.command import add_price_column
from assistant.translator.command import translate


def add_subcommands(
        _cli: click.Group,
):
    _cli.add_command(translate)
    _cli.add_command(add_price_column)


if __name__ == '__main__':
    add_subcommands(cli)
    cli()
