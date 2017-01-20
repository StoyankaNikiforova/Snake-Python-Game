import unittest
from class_cell import Cell
from class_game_world import GameWorld
from class_food import Food


class test_game_world(unittest.TestCase):
    def setUp(self):
        self.game = GameWorld(15)
        food = Cell(2, 1, Food('Banana', 2))
        self.game.add_content_item(food)

    def test_print_game(self):
        print(self.game)
        print(self.game.content[2][1])

if __name__ == '__main__':
    unittest.main()
