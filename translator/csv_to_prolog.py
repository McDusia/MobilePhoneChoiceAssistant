import ast
import csv
import string
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generator
from typing import List
from typing import Tuple

__all__ = ["translate_file"]


def translate_file(
        reader: csv.DictReader,
) -> Generator[str, None, None]:
    output_chunk = """\
:- dynamic
    has/2.
"""
    yield output_chunk

    translator = RulesTranslator()

    for row in reader:
        yield translator.row_to_rule(row)


def prolog_bool(x: str) -> str:
    return str(bool(int(x))).lower()


Mapping = Callable[[str], Any]
DictKey = str
FactKey = str
PhoneSpecRow = Dict[str, str]


class RulesTranslator:
    _RULE_TEMPLATE = string.Template("""\
model("$model") :- $facts.
""")

    _HAS_FACTS: List[Tuple[DictKey, FactKey, Mapping]] = [
        ("battery_capacity", "battery_capacity", int),
        ("memory", "memory", int),
        ("display_diagonal", "display_diagonal", float),
        ("display_width", "display_width", int),
        ("display_height", "display_height", int),
        ("display_number_of_colors", "display_number_of_colors", int),
        ("storage", "storage", int),
        ("touch_screen", "touch_screen", prolog_bool),
        ("NFC", "nfc", prolog_bool),
        ("water_resistant", "water_resistant", prolog_bool),
        ("dual_sim", "dual_sim", prolog_bool),
        ("android_version", "android_version", float),
        ("cpu_frequency", "cpu_frequency", int),
        ("cpu_n_cores", "cpu_n_cores", int),
        ("gps", "gps", prolog_bool),
        ("agps", "agps", prolog_bool),
        ("glonass", "glonass", prolog_bool),
        ("galileo", "galileo", prolog_bool),
        ("quick_charge", "quick_charge", prolog_bool),
        ("has_jack", "has_jack", prolog_bool),
        ("usb_c", "usb_c", prolog_bool),
        ("sim_types", "sim_type", str),
        ("back_camera_matrix", "back_camera_matrix", float),
        ("front_camera_matrix", "front_camera_matrix", float),
    ]

    _FACT_TEMPLATE_HAS = string.Template("has($key, $value)")

    @staticmethod
    def row_to_rule(
            row: PhoneSpecRow,
    ) -> str:
        facts = RulesTranslator._facts(row)
        facts_str = ",".join(f"\n\t{fact}"
                             for fact in facts)
        return RulesTranslator._RULE_TEMPLATE.substitute(
            model=row["model"],
            facts=facts_str,
        )

    @staticmethod
    def _facts(row: PhoneSpecRow) -> Generator[str, None, None]:
        for dict_key, fact_key, mapping in RulesTranslator._HAS_FACTS:
            values = parse_value(row[dict_key])
            yield from (RulesTranslator._FACT_TEMPLATE_HAS.substitute(key=fact_key,
                                                                      value=mapping(value))
                        for value in values)


def parse_value(
        raw_value: str
) -> List[str]:
    if raw_value == "NA":
        return []
    if raw_value.startswith("[") and raw_value.endswith("]"):
        return ast.literal_eval(raw_value)
    else:
        return raw_value.split(",")
