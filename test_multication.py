import unittest
from calculator import multiplication

class TestMultiplication(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(multiplication(1, 2), 2)
        self.assertEqual(multiplication(1, -1), -1)
        self.assertEqual(multiplication(-1, -1), 1)
        self.assertEqual(multiplication(0, 0), 0)
        self.assertEqual(multiplication(0, 1), 0)
        self.assertEqual(multiplication(1, 0), 0)
        self.assertEqual(multiplication(872, 9879879878798), 8615255254311856)
    