from typing import Any
from typing import Dict
from typing import Generator
from typing import Set
from pyswip import Prolog
from assistant.features import UserRequirementBatteryLife, UserRequirementCPUFrequency
from assistant.phone_choice_assistant_interface import Model
from assistant.phone_choice_assistant_interface import PhoneChoiceAssistant


RuleKey = str
Rule = str


class PrologPhoneChoiceAssistant(PhoneChoiceAssistant):
    _REQUIRE_TEMPLATE = "user_requirement({rule_key}, {value})"

    def __init__(self,
                 rules_file: str,
                 knowledge_base_file: str,
                 ):
        super().__init__()
        self._prolog = Prolog()
        self._load_knowledge_base(knowledge_base_file)
        self._load_rules(rules_file)
        self._loaded_rules: Dict[RuleKey, Rule] = dict()

    def _load_rules(self,
                    rules_file: str,
                    ):
        self._prolog.consult(rules_file)

    def _load_knowledge_base(self, knowledge_base_file: str, ):
        self._prolog.consult(knowledge_base_file)

    def suggest(self) -> Set[Model]:
        models: Generator[Dict[str, bytes], None, None] = self._prolog.query("model(Model)")
        models_list = [d["Model"].decode("utf-8") for d in models]
        return set(models_list)

    def battery_life(self, battery_life: UserRequirementBatteryLife):
        rule_key = "battery_life"
        self._require(rule_key, battery_life.name.lower())

    def cpu_frequency(self, cpu_frequency: UserRequirementCPUFrequency):
        rule_key = "cpu_frequency"
        self._require(rule_key, cpu_frequency.name.lower()) # ile użytkownik chce capacity

    def _require(self, rule_key: str, value: Any):
        previous_rule = self._loaded_rules.get(rule_key)
        if previous_rule:
            self._prolog.retract(previous_rule)

        new_rule = PrologPhoneChoiceAssistant._REQUIRE_TEMPLATE.format(
            rule_key=rule_key,
            value=value,
        )

        self._prolog.asserta(new_rule)
        self._loaded_rules[rule_key] = new_rule
