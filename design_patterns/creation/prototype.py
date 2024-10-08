"""
Prototypes are used to implement a copy operation - it creates a new object identical 
to the original, with the same state.

Python provides Prototype functionalily out of the box with "copy.copy()" 
and "copy.deepcopy()". If a class needs to define its own implementation of shallow or
deep copy, it should implement __copy__() or __deepcopy__() methods.

We'll impelemnt an explicit Prototype interface that always returns deep copies.
"""

from copy import deepcopy
from dataclasses import dataclass
from typing import Self


class Prototype:
    def clone(self) -> Self:
        return deepcopy(self)


@dataclass
class Rectangle(Prototype):
    width: int
    height: int


@dataclass
class Circle(Prototype):
    radius: int
