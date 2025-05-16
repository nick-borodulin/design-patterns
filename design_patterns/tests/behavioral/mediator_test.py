from design_patterns.behavioral.mediator import DialogMediator


def test_dialog() -> None:
    dialog = DialogMediator()
    assert not dialog.okay_button.enabled
    assert not dialog.cancel_button.enabled
    assert dialog.text_box.text == ""

    dialog.text_box.text = "User input"
    assert dialog.okay_button.enabled
    assert dialog.cancel_button.enabled

    dialog.text_box.text = ""
    assert not dialog.okay_button.enabled
    assert not dialog.cancel_button.enabled
