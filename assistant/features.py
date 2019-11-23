from enum import Enum


class UserRequirementBatteryLife(Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    IRRELEVANT = "irrelevant"


class UserRequirementCPUFrequency(Enum):
    HIGH = "high"
    LOW = "low"
