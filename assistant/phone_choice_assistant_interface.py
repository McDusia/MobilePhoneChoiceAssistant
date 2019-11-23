from abc import ABC
from abc import abstractmethod
from typing import Set

from assistant.features import UserRequirementBatteryLife, UserRequirementCPUFrequency

Model = str


class PhoneChoiceAssistant(ABC):
    @abstractmethod
    def suggest(self) -> Set[Model]:
        ...

    @abstractmethod
    def battery_life(self, battery_life: UserRequirementBatteryLife):
        ...

    @abstractmethod
    def cpu_frequency(self, cpu_frequency: UserRequirementCPUFrequency):
        ...


#class DummyPhoneChoiceAssistant(PhoneChoiceAssistant):
#
#    def suggest(self) -> List[Model]:
#        return ["Xiaomi Redmi 5A"]#

    #def battery_life(self, battery_life: BatteryLife):
    #    return battery_life.GOOD

    #def cpu_frequency(self, cpu_frequency: CPUFrequency):
    #    return cpu_frequency.LOW
