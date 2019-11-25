import click

from assistant.prolog.phone_choice_assistant import PrologPhoneChoiceAssistant
from assistant.repl import AssistantCmd


@click.group(invoke_without_command=True)
@click.option("--rules-file", type=click.Path(exists=True, dir_okay=False),
              help="File containing application logic",
              default="prolog_assistant/rules.pl")
@click.option("--knowledge-base-file", type=click.Path(exists=True, dir_okay=False),
              help="Knowledge base file with mobile phone specs",
              default="prolog_assistant/knowledge_base.pl")
@click.pass_context
def cli(
        ctx: click.Context,
        rules_file: str,
        knowledge_base_file: str,
):
    """
    Mobile phone choice assistant
    """
    if ctx.invoked_subcommand is not None:
        return

    assistant = PrologPhoneChoiceAssistant(rules_file, knowledge_base_file)
    repl = AssistantCmd(assistant)
    repl.cmdloop()
