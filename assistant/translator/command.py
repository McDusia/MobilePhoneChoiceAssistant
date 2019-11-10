import csv
import sys
from typing import TextIO

import click

from assistant.translator.csv_to_prolog import translate_file


@click.command(name="translate")
@click.argument("input-file", type=click.Path(exists=True, dir_okay=False))
def translate(
        input_file: str,
):
    """
    Translates .csv knowledge base to Prolog
    """
    output_file: TextIO = sys.stdout

    with open(input_file, "rt") as f:
        reader = csv.DictReader(f)
        for lines in translate_file(reader):
            output_file.write(lines)
