from design_patterns.behavioral.chain_of_responsibility import (
    HelpHandler,
    NoHelpTopic,
    PrintTopic,
    ApplicationTopic
)

def test_chain_of_respobsibility() -> None:
    application = HelpHandler(successor=None, topic=ApplicationTopic())
    dialog = HelpHandler(successor=application, topic=PrintTopic())
    button = HelpHandler(successor=dialog, topic=NoHelpTopic())

    assert button.get_help() == PrintTopic().help_string
    assert dialog.get_help() == PrintTopic().help_string
    assert application.get_help() == ApplicationTopic().help_string
