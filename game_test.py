import unittest
from class_cell import Cell
from class_game_world import GameWorld
from class_food import Food
from class_black_hole import BlackHole
from class_python import Python


class test_game_world(unittest.TestCase):
    def setUp(self):
        self.game = GameWorld(15)
        food = Cell(2, 1, Food('Banana', 2))
        self.game.add_content_item(food)
        self.python = Python(self.game, (5, 6), 5, Python.DOWN)

    def test_print_game(self):
        # self.python.draw()
        print(self.game)

if __name__ == '__main__':
    unittest.main()
