"""
The idea is to implement state machine using a set of classes, each
of which represents one state. Each class is a singleton. A "state" interface
defines a method that passes control to the next state.
"""

from typing import override


class IncorrectStateError(ValueError):
    pass


class State:
    def __init__(self, context: "Context") -> None:
        self._context = context

    def initialize(self) -> None:
        raise IncorrectStateError

    def open(self) -> None:
        raise IncorrectStateError

    def close(self) -> None:
        raise IncorrectStateError

    def change_state(self, new_state: "State") -> None:
        self._context.state = new_state


class Init(State):
    @override
    def initialize(self) -> None:
        # Do work
        self.change_state(new_state=Open(context=self._context))


class Open(State):
    @override
    def open(self) -> None:
        # Do work
        self.change_state(new_state=Close(context=self._context))


class Close(State):
    @override
    def close(self) -> None:
        # Do work
        # Not changing the state
        pass


class Context:
    def __init__(self) -> None:
        self._state = Init(context=self)

    @property
    def state(self) -> State:
        return self._state

    @state.setter
    def state(self, new_state: State) -> None:
        self._state = new_state

    def initialize(self) -> None:
        self.state.initialize()

    def open(self) -> None:
        self.state.open()

    def close(self) -> None:
        self.state.close()
