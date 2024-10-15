"""
Abstract Factory pattern is an extension of Factory Method. The latter is used when we need to
construct just one object based on a set of inputs, whereas Abstract Factory is used when we need to
build interrelated objects.
For example, below, we have 2 factories,
1) RoundWindowsBrickWalls, builds round windows and brich walls,
2) SquareWindowsWoodenWalls, builds square windows and wooden walls.
In this example, it is important that a certain type of windows only being built with certain type of walls,
so we are using an Abstract Factory pattern and not Factory Method.
"""

from abc import ABC, abstractmethod


class Window(ABC):
    @abstractmethod
    def climb_through(self) -> str: ...


class Wall(ABC):
    @abstractmethod
    def build(self) -> str: ...


class Factory(ABC):
    @abstractmethod
    def create_window(self) -> Window: ...

    @abstractmethod
    def create_wall(self) -> Wall: ...


class RoundWindow(Window):
    def climb_through(self):
        return "climb_round_window"


class SquareWindow(Window):
    def climb_through(self):
        return "climb_square_window"


class BrickWall(Wall):
    def build(self) -> str:
        return "build_brick_wall"


class WoodenWall(Wall):
    def build(self) -> str:
        return "build_wooden_wall"


class RoundWindowsBrickWalls(Factory):
    def create_window(self) -> Window:
        return RoundWindow()

    def create_wall(self) -> Wall:
        return BrickWall()


class SquareWindowsWoodenWalls(Factory):
    def create_window(self) -> Window:
        return SquareWindow()

    def create_wall(self) -> Wall:
        return WoodenWall()
