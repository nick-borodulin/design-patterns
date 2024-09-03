from design_patterns.structural.adaptors.class_adaptor import DrawingApp as ClassAdaptorDrawingApp
from design_patterns.structural.adaptors.object_adaptor import DrawingApp as ObjectAdaptorDrawingApp

def test_class_adaptor():
    assert ClassAdaptorDrawingApp().draw() == "draw_line\nprint_text"

def test_object_adaptor():
    assert ObjectAdaptorDrawingApp().draw() == "draw_line\nprint_text"
