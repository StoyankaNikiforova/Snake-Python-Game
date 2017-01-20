from class_world_object import WorldObject


class Food(WorldObject):
    def __init__(self, name, energy):
        super().__init__(name, energy)
