from abc import ABC
from abc import abstractmethod
from typing import List

from assistant.features import BatteryLife, CPUFrequency

Model = str


class PhoneChoiceAssistant(ABC):
    @abstractmethod
    def suggest(self) -> List[Model]:
        ...

    @abstractmethod
    def battery_life(self, battery_life: BatteryLife):
        ...

    @abstractmethod
    def cpu_frequency(self, cpu_frequency: CPUFrequency):
        ...


class DummyPhoneChoiceAssistant(PhoneChoiceAssistant):

    def suggest(self) -> List[Model]:
        return ["Xiaomi Redmi 5A"]

    def battery_life(self, battery_life: BatteryLife):
        return battery_life.GOOD

    def cpu_frequency(self, cpu_frequency: CPUFrequency):
        return cpu_frequency.LOW
