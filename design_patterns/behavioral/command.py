"""
This example combines Command, a behavioral pattern and Composite, a structural pattern.
Command pattern consits of command interface, one or more concrete command implementations.
Each of them can be have a single Receiver (SimpleCommand, below) or multiple receivers (CompositeCommand).
Receiver is an object that Command acts upon.
"""

from typing import Any, Self
from abc import abstractmethod, ABC


class Command(ABC):
    """Command pattern"""

    @abstractmethod
    def execute(self) -> Any: ...


class Component:
    """Composite pattern"""

    def add_child(self, child: Self) -> None:
        pass

    def remove_child(self, child_index: int) -> None:
        pass


class Receiver:
    """Command receiver"""

    def action(self) -> str:
        return "receiver_action"


class SimpleCommand(Command, Component):

    def __init__(self, receiver: Receiver) -> None:
        self._receiver = receiver

    def execute(self) -> str:
        return self._receiver.action()


class CompositeCommand(Command, Component):
    def __init__(self) -> None:
        self._children: list[Any] = []

    def add_child(self, child: Component) -> None:
        self._children.append(child)

    def remove_child(self, child_index: int) -> None:
        self._children.pop(child_index)

    def execute(self) -> Any:
        return "".join([child.execute() for child in self._children])
