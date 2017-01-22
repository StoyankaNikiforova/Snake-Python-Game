from class_world_object import WorldObject
from class_vector2D import Vector2D
from settings import SIMBOL


class Cell(WorldObject):
    def __init__(self, x, y,  contents=WorldObject()):
        self.x = x
        self.y = y
        self.contents = contents
        super().__init__(contents)
