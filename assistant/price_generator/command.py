import csv
import sys
from typing import TextIO

import click

from assistant.price_generator.generator import PriceGenerator


@click.command()
@click.argument("input-file", type=click.Path(exists=True, dir_okay=False))
def add_price_column(
        input_file: str,
):
    """
    For each .csv file row generates price based on other columns.
    """
    generator = PriceGenerator()
    output_file: TextIO = sys.stdout

    with open(input_file, "rt") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + ["price"]

        writer = csv.DictWriter(output_file, fieldnames)
        writer.writeheader()
        for row in reader:
            price = generator.price_for(row)
            row["price"] = price
            writer.writerow(row)
