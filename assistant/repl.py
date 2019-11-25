import cmd
from typing import TextIO, List, Any

from assistant.phone_choice_assistant_interface import BatteryLife, CPUFrequency, CpuNCores, FrontCameraMatrix, BackCameraMatrix
from assistant.phone_choice_assistant_interface import PhoneChoiceAssistant


class AssistantCmd(cmd.Cmd):

    def __init__(self,
                 phone_choice_assistant: PhoneChoiceAssistant,
                 completekey: str = 'tab',
                 stdin: TextIO = None,
                 stdout: TextIO = None,
                 ):
        super().__init__(completekey, stdin, stdout)
        self._phone_choice_assistant = phone_choice_assistant
        self._command_parser = CommandParser()

    intro = "Type help or ? to list commands."
    prompt = "> "

    def do_suggest(self, arg: str):
        """Finds best mobile phones matching given criteria."""
        suggested_models = self._phone_choice_assistant.suggest()
        if suggested_models:
            self._print("Suggested models:")
            self._print("\n".join(f" - {model}" for model in suggested_models))
        else:
            self._print("No known model meets your requirements")

    def do_EOF(self, _arg: str):
        return True

# TODO: all these methods looks the same...

    def do_battery_life(self, arg: str):
        """Sets requirement for battery life.
Either good or irrelevant."""
        try:
            battery_life = self._command_parser.parse_battery_life(arg)
            self._phone_choice_assistant.battery_life(battery_life)
        except ValueError:
            self._print("ERROR! Battery life can be either good or irrelevant or excellent")

    @staticmethod
    def complete_battery_life(prefix: str, *_args) -> List[str]:
        names = (v.name.lower() for v in BatteryLife)
        return [name
                for name in names
                if name.startswith(prefix.lower())]

    def do_cpu_frequency(self, arg: str):
        """Sets requirement for CPU frequency.
        Either high or low"""
        try:
            cpu_frequency = self._command_parser.parse_cpu_frequency(arg) # bierze jaka jest wartość
            self._phone_choice_assistant.cpu_frequency(cpu_frequency) # ustawia to jako pole
        except ValueError:
            self._print("CPU frequency can be high or low")

    @staticmethod
    def complete_cpu_frequency(prefix: str, *_args) -> List[str]:
        names = (v.name.lower() for v in CPUFrequency)
        return [name
                for name in names
                if name.startswith(prefix.lower())]

    def do_nfc(self, arg: str):
        """Sets requirement for NFC
        No arguments required"""
        self._phone_choice_assistant.nfc()

    def do_water_resistant(self, arg: str):
        """Sets requirement for water resistance
        No arguments required"""
        self._phone_choice_assistant.water_resistant()

    def do_dual_sim(self, arg: str):
        """Sets requirement for dual_sim
        No arguments required"""
        self._phone_choice_assistant.dual_sim()

    def do_touch_screen(self, arg: str):
        """Sets requirement for touch_screen
        No arguments required"""
        self._phone_choice_assistant.touch_screen()

    def do_cpu_n_cores(self, arg: str):
            """Sets requirement for cpu_n_cores
            Either many, medium_amount or irrelevant."""
            try:
                cpu_n_cores = self._command_parser.parse_cpu_n_cores(arg)
                self._phone_choice_assistant.cpu_n_cores(cpu_n_cores)
            except ValueError:
                self._print("ERROR! Number of cpu can be either many or medium_amount or irrelevant")

    @staticmethod
    def complete_cpu_n_cores(prefix: str, *_args) -> List[str]:
            names = (v.name.lower() for v in CpuNCores)
            return [name
                    for name in names
                    if name.startswith(prefix.lower())]

    def do_back_camera_matrix(self, arg: str):
            """Sets requirement for back camera matrix
            Either excellent, good or irrelevant."""
            try:
                back_camera_matrix = self._command_parser.parse_back_camera_matrix(arg)
                self._phone_choice_assistant.back_camera_matrix(back_camera_matrix)
            except ValueError:
                self._print("ERROR! Back camera matrix can be either excellent, good or irrelevant")

    @staticmethod
    def complete_back_camera_matrix(prefix: str, *_args) -> List[str]:
            names = (v.name.lower() for v in BackCameraMatrix)
            return [name
                    for name in names
                    if name.startswith(prefix.lower())]

    def do_front_camera_matrix(self, arg: str):
            """Sets requirement for front camera matrix
            Either excellent, good or irrelevant."""
            try:
                front_camera_matrix = self._command_parser.parse_front_camera_matrix(arg)
                self._phone_choice_assistant.front_camera_matrix(front_camera_matrix)
            except ValueError:
                self._print("ERROR! Front camera matrix can be either excellent, good or irrelevant")

    @staticmethod
    def complete_front_camera_matrix(prefix: str, *_args) -> List[str]:
            names = (v.name.lower() for v in FrontCameraMatrix)
            return [name
                    for name in names
                    if name.startswith(prefix.lower())]

    def do_phone_for_business(self, arg: str):
            """Sets requirement: phone for business
            No arguments required """
            self._phone_choice_assistant.phone_for_business()

    def do_big_screen(self, arg: str):
            """Sets requirement: big screen
            No arguments required """
            self._phone_choice_assistant.big_screen()

    def do_very_big_screen(self, arg: str):
            """Sets requirement: very big screen
            No arguments required """
            self._phone_choice_assistant.very_big_screen()

    def do_phone_for_teenager(self, arg: str):
            """Sets requirement: phone for teenager
            No arguments required """
            self._phone_choice_assistant.phone_for_teenager()

    def do_phone_to_listening_music(self, arg: str):
            """Sets requirement: phone to listenning music
            No arguments required """
            self._phone_choice_assistant.phone_to_listening_music()

    def do_phone_for_social_media(self, arg: str):
            """Sets requirement: phone for social media
            No arguments required """
            self._phone_choice_assistant.phone_for_social_media()

    def do_phone_to_play_games(self, arg: str):
            """Sets requirement: phone to play games
            No arguments required """
            self._phone_choice_assistant.phone_to_play_games()

    def do_phone_to_make_photos(self, arg: str):
            """Sets requirement: phone to make photos
            No arguments required """
            self._phone_choice_assistant.phone_to_make_photos()

    def _print(self, *args, **kwargs):
        kwargs["file"] = self.stdout
        print(*args, **kwargs)


class CommandParser:

    @staticmethod
    def parse_feature(input_str: str, feature_object: Any) -> Any:
        return feature_object.__class__.__name__(input_str.lower())

    @staticmethod
    def parse_battery_life(input_str: str) -> BatteryLife:
        return BatteryLife(input_str.lower())

    @staticmethod
    def parse_cpu_frequency(input_str: str) -> CPUFrequency:
        return CPUFrequency(input_str.lower())

    @staticmethod
    def parse_cpu_n_cores(input_str: str) -> CpuNCores:
        return CpuNCores(input_str.lower())

    @staticmethod
    def parse_back_camera_matrix(input_str: str) -> BackCameraMatrix:
        return BackCameraMatrix(input_str.lower())

    @staticmethod
    def parse_front_camera_matrix(input_str: str) -> FrontCameraMatrix:
        return FrontCameraMatrix(input_str.lower())
