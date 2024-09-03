from abc import abstractmethod, ABC

class VisualComponent(ABC):
    @abstractmethod
    def draw(self) -> str:
        ...

class TextBox(VisualComponent):
    def draw(self) -> str:
        return "text_box_draw"

class Decorator(VisualComponent):
    def __init__(self, component: VisualComponent) -> None:
        self._component = component
    
    def draw(self) -> str:
        return self._component.draw()
    
class BorderDecorator(Decorator):
    def __init__(self, component: VisualComponent, border_width: int) -> None:
        super().__init__(component)
        self._border_width = border_width

    def draw_border(self) -> str:
        return "border_decorator_draw_border"

    def draw(self) -> str:
        return super().draw() + self.draw_border()
    
class ScrollableDecorator(Decorator):
    def __init__(self, component: VisualComponent) -> None:
        super().__init__(component)

    def add_scroll_bar(self) -> str:
        return "scrollable_decorator_add_scroll_bar"
    
    def draw(self) -> str:
        return super().draw() + self.add_scroll_bar()

