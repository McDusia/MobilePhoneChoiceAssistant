from enum import Enum


class BatteryCapacity(Enum):
    LARGE = "large"
    BIG = "big"
    OK = "ok"


class CpuFrequency(Enum):
    LOW = "low"
    HIGH = "high"
