from design_patterns.creation.prototype import Circle, Rectangle

def test_correct_circle_deepcopy() -> None:
    circle = Circle(5)
    copy = circle.clone()
    assert circle.radius == copy.radius
    assert circle == copy
    circle.radius = 6
    assert circle.radius != copy.radius
    assert circle != copy

def test_correct_rectange_deepcopy() -> None:
    rectangle = Rectangle(height=1, width=2)
    copy = rectangle.clone()
    assert rectangle.height == copy.height and rectangle.width == copy.width
    assert rectangle == copy
    copy.width = 3
    copy.height = 4
    assert rectangle.height != copy.height and rectangle.width != copy.width
    assert rectangle != copy
    