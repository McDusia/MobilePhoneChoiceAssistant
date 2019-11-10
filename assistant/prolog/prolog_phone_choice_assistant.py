from typing import Dict
from typing import Generator
from typing import List

from pyswip import Prolog

from assistant.features import BatteryLife
from assistant.phone_choice_assistant import Model
from assistant.phone_choice_assistant import PhoneChoiceAssistant


RuleKey = str
Rule = str


class PrologPhoneChoiceAssistant(PhoneChoiceAssistant):

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

    def suggest(self) -> List[Model]:
        models: Generator[Dict[str, bytes], None, None] = self._prolog.query("model(Model)")
        return [d["Model"].decode("utf-8")
                for d in models]

    def battery_life(self, battery_life: BatteryLife):
        rule_key = "battery_life"

        previous_rule = self._loaded_rules.get(rule_key)
        if previous_rule:
            self._prolog.retract(previous_rule)

        new_rule = f"required(battery_capacity, {battery_life.name.lower()})"
        self._prolog.asserta(new_rule)
        self._loaded_rules[rule_key] = new_rule

    def _load_knowledge_base(self,
                             knowledge_base_file: str,
                             ):
        self._prolog.consult(knowledge_base_file)
