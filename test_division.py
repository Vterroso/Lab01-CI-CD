import unittest
from calculator import division

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(1, 2), 0.5)
        self.assertEqual(division(1, -1), -1)
        self.assertEqual(division(-1, -1), 1)
        self.assertEqual(division(0, 0), "Error: Division by zero is not allowed.")
        self.assertEqual(division(0, 1), 0)
        self.assertEqual(division(1, 0), "Error: Division by zero is not allowed.")
        self.assertEqual(division(4.5 , 2.4), 1.875)
        
if __name__ == '__main__':
    unittest.main()