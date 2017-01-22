from class_world_object import WorldObject
import unittest


class testWorlfObject(unittest.TestCase):
    def setUp(self):
        self.obj = WorldObject()

    def test_drow(self):
        self.assertEqual(self.obj.draw(), '□')

    def test_drow(self):
        self.assertEqual(str(self.obj), '+')


if __name__ == '__main__':
    unittest.main()
