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

from assistant.translator.features import BatteryCapacity, CPUFrequency, Storage, FrontCameraMatrix, DisplaySize, \
    CPUNCores, DisplayWidth, DisplayHeight, Price

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
    _DOWN_THRESHOLD_TEMPLATE = _RULE_TEMPLATE.substitute(threshold="down_threshold")

    def __init__(self) -> None:
        self._battery_capacities: List[int] = list()
        self._cpu_frequencies: List[int] = list()
        self._storages: List[int] = list()
        self._front_cameras: List[float] = list()
        self._display_diagonals: List[float] = list()
        self._cpu_n_cores: List[int] = list()
        self._display_heights: List[int] = list()
        self._display_widths: List[int] = list()
        self._prices: List[float] = list()

    def aggregate(
            self,
            row: PhoneSpecRow,
    ):
        self._try_add(row["battery_capacity"], int, self._battery_capacities)
        self._try_add(row["cpu_frequency"], int, self._cpu_frequencies)
        self._try_add(row["storage"], int, self._storages)
        self._try_add(row["front_camera_matrix"], float, self._front_cameras) #tutaj musi zwracac nie float ale cos co bedzie zmieniac liste  na liste float (mozna uzytc tego parse_value)
        self._try_add(row["display_diagonal"], float, self._display_diagonals)
        self._try_add(row["cpu_n_cores"], int, self._cpu_n_cores)
        self._try_add(row["display_height"], int, self._display_heights)
        self._try_add(row["display_width"], int, self._display_widths)
        self._try_add(row["price"], float, self._prices)

    @property
    def aggregated_rules(self) -> Generator[str, None, None]:

        for front_camera_matrix, threshold in self._front_camera_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="front_camera_matrix",
                key=front_camera_matrix.value,
                value=threshold,
            )

        for cpu_n_cores, threshold in self._cpu_n_cores_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="cpu_n_cores",
                key=cpu_n_cores.value,
                value=threshold,
            )

        for battery_capacity, threshold in self._battery_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="battery_capacity",
                key=battery_capacity.value,
                value=threshold,
            )

        for display_height, threshold in self._display_height_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="display_height",
                key=display_height.value,
                value=threshold,
            )

        for display_width, threshold in self._display_width_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="display_width",
                key=display_width.value,
                value=threshold,
            )

        for price, threshold in self._prices_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="price",
                key=price.value,
                value=threshold,
            )

        cpu_thresholds = self._cpu_frequency_thresholds
        yield self._DOWN_THRESHOLD_TEMPLATE.format(
            name="cpu_frequency",
            key=CPUFrequency.HIGH.value,
            value=cpu_thresholds[CPUFrequency.HIGH],
        )
        yield self._DOWN_THRESHOLD_TEMPLATE.format(
            name="cpu_frequency",
            key=CPUFrequency.LOW.value,
            value=cpu_thresholds[CPUFrequency.LOW],
        )

        for display_diagonal, threshold in self._display_diagonals_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="display_diagonal",
                key=display_diagonal.value,
                value=threshold,
            )

        storage_thresholds = self._storage_thresholds
        yield self._DOWN_THRESHOLD_TEMPLATE.format(
            name='storage',
            key=Storage.LOW.value,
            value=storage_thresholds[Storage.LOW],
        )

        yield self._DOWN_THRESHOLD_TEMPLATE.format(
            name='storage',
            key=Storage.HIGH.value,
            value=storage_thresholds[Storage.HIGH],
        )

        yield self._DOWN_THRESHOLD_TEMPLATE.format(
            name='storage',
            key=Storage.MEDIUM.value,
            value=storage_thresholds[Storage.MEDIUM],
        )

    @property
    def _front_camera_thresholds(
            self,
    ) -> Dict[FrontCameraMatrix, float]:
        mean = stats.mean(self._front_cameras)
        stdev = stats.stdev(self._front_cameras)
        return {
            FrontCameraMatrix.GOOD: mean + stdev,
            FrontCameraMatrix.EXCELLENT: mean + 2 * stdev,
            FrontCameraMatrix.IRRELEVANT: mean,
        }

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
    def _display_diagonals_thresholds(
            self,
    ) -> Dict[DisplaySize, float]:
        mean = stats.mean(self._display_diagonals)
        stdev = stats.stdev(self._display_diagonals)
        return {
            DisplaySize.BIG: mean + 2 * stdev,
            DisplaySize.MEDIUM: mean + stdev,
            DisplaySize.SMALL: mean,
        }

    @property
    def _display_height_thresholds(
            self,
    ) -> Dict[DisplayHeight, int]:
        mean = stats.mean(self._display_heights)
        stdev = stats.stdev(self._display_diagonals)
        return {
            DisplayHeight.BIG: mean + 2 * stdev,
            DisplayHeight.MEDIUM: mean + stdev,
            DisplayHeight.SMALL: mean,
        }

    @property
    def _display_width_thresholds(
            self,
    ) -> Dict[DisplayWidth, int]:
        mean = stats.mean(self._display_widths)
        stdev = stats.stdev(self._display_widths)
        return {
            DisplayWidth.BIG: mean + 2 * stdev,
            DisplayWidth.MEDIUM: mean + stdev,
            DisplayWidth.SMALL: mean,
        }

    @property
    def _cpu_n_cores_thresholds(
            self,
    ) -> Dict[CPUNCores, float]:
        mean = stats.mean(self._cpu_n_cores)
        stdev = stats.stdev(self._cpu_n_cores)
        return {
            CPUNCores.MANY: mean + 2 * stdev,
            CPUNCores.MEDIUM_AMOUNT: mean + stdev,
            CPUNCores.IRRELEVANT: mean,
        }

    @property
    def _storage_thresholds(
            self,
    ) -> Dict[Storage, int]:
        mean_s = stats.mean(self._storages)
        stdev_s = stats.stdev(self._storages)
        return {
            Storage.HIGH: mean_s + 2 * stdev_s,
            Storage.MEDIUM: mean_s + stdev_s,
            Storage.LOW: mean_s,
        }

    @property
    def _cpu_frequency_thresholds(
            self,
    ) -> Dict[CPUFrequency, int]:
        mean_freq = stats.mean(self._cpu_frequencies)
        stdev_freq = stats.stdev(self._cpu_frequencies)
        return {
            CPUFrequency.LOW: mean_freq,
            CPUFrequency.HIGH: mean_freq + stdev_freq
        }

    @property
    def _prices_thresholds(
            self,
    ) -> Dict[Price, int]:
        mean_freq = stats.mean(self._prices)
        stdev_freq = stats.stdev(self._prices)
        return {
            Price.CHEAP: mean_freq,
            Price.HIGH: mean_freq + stdev_freq
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

    @staticmethod
    def _try_add_multiple_values(
            maybe_value: Optional[Any],
            mapping: Callable[[Any], List[Any]],
            values_list: List[Any],
    ):
        if maybe_value:
            try:
                new_items = mapping(maybe_value)
                values_list.extend(new_items)
            except:
                pass


def brand_from_model(model: str) -> str:
    return f'"{model.split(maxsplit=1)[0]}"'


class RulesTranslator:
    _RULE_TEMPLATE = """\
{facts}.
"""

    _HAS_FACTS: List[Tuple[DictKey, FactKey, Mapping]] = [
        ("model", "brand", brand_from_model),
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
        ("price", "price", float),
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
        facts_str = ".\n".join(f"{fact}"
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
