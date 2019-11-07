from assistant.phone_choice_assistant import DummyPhoneChoiceAssistant
from assistant.repl import AssistantCmd


def main():
    assistant = DummyPhoneChoiceAssistant()
    repl = AssistantCmd(assistant)
    repl.cmdloop()


if __name__ == '__main__':
    main()
