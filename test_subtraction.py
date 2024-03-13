import unittest
from calculator import subtraction

class TestSubtraction(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(subtraction(1, 2), -1)
        self.assertEqual(subtraction(1, -1), 2)
        self.assertEqual(subtraction(-1, -1), 0)
        self.assertEqual(subtraction(0, 0), 0)
        self.assertEqual(subtraction(0, 1), -1)
        self.assertEqual(subtraction(1, 0), 1)
        self.assertEqual(subtraction(1, 1), 0)
        
if __name__ == '__main__':
    unittest.main()