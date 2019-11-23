from abc import ABC
from abc import abstractmethod
from typing import Set

from assistant.features import BatteryLife, CPUFrequency, TouchScreen, DualSim, WaterResistance, NFC
Model = str


class PhoneChoiceAssistant(ABC):
    @abstractmethod
    def suggest(self) -> Set[Model]:
        ...

    @abstractmethod
    def battery_life(self, battery_life: BatteryLife):
        ...

    @abstractmethod
    def cpu_frequency(self, cpu_frequency: CPUFrequency):
        ...

    @abstractmethod
    def touch_screen(self, touch_screen: TouchScreen):
        ...

    @abstractmethod
    def nfc(self, nfc: NFC):
        ...

    @abstractmethod
    def water_resistant(self, water_resistant: WaterResistance):
        ...

    @abstractmethod
    def dual_sim(self, dual_sim: DualSim):
        ...

#class DummyPhoneChoiceAssistant(PhoneChoiceAssistant):
#
#    def suggest(self) -> List[Model]:
#        return ["Xiaomi Redmi 5A"]#

    #def battery_life(self, battery_life: BatteryLife):
    #    return battery_life.GOOD

    #def cpu_frequency(self, cpu_frequency: CPUFrequency):
    #    return cpu_frequency.LOW
