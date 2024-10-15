"""
Composite pattern is used when there's a need to perform a certain action either on a single object
or on a container. 
"""

from typing import Self


class InvalidLeafError(Exception):
    pass


class Component:
    def operation(self) -> str:
        return str()

    def add_child(self, child: Self) -> None:
        pass

    def remove_child(self, child: Self) -> None:
        pass


class Leaf(Component):
    def operation(self) -> str:
        return "child_operation"


class Composite(Component):
    def __init__(self) -> None:
        self._children: list[Component] = []

    def add_child(self, child: Component) -> None:
        self._children.append(child)

    def remove_child(self, child: Component) -> None:
        try:
            chlid_index = self._children.index(child)
        except ValueError as child_not_found:
            raise InvalidLeafError from child_not_found
        self._children.pop(chlid_index)

    def operation(self) -> str:
        child_operations = "composite_operation"
        for child in self._children:
            child_operations += child.operation()
        return child_operations
