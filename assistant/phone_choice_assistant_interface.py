from abc import ABC
from abc import abstractmethod
from typing import Set

from assistant.features import BatteryLife, CPUFrequency


from assistant.features import BatteryLife, CPUFrequency, BackCameraMatrix, \
    FrontCameraMatrix, CpuNCores

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
    def battery_life(self, battery_life: BatteryLife):
        ...

    @abstractmethod
    def cpu_frequency(self, cpu_frequency: CPUFrequency):
        ...

    @abstractmethod
    def touch_screen(self):
        ...

    @abstractmethod
    def nfc(self):
        ...

    @abstractmethod
    def water_resistant(self):
        ...

    @abstractmethod
    def dual_sim(self):
        ...

    @abstractmethod
    def cpu_n_cores(self, cpu_n_cores: CpuNCores):
        ...

    @abstractmethod
    def back_camera_matrix(self, back_camera_matrix: BackCameraMatrix):
        ...

    @abstractmethod
    def front_camera_matrix(self, front_camera_matrix: FrontCameraMatrix):
        ...

    @abstractmethod
    def phone_for_business(self):
        ...
