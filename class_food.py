from class_world_object import WorldObject


class Food(WorldObject):
    def __init__(self, name, energy):
        self.energy = energy
        super().__init__(name)
