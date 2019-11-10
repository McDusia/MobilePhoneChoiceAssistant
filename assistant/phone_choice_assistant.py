from abc import ABC
from abc import abstractmethod
from typing import List

from assistant.features import BatteryLife

Model = str


class PhoneChoiceAssistant(ABC):
    @abstractmethod
    def suggest(self) -> List[Model]:
        ...

    @abstractmethod
    def battery_life(self, battery_life: BatteryLife):
        ...


class DummyPhoneChoiceAssistant(PhoneChoiceAssistant):

    def suggest(self) -> List[Model]:
        return ["Xiaomi Redmi 5A"]

    def battery_life(self, battery_life: BatteryLife):
        return battery_life.GOOD
