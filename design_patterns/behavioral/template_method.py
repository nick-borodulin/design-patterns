"""
Template method usually exists in a parent class (that can be abstract or not).
A template method defines an algorithm in terms of abstract interfaces, and 
child classes refefine parts of that algorithm.
The child classes might NEED to redefine some methods (which are abstract in the base class),
or they might CHOOSE to redefine base methods. The latter ones are usually called "hooks".

Naming conventions: Traditionally, methods that should be overridden have prefix "do",
according to MacApp framework for Macintosh applications.
"""

from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self) -> None:
        self._hook_result: int = 0
        self._do_work_result: int = 0

    def template_method(self) -> int:
        self._hook_result = self.hook()
        self._do_work_result = self.do_work()
        return self._hook_result + self._do_work_result

    @abstractmethod
    def do_work(self) -> int: ...

    def hook(self) -> int:
        return 0


class Derived(Base):
    def do_work(self) -> int:
        return 10

    def hook(self) -> int:
        return super().hook() + 2
