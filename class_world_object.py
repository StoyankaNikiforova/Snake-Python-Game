from settings import EMPTY_SIMBOL


class WorldObject:
    def __init__(self, simbol=EMPTY_SIMBOL):
        self.simbol = simbol
        super(WorldObject, self).__init__()

    def draw(self):
        pass
