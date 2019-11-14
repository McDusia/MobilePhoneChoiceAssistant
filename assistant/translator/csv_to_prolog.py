import ast
import csv
import statistics as stats
import string
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Tuple

from assistant.translator.features import BatteryCapacity
from assistant.translator.features import CpuFrequency

__all__ = ["translate_file"]


def translate_file(
        reader: csv.DictReader,
) -> Generator[str, None, None]:
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
    _RULE_TEMPLATE = string.Template("$threshold({name}, {key}, {value}).\n")
    _UP_THRESHOLD_TEMPLATE = _RULE_TEMPLATE.substitute(threshold="up_threshold")
    _DOWN_THRESHOLD_TEMPLATE = _RULE_TEMPLATE.substitute(threshold="down_threshold")

    def __init__(self) -> None:
        self._battery_capacities: List[int] = list()
        self._cpu_frequencies: List[int] = list()

    def aggregate(
            self,
            row: PhoneSpecRow,
    ):
        self._try_add(row["battery_capacity"], int, self._battery_capacities)
        self._try_add(row["cpu_frequency"], int, self._cpu_frequencies)

    @property
    def aggregated_rules(self) -> Generator[str, None, None]:
        for battery_capacity, threshold in self._battery_thresholds.items():
            yield self._UP_THRESHOLD_TEMPLATE.format(
                name="battery_capacity",
                key=battery_capacity.value,
                value=threshold,
            )
        cpu_thresholds = self._cpu_frequency_thresholds
        yield self._UP_THRESHOLD_TEMPLATE.format(
            name="cpu_frequency",
            key=CpuFrequency.HIGH.value,
            value=cpu_thresholds[CpuFrequency.HIGH],
        )
        yield self._DOWN_THRESHOLD_TEMPLATE.format(
            name="cpu_frequency",
            key=CpuFrequency.LOW.value,
            value=cpu_thresholds[CpuFrequency.LOW],
        )

    @property
    def _battery_thresholds(
            self,
    ) -> Dict[BatteryCapacity, int]:
        mean_bc = stats.mean(self._battery_capacities)
        stdev_bc = stats.stdev(self._battery_capacities)
        return {
            BatteryCapacity.LARGE: mean_bc + 2 * stdev_bc,
            BatteryCapacity.BIG: mean_bc + stdev_bc,
            BatteryCapacity.OK: mean_bc,
        }

    @property
    def _cpu_frequency_thresholds(
            self,
    ) -> Dict[CpuFrequency, int]:
        mean_freq = stats.mean(self._cpu_frequencies)
        stdev_freq = stats.stdev(self._cpu_frequencies)
        return {
            CpuFrequency.LOW: mean_freq,
            CpuFrequency.HIGH: mean_freq + stdev_freq
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
    _RULE_TEMPLATE = """\
{facts}.
"""

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

    _FACT_TEMPLATE_HAS = 'has("{model}", {key}, {value})'

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
        facts_str = ",\n".join(f"{fact}"
                               for fact in facts)

        self._aggregated_rules_generator.aggregate(row)

        return RulesTranslator._RULE_TEMPLATE.format(
            model=row["model"],
            facts=facts_str,
        )

    @staticmethod
    def _facts(row: PhoneSpecRow) -> Generator[str, None, None]:
        model = row["model"]
        for dict_key, fact_key, mapping in RulesTranslator._HAS_FACTS:
            values = parse_value(row[dict_key])
            yield from (RulesTranslator._FACT_TEMPLATE_HAS.format(model=model,
                                                                  key=fact_key,
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
