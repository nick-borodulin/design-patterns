"""
Uses composition instead of inheritance (opposed to class apators).
The client will need to explicitly redefine all the methods of the Adaptee in the Adaptor
that it wants to use.
"""
from abc import abstractmethod, ABC

class ExternalTextLibrary:
    def print_text(self, text) -> str:
        return text

class Primitive(ABC):
    @abstractmethod
    def draw(self) -> str:
        ...

class Line(Primitive):
    def draw(self) -> str:
        return "draw_line"
    
class Text(Primitive):
    def __init__(self) -> None:
        self._text_library = ExternalTextLibrary()

    def draw(self) -> str:
        return self._text_library.print_text("print_text")

class DrawingApp:
    def draw(self) -> str:
        return Line().draw() + "\n" + Text().draw()