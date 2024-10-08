"""
Bridge is being used whenever we have 2 (or more) dimensions of the interface.
For example: in a text editor, windows can be categorized by their utility
(icons, text boxes) and platofrm implementations (Mac, Linux).
"""

from abc import ABC, abstractmethod


class WindowImplementation(ABC):
    @abstractmethod
    def draw_line(self) -> str: ...

    @abstractmethod
    def draw_text(self) -> str: ...


class Window:
    def __init__(self, implementation: WindowImplementation) -> None:
        self._imp: WindowImplementation = implementation

    def draw_text(self) -> str:
        return self._imp.draw_text()

    def draw_rectangle(self) -> str:
        return "".join([self._imp.draw_line() for line in range(4)])


class MacOSWindowImplementation(WindowImplementation):
    def draw_line(self) -> str:
        return "mac_os_draw_line"

    def draw_text(self) -> str:
        return "mac_os_draw_text"


class LinuxWindowImplementation(WindowImplementation):
    def draw_line(self) -> str:
        return "linux_draw_line"

    def draw_text(self) -> str:
        return "linux_draw_text"


class TextBox(Window):
    def draw(self) -> str:
        return self.draw_rectangle() + self.draw_text()


class IconWindow(Window):
    def draw(self) -> str:
        return self.draw_rectangle()
