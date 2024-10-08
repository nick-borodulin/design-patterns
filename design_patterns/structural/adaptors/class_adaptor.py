"""
Use class adaptors when you want to override one or more methods of the Adaptee.
Allows not to have a separate Adaptee object in the Adaptor class.
"""

from abc import abstractmethod, ABC


class ExternalTextLibrary:
    def print_text(self, text) -> str:
        return text


class Primitive(ABC):
    @abstractmethod
    def draw(self) -> str: ...


class Line(Primitive):
    def draw(self) -> str:
        return "draw_line"


class Text(Primitive, ExternalTextLibrary):
    def draw(self) -> str:
        return self.print_text("print_text")


class DrawingApp:
    def draw(self) -> str:
        return Line().draw() + "\n" + Text().draw()
