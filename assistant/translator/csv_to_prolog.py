import ast
import csv
import string
import statistics as stats
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Tuple

from assistant.features import BatteryLife

__all__ = ["translate_file"]


def translate_file(
        reader: csv.DictReader,
) -> Generator[str, None, None]:
    output_chunk = """\
:- dynamic
    has/2.
"""
    yield output_chunk

    aggregated_rules_generator = AggregatedRulesGenerator()
    translator = RulesTranslator(aggregated_rules_generator)

    for row in reader:
        yield translator.row_to_rule(row)

    yield from aggregated_rules_generator.aggregated_rules


def prolog_bool(x: str) -> str:
    return str(bool(int(x))).lower()


Mapping = Callable[[str], Any]
DictKey = str
FactKey = str
PhoneSpecRow = Dict[str, str]


class AggregatedRulesGenerator:
    _RULE_TEMPLATE = string.Template("$name($key, $value).\n")

    def __init__(self) -> None:
        self._battery_capacities: List[int] = list()

    def aggregate(
            self,
            row: PhoneSpecRow,
    ):
        self._try_add(row["battery_capacity"], int, self._battery_capacities)

    @property
    def aggregated_rules(self) -> Generator[str, None, None]:
        for battery_life, threshold in self._battery_lifes.items():
            yield self._RULE_TEMPLATE.substitute(
                name="battery_threshold",
                key=battery_life.value,
                value=threshold,
            )

    @property
    def _battery_lifes(
            self,
    ) -> Dict[BatteryLife, int]:
        mean_bc = stats.mean(self._battery_capacities)
        stdev_bc = stats.stdev(self._battery_capacities)
        return {
            BatteryLife.EXCELLENT: mean_bc + 2 * stdev_bc,
            BatteryLife.GOOD: mean_bc + stdev_bc,
            BatteryLife.IRRELEVANT: 0,
        }

    @staticmethod
    def _try_add(
            maybe_value: Optional[Any],
            mapping: Callable[[Any], Any],
            values_list: List[Any],
    ):
        if maybe_value:
            try:
                values_list.append(mapping(maybe_value))
            except:
                pass


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

    def __init__(
            self,
            aggregated_rules_generator: AggregatedRulesGenerator,
    ):
        self._aggregated_rules_generator = aggregated_rules_generator

    def row_to_rule(
            self,
            row: PhoneSpecRow,
    ) -> str:
        facts = RulesTranslator._facts(row)
        facts_str = ",".join(f"\n\t{fact}"
                             for fact in facts)

        self._aggregated_rules_generator.aggregate(row)

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
