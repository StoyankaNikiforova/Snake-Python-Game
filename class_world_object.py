from settings import SIMBOL


class WorldObject:
    def __init__(self, name='Empty', energy=0):
        self.name = name
        self.energy = energy
        super().__init__()

    def draw(self):
        simbol = SIMBOL[self.name]
        return simbol

    def __str__(self):
        return self.draw()

    def __repr__(self):
        return self.__str__()
