import unittest
from Program1 import compute_word_frequency

class TestProgram1(unittest.TestCase):
    def test_compute_word_frequency(self):
        text = "which is better python 2 or python 3"
        expected_output = {'2': 1, '3': 1, 'better': 1, 'is': 1, 'or': 1, 'python': 2, 'which': 1}
        self.assertEqual(compute_word_frequency(text), expected_output)

if __name__ == '__main__':
    unittest.main()