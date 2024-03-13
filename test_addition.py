import unittest
from calculator import addition

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(1, 2), 3)
        self.assertEqual(addition(1, -1), 0)
        self.assertEqual(addition(-1, -1), -2)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(0, 1), 1)
        self.assertEqual(addition(1, 0), 1)

if __name__ == '__main__':
    unittest.main()