
from design_patterns.creation.abstract_factory import (
    RoundWindowsBrickWalls,
    SquareWindowsWoodenWalls,
)

def test_creation_of_round_windows_brick_walls():
    factory = RoundWindowsBrickWalls()
    window = factory.create_window()
    wall = factory.create_wall()

    assert window.climb_through() == "climb_round_window"
    assert wall.build() == "build_brick_wall"

def test_creation_of_square_windows_wooden_walls():
    factory = SquareWindowsWoodenWalls()
    window = factory.create_window()
    wall = factory.create_wall()

    assert window.climb_through() == "climb_square_window"
    assert wall.build() == "build_wooden_wall"
