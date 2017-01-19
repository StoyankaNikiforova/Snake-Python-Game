from class_world_object import WorldObject
from class_vector2D import Vector2D


class Cell(WorldObject, Vector2D):
    def __init__(self, contents=None):
        super().__init__()
        self.contents = contents

    def __repr__(self):
        return self.__str__

    def __str__(self):
        return '{}{}{}'.format(self.x, self.y, self.simbol)
