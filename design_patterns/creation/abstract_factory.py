from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def climb_through(self) -> str:
        ...

class Wall(ABC):
    @abstractmethod
    def build(self) -> str:
        ...

class Factory(ABC):
    @abstractmethod
    def create_window(self) -> Window:
        ...

    @abstractmethod
    def create_wall(self) -> Wall:
        ...

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
