
from abc import ABC, abstractmethod
from typing import override


class Widget:
    def __init__(self, mediator: "Mediator") -> None:
        self._mediator = mediator

    def changed(self) -> None:
        self._mediator.widget_changed(self)
        
class Mediator(ABC):
    @abstractmethod
    def widget_changed(self, widget: Widget) -> None: ...

class DialogMediator(Mediator):
    def __init__(self) -> None:
        self._okay_button = Button(text="Ok", enabled=False, mediator=self)
        self._cancel_button = Button(text="Cancel", enabled=False, mediator=self)
        self._text_box = TextBox(self)

    @property
    def okay_button(self) -> "Button":
        return self._okay_button
    
    @property
    def cancel_button(self) -> "Button":
        return self._cancel_button
    
    @property
    def text_box(self) -> "TextBox":
        return self._text_box
    
    @override
    def widget_changed(self, widget: Widget) -> None:
        if widget is self._text_box:
            self._okay_button.enabled = self._cancel_button.enabled = (self._text_box.text != "")
        # Other logic based on the the state of the 3 components

class Button(Widget):
    def __init__(self,
                 text: str,
                 enabled: bool,
                 mediator: Mediator,
                 ) -> None:
        super().__init__(mediator)
        self._text: str = text  # The text displayed on the button
        self._enabled = enabled

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, new_state) -> None:
        self._enabled = new_state

    def clicked(self) -> None:
        self.changed()

class TextBox(Widget):
    def __init__(self,
                 mediator: Mediator,
                 ) -> None:
        super().__init__(mediator)
        self._text: str = ""

    @property
    def text(self) -> str:
        return self._text
    
    @text.setter
    def text(self, new_text) -> None:
        self._text = new_text
        self.changed()
    