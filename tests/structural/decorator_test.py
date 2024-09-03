from design_patterns.structural.decorator import BorderDecorator, ScrollableDecorator, TextBox

def test_raw_text_box() -> None:
    text_box = TextBox()
    assert text_box.draw() == "text_box_draw"

def test_text_box_with_border() -> None:
    text_box = BorderDecorator(component=TextBox(),
                               border_width=10)
    assert text_box.draw() == "text_box_draw" + "border_decorator_draw_border"

def text_text_box_with_scroll_bar_and_border() -> None:
    text_box = ScrollableDecorator(component=BorderDecorator(component=TextBox(),
                                                             border_width=5))
    assert text_box.draw() == "text_box_draw" + \
        "scrollable_decorator_add_scroll_bar" + \
        "border_decorator_draw_border"

