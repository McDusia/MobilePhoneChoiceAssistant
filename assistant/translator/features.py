from enum import Enum


class BatteryCapacity(Enum):
    LARGE = "large"
    BIG = "big"
    OK = "ok"


class CPUFrequency(Enum):
    LOW = "low"
    HIGH = "high"
