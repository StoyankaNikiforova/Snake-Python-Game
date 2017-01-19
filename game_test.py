import unittest
from class_game_world import GameWorld


class test_game_world(unittest.TestCase):
    def setUp(self):
        self.game = GameWorld(15)

    def test_print_game(self):
        print(self.game)
        print(self.game.content[3][4])

if __name__ == '__main__':
    unittest.main()
