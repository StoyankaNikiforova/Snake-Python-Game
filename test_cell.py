import unittest
from settings import SIMBOL
from class_cell import Cell
from class_world_object import WorldObject


class test_game_world(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(1, 2, contents=WorldObject())

    def test_print_cell(self):
        print(self.cell)

if __name__ == '__main__':
    unittest.main()
