"""
There are 3 parties: Memento, Originator and Caretaker. Caretaker is responsible to storing Mementos.
Memento has 2 interfaces: public and private. Public interface is used by Caretaker, while the private
one is used by Originator to set and read its private state. Python does not provide support for
private/public interfaces (whereas in C++ it is possible by making Originator a "friend" of Memento
and gaining access to its private data). One way to get around this limitation is to define the public
Memento interface in a base class, and the private one in a implementation class.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from dataclasses import dataclass
from random import randint
from typing import Any


class Memento(ABC):
    def __init__(self, name: str) -> None:
        self._creation_timestamp = datetime.now()
        self._name = name

    @property
    def creation_timestamp(self) -> datetime:
        return self._creation_timestamp

    @property
    def name(self) -> str:
        return self._name

    @property
    @abstractmethod
    def state(self) -> Any: ...


@dataclass
class Coordinates:
    x: int
    y: int
    z: int

    @classmethod
    def create_random_coordinates(cls) -> "Coordinates":
        min = 0
        max = 1000
        return Coordinates(
            x=randint(min, max), y=randint(min, max), z=randint(min, max)
        )


class CoordinateMemento(Memento):
    def __init__(self, name: str, state: Coordinates) -> None:
        super().__init__(name=name)
        self._state = state

    @property
    def state(self) -> Coordinates:
        return self._state


class Originator:
    def __init__(self) -> None:
        self._state: Coordinates = Coordinates.create_random_coordinates()

    @property
    def state(self) -> Coordinates:
        return self._state

    def do_work(self) -> None:
        self._state = Coordinates.create_random_coordinates()

    def save(self) -> Memento:
        return CoordinateMemento(name=__class__.__name__, state=self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.state


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._history: list[Memento] = []

    @property
    def history(self) -> list[Memento]:
        return self._history

    def backup(self) -> None:
        self._history.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._history):
            return

        memento = self._history.pop()
        self._originator.restore(memento=memento)
