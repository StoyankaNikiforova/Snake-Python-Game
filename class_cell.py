from class_world_object import WorldObject
from class_vector2D import Vector2D
from settings import SIMBOL


class Cell(Vector2D, WorldObject):
    def __init__(self, x, y,  contents=WorldObject()):
        self.contents = contents
        super().__init__(x, y)
