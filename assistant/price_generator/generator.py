import zlib
from typing import Dict

from assistant.price_generator.collections import defaultdict


class PriceGenerator:

    _MIN_BASE_PRICE = 100
    _MAX_BASE_PRICE = 2000

    def __init__(self):
        self._base_prices = defaultdict(self.__base_price_for)

    def price_for(
            self,
            row: Dict[str, str],
    ) -> float:
        make = row["model"].split(maxsplit=1)[0]
        base_price = self._base_prices[make]
        return (base_price
                + self._cpu_price(row)
                + self._memory_price(row)
                + self._camera_price(row))

    @staticmethod
    def __base_price_for(make: str) -> float:
        return (zlib.adler32(make.encode("utf-8"))
                % (PriceGenerator._MAX_BASE_PRICE - PriceGenerator._MIN_BASE_PRICE)
                + PriceGenerator._MIN_BASE_PRICE)

    @staticmethod
    def _cpu_price(row: Dict[str, str]) -> float:
        try:
            return int(row["cpu_n_cores"]) * int(row["cpu_frequency"]) / 100
        except ValueError:
            return 5

    @staticmethod
    def _memory_price(row: Dict[str, str]) -> float:
        try:
            return sum(ord(c) for c in row["memory"]) / 5
        except ValueError:
            return 5

    @staticmethod
    def _camera_price(row: Dict[str, str]) -> float:
        try:
            return (sum(ord(c) for c in row["front_camera_matrix"])
                    + sum(ord(c) for c in row["back_camera_matrix"])) / 5
        except ValueError:
            return 5
