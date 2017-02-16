"""Problem 6: Sum square difference.

Brute force"""
import unittest

def sum_square_difference(n):
    """Calculates difference between sum of squares and square of sum of first
    n natural numbers."""
    sum_squares = sum([x*x for x in range(1, n+1)])
    square_sum = sum([x for x in range(1, n+1)])**2
    return square_sum - sum_squares

class TestSSD(unittest.TestCase):
    def test_ssd(self):
        self.assertEqual(sum_square_difference(10), 2640)

if __name__ == "__main__":
    print(sum_square_difference(100))
    unittest.main()
