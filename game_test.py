import unittest
from class_cell import Cell
from class_game_world import GameWorld
from class_food import Food
from class_black_hole import BlackHole
from class_python import Python
from class_wall import Wall


class test_game_world(unittest.TestCase):
    def setUp(self):
        self.game = GameWorld(15)
        food = Cell(2, 1, Food('Banana', 2))
        self.wall = Cell(2, 1, Wall())
        self.black_hole = Cell(5, 6, BlackHole())
        self.game.add_content_items([food])
        self.python = Python(self.game, (5, 6), 5, Python.DOWN)

    def test_print_game(self):
        print(self.game)

    def test_add_content(self):
        self.assertEqual(self.game.add_content_items([self.wall, self.black_hole]), 'uheciewwijd')
        print(self.game)

if __name__ == '__main__':
    unittest.main()
