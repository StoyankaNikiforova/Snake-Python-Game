from settings import EMPTY_SIMBOL


class WorldObject:
    def __init__(self, simbol=EMPTY_SIMBOL):
        self.simbol = simbol

    def draw(self):
        pass
