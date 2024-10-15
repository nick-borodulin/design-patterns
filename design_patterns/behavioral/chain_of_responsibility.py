"""
This example demonstrates Chain of Responsbility pattern where there is a chain (list) of objects,
and each of them tells the client if it's able to handle a request. If it is able to handle it, 
it does it, and if it cannot handle it, it forwards the request to its successor (usually, a parent object).
The request travels up the chain of responsibility until one of the objects in the chain handles it.
"""

from typing import Self, override

from design_patterns.creation.singleton import SingletonMetaClass


class NoHelpError(Exception):
    pass


class Topic(metaclass=SingletonMetaClass):
    @property
    def help_string(self) -> str:
        raise NotImplementedError()


class NoHelpTopic(Topic):
    @property
    @override
    def help_string(self) -> str:
        raise NoHelpError()


class PrintTopic(Topic):
    @property
    @override
    def help_string(self) -> str:
        return "Push the power button in your printer"


class ApplicationTopic(Topic):
    @property
    @override
    def help_string(self) -> str:
        return "This is a demo app"


class HelpHandler:
    def __init__(
        self, successor: Self | None = None, topic: Topic = NoHelpTopic()
    ) -> None:
        self._successor = successor
        self._topic = topic

    def has_help(self) -> bool:
        return type(self._topic) is not NoHelpTopic

    def get_help(self) -> str | None:
        if self.has_help():
            return self._topic.help_string
        if self._successor:
            return self._successor.get_help()
        return None
