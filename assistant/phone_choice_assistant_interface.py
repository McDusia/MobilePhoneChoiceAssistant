from abc import ABC
from abc import abstractmethod
from typing import Set

from assistant.features import BatteryLife, CPUFrequency, TouchScreen, DualSim, WaterResistance, NFC, BackCameraMatrix, \
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

    @abstractmethod
    def cpu_n_cores(self, cpu_n_cores: CpuNCores):
        ...

    @abstractmethod
    def back_camera_matrix(self, back_camera_matrix: BackCameraMatrix):
        ...

    @abstractmethod
    def front_camera_matrix(self, front_camera_matrix: FrontCameraMatrix):
        ...
