import unittest
import math
from calculator import add, subtract, log

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)

    def test_log(self):
        self.assertAlmostEqual(log(100, 10), 2.0)
        self.assertAlmostEqual(log(math.e), 1.0)
        with self.assertRaises(ValueError):
            log(0)
        with self.assertRaises(ValueError):
            log(-1)

if __name__ == "__main__":
    unittest.main()

