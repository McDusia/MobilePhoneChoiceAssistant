import ast
import csv
import numpy as np
import string
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Tuple

from assistant.translator.features import BatteryCapacity, CPUFrequency, Storage, FrontCameraMatrix, DisplayDiagonal, \
    CPUNCores, DisplayWidth, DisplayHeight, Price, BackCameraMatrix

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
        self._back_cameras: List[float] = list()
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
        self._try_add(row["back_camera_matrix"], float, self._back_cameras)
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

        for back_camera_matrix, threshold in self._back_camera_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="back_camera_matrix",
                key=back_camera_matrix.value,
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

        for cpu_frequency, threshold in self._cpu_frequency_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="cpu_frequency",
                key=cpu_frequency.value,
                value=threshold,
            )

        for storage, threshold in self._storage_thresholds.items():
            yield self._DOWN_THRESHOLD_TEMPLATE.format(
                name="storage",
                key=storage.value,
                value=threshold,
            )

    @property
    def _front_camera_thresholds(
            self,
    ) -> Dict[FrontCameraMatrix, float]:
        return {
            FrontCameraMatrix.GOOD: np.percentile(self._front_cameras,50),
            FrontCameraMatrix.EXCELLENT: np.percentile(self._front_cameras, 75),
            FrontCameraMatrix.IRRELEVANT: np.percentile(self._front_cameras, 25),
        }

    @property
    def _back_camera_thresholds(
            self,
    ) -> Dict[BackCameraMatrix, float]:
        return {
            BackCameraMatrix.GOOD: np.percentile(self._back_cameras, 50),
            BackCameraMatrix.EXCELLENT: np.percentile(self._back_cameras, 75),
            BackCameraMatrix.IRRELEVANT: min(self._back_cameras),
        }

    @property
    def _battery_thresholds(
            self,
    ) -> Dict[BatteryCapacity, int]:
        return {
            BatteryCapacity.LARGE: np.percentile(self._battery_capacities, 75),
            BatteryCapacity.BIG: np.percentile(self._battery_capacities, 50),
            BatteryCapacity.OK: np.percentile(self._battery_capacities, 25),
        }

    @property
    def _display_diagonals_thresholds(
            self,
    ) -> Dict[DisplayDiagonal, float]:
        return {
            DisplayDiagonal.BIG: np.percentile(self._display_diagonals, 75),
            DisplayDiagonal.MEDIUM: np.percentile(self._display_diagonals, 50),
            DisplayDiagonal.SMALL: np.percentile(self._display_diagonals, 25),
        }

    @property
    def _display_height_thresholds(
            self,
    ) -> Dict[DisplayHeight, int]:
        return {
            DisplayHeight.BIG: np.percentile(self._display_heights, 75),
            DisplayHeight.MEDIUM: np.percentile(self._display_heights, 50),
            DisplayHeight.SMALL: np.percentile(self._display_heights, 25),
        }

    @property
    def _display_width_thresholds(
            self,
    ) -> Dict[DisplayWidth, int]:
        return {
            DisplayWidth.BIG: np.percentile(self._display_widths, 75),
            DisplayWidth.MEDIUM: np.percentile(self._display_widths, 50),
            DisplayWidth.SMALL: np.percentile(self._display_widths, 25),
        }

    @property
    def _cpu_n_cores_thresholds(
            self,
    ) -> Dict[CPUNCores, float]:
        return {
            CPUNCores.MANY: np.percentile(self._cpu_n_cores, 75),
            CPUNCores.MEDIUM_AMOUNT: np.percentile(self._cpu_n_cores, 50),
            CPUNCores.IRRELEVANT: np.percentile(self._cpu_n_cores, 25),
        }

    @property
    def _storage_thresholds(
            self,
    ) -> Dict[Storage, int]:
        return {
            Storage.HIGH: np.percentile(self._storages, 75),
            Storage.MEDIUM: np.percentile(self._storages, 50),
            Storage.LOW: np.percentile(self._storages, 25),
        }

    @property
    def _cpu_frequency_thresholds(
            self,
    ) -> Dict[CPUFrequency, int]:
        return {
            CPUFrequency.LOW: np.percentile(self._cpu_frequencies, 75),
            CPUFrequency.HIGH: np.percentile(self._cpu_frequencies, 25)
        }

    @property
    def _prices_thresholds(
            self,
    ) -> Dict[Price, int]:
        return {
            Price.CHEAP: np.percentile(self._prices, 75),
            Price.HIGH: np.percentile(self._prices, 25)
        }

    @staticmethod
    def _try_add(
            maybe_value: Optional[Any],
            mapping: Callable[[Any], Any],
            values_list: List[Any],
    ):
        if maybe_value:
            try:
                if maybe_value.startswith("[") and maybe_value.endswith("]"):
                    maybe_value = maybe_value[1:-1]
                    maybe_value_items = maybe_value.split(",")
                    for i in maybe_value_items:
                        values_list.append(mapping(i))
                else:
                    values_list.append(mapping(maybe_value))
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
