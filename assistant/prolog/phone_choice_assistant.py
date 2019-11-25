from typing import Any
from typing import Dict
from typing import Generator
from typing import Set
from pyswip import Prolog
from assistant.features import BatteryLife, CPUFrequency, FrontCameraMatrix, \
    BackCameraMatrix, CpuNCores
from assistant.phone_choice_assistant_interface import Model
from assistant.phone_choice_assistant_interface import PhoneChoiceAssistant


RuleKey = str
Rule = str
RequiredFeature_String = "yes"


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
        models: Generator[Dict[str, bytes], None, None] = self._prolog.query("is_sufficient(Model)")
        models_list = [d["Model"].decode("utf-8") for d in models]
        return set(models_list)

    def battery_life(self, battery_life: BatteryLife):
        rule_key = "battery_life"
        self._require(rule_key, battery_life.name.lower())

    def cpu_frequency(self, cpu_frequency: CPUFrequency):
        rule_key = "cpu_frequency"
        self._require(rule_key, cpu_frequency.name.lower())

    def touch_screen(self):
        rule_key = "touch_screen"
        self._require(rule_key, RequiredFeature_String)

    def nfc(self):
        rule_key = "nfc"
        self._require(rule_key,RequiredFeature_String)

    def water_resistant(self):
        rule_key = "touch_screen"
        self._require(rule_key, RequiredFeature_String)

    def dual_sim(self):
        rule_key = "dual_sim"
        self._require(rule_key, RequiredFeature_String)

    def cpu_n_cores(self, cpu_n_cores: CpuNCores):
        rule_key = "cpu_n_cores"
        self._require(rule_key, cpu_n_cores.name.lower())

    def back_camera_matrix(self, back_camera_matrix: BackCameraMatrix):
        rule_key = "back_camera_matrix"
        self._require(rule_key, back_camera_matrix.name.lower())

    def front_camera_matrix(self, front_camera_matrix: FrontCameraMatrix):
        rule_key = "front_camera_matrix"
        self._require(rule_key, front_camera_matrix.name.lower())

    def phone_for_business(self):
        rule_key = "phone_for_business"
        self._require(rule_key, RequiredFeature_String)

    def big_screen(self):
        rule_key = "big_screen"
        self._require(rule_key, RequiredFeature_String)

    def very_big_screen(self):
        rule_key = "very_big_screen"
        self._require(rule_key, RequiredFeature_String)

    def phone_for_teenager(self):
        rule_key = "phone_for_teenager"
        self._require(rule_key, RequiredFeature_String)

    def phone_to_listening_music(self):
        rule_key = "phone_to_listening_music"
        self._require(rule_key, RequiredFeature_String)

    def phone_for_social_media(self):
        rule_key = "phone_for_social_media"
        self._require(rule_key, RequiredFeature_String)

    def phone_to_play_games(self):
        rule_key = "phone_to_play_games"
        self._require(rule_key, RequiredFeature_String)

    def phone_to_make_photos(self):
        rule_key = "phone_to_make_photos"
        self._require(rule_key, RequiredFeature_String)

    def phone_for_trips(self):
        rule_key = "phone_for_trips"
        self._require(rule_key, RequiredFeature_String)

    def _require(self, rule_key: str, value: Any):
        previous_rule = self._loaded_rules.get(rule_key)
        if previous_rule:
            self._prolog.retract(previous_rule)

        new_rule = PrologPhoneChoiceAssistant._REQUIRE_TEMPLATE.format(
            rule_key=rule_key,
            value=value,
        )
        print(new_rule)
        self._prolog.asserta(new_rule)
        self._loaded_rules[rule_key] = new_rule

    def clear_requirements(self):
