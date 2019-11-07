from assistant.prolog.prolog_phone_choice_assistant import PrologPhoneChoiceAssistant
from assistant.repl import AssistantCmd


def main(
        rules_file: str,
        knowledge_base_file: str,
):
    assistant = PrologPhoneChoiceAssistant(rules_file, knowledge_base_file)
    repl = AssistantCmd(assistant)
    repl.cmdloop()


if __name__ == '__main__':
    rules_file = "prolog_assistant/rules.pl"
    knowledge_base_file = "prolog_assistant/knowledge_base.pl"
    main(rules_file, knowledge_base_file)
