from contextlib import AbstractContextManager, nullcontext
import pytest
from design_patterns.behavioral.command import CompositeCommand, SimpleCommand, Receiver


def test_simple_command() -> None:
    command = SimpleCommand(Receiver())
    assert command.execute() == "receiver_action"


@pytest.mark.parametrize(
    "add_children,remove_children,exception_during_removal",
    [(1, 1, nullcontext()), (10, 10, nullcontext()), (1, 2, pytest.raises(IndexError))],
)
def test_composite_command(
    add_children: int,
    remove_children: int,
    exception_during_removal: AbstractContextManager,
) -> None:
    command = CompositeCommand()
    children = []
    for _ in range(add_children):
        new_child = SimpleCommand(Receiver())
        children.append(new_child)
        command.add_child(new_child)
    assert command.execute() == "receiver_action" * add_children

    assert len(children) == add_children

    with exception_during_removal:
        for _ in range(remove_children):
            command.remove_child(0)
