from class_world_object import WorldObject
from class_vector2D import Vector2D
from class_cell import Cell


class Python:
    LEFT = Vector2D(0, 1)
    RIGHT = Vector2D(0, -1)
    UP = Vector2D(1, 0)
    DOWN = Vector2D(-1, 0)

    def __init__(self, world, coords, size, direction):
        self.world = world
        self.position = Vector2D(coords[0], coords[1])
        self.size = size
        self.direction = direction
        self.head = WorldObject('Snake_hade')
        self.part = WorldObject('Snake_body')
        self.draw()

    def draw(self):
        head_cell = Cell(self.position.x, self.position.y, self.head)
        self.world.add_content_item(head_cell)

        part_position = self.position + self.direction
        for i in range(self.size):
            part_cell = Cell(part_position.x, part_position.y, self.part)
            self.world.add_content_item(part_cell)
            part_position += self.direction

    def __str__(self):
        snake = str(self.head)
        for i in range(self.size):
            snake += str(self.part)
        return snake
