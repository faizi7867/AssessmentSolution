import unittest
from Program2 import Square, Shape

class TestProgram2(unittest.TestCase):
    def test_square_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)

    def test_shape_area(self):
        shape = Shape()
        self.assertEqual(shape.area(), 0)

if __name__ == '__main__':
    unittest.main()