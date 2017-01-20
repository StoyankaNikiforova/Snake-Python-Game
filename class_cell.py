from class_world_object import WorldObject
from class_vector2D import Vector2D


class Cell(Vector2D, WorldObject):
    def __init__(self, x, y,  contents=None):
        super().__init__(x, y)
        self.contents = contents

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.simbol
