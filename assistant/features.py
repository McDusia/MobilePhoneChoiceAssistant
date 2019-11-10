from enum import Enum


class BatteryLife(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    IRRELEVANT = "irrelevant"


class CpuFrequency(Enum):
    LOW = "low"
    HIGH = "high"
