import unittest
from settings import SQRT_SIMBOL
from class_cell import Cell


class test_game_world(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(SQRT_SIMBOL)

    def test_print_cell(self):
        print(self.cell)

if __name__ == '__main__':
    unittest.main()
