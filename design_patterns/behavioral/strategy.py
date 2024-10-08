"""
The main idea - define an interface for a family of algorithms and
"bring data into the algorithm", i.e. pass a predetermined dataset (as a parameters)
into the interface.
"""

from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")


class Strategy(ABC):
    """
    Our Strategy interface is going to be working with lists.
    """

    @abstractmethod
    def act_on_list(self, data: list[T], /, *args, **kwargs) -> list[T]: ...


class RemoveTail(Strategy):
    def act_on_list(self, data: list[T], /, *args, **kwargs) -> list[T]:
        if not data:
            return []
        data.pop()
        return data


class RemoveHead(Strategy):
    def act_on_list(self, data: list[T], /, *args, **kwargs) -> list[T]:
        if not data:
            return []
        data.pop(0)
        return data


class Context:
    def __init__(self, list_algorithm: Strategy) -> None:
        self._list_algorithm = list_algorithm

    def business_logic(self, input_list: list[T]) -> list[T]:
        return self._list_algorithm.act_on_list(input_list)
