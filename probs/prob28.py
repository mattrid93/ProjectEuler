"""Problem 28: Number spiral diagonals"""
import unittest

def sum_diagonals(side_length):
    """Sums diagonals of a number spiral with given side length."""
    total = 25
    bottom_corner = 3
    for s in range(5, side_length+2, 2):
        bottom_corner += 4*s - 10
        for c in range(4):
            total += bottom_corner + (s-1)*c
    return total

def solution():
    return sum_diagonals(1001)

class TestFunction(unittest.TestCase):
    def test_summer(self):
        self.assertEqual(sum_diagonals(5), 101)

if __name__ == "__main__":
    print(solution())
    unittest.main()
