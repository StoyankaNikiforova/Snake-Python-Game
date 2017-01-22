class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(Vector2D, self).__init__()

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
