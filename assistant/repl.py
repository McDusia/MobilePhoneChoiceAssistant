import cmd
from typing import TextIO, List

from assistant.phone_choice_assistant import BatteryLife
from assistant.phone_choice_assistant import PhoneChoiceAssistant


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

    def do_battery_life(self, arg: str):
        """Sets requirement for battery life.
Either good or irrelevant."""
        try:
            battery_life = self._command_parser.parse_battery_life(arg)
            self._phone_choice_assistant.battery_life(battery_life)
        except ValueError:
            self._print("ERROR! Battery life can be either good or irrelevant")

    @staticmethod
    def complete_battery_life(prefix: str, *_args) -> List[str]:
        names = (v.name.lower() for v in BatteryLife)
        return [name
                for name in names
                if name.startswith(prefix.lower())]

    def _print(self, *args, **kwargs):
        kwargs["file"] = self.stdout
        print(*args, **kwargs)


class CommandParser:
    @staticmethod
    def parse_battery_life(input_str: str) -> BatteryLife:
        return BatteryLife(input_str.lower())
