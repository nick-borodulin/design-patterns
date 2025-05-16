from design_patterns.behavioral.state import (
    Context,
    Close,
    IncorrectStateError,
    Init,
    Open,
)
import pytest


def test_correct_state_transitions() -> None:
    context = Context()
    assert type(context.state) is Init
    context.initialize()
    assert type(context.state) is Open
    context.open()
    assert type(context.state) is Close
    context.close()
    assert type(context.state) is Close  # Close doesn't change into anything else.


def test_incorrect_state_transitions_in_init_state() -> None:
    context = Context()
    assert type(context.state) is Init
    with pytest.raises(IncorrectStateError):
        context.open()
    with pytest.raises(IncorrectStateError):
        context.close()


def test_incorrect_state_transitions_in_open_state() -> None:
    context = Context()
    assert type(context.state) is Init
    context.initialize()
    assert type(context.state) is Open
    with pytest.raises(IncorrectStateError):
        context.initialize()
    with pytest.raises(IncorrectStateError):
        context.close()


def test_incorrect_state_transitions_in_closed_state() -> None:
    context = Context()
    assert type(context.state) is Init
    context.initialize()
    assert type(context.state) is Open
    context.open()
    assert type(context.state) is Close
    context.close()
    assert type(context.state) is Close
    with pytest.raises(IncorrectStateError):
        context.initialize()
    with pytest.raises(IncorrectStateError):
        context.open()
