"""Problem 53: Combinatoric selections"""
import unittest
from math import factorial

def nCr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def solution():
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if nCr(n, r) > 1e6:
                count += 1
    return count

class TestFunction(unittest.TestCase):
    def test_nCr(self):
        self.assertEqual(nCr(1, 1), 1)
        self.assertEqual(nCr(2, 1), 2)
        self.assertEqual(nCr(5, 3), 10)
        self.assertEqual(nCr(100, 5), 75287520)

if __name__ == "__main__":
    print(solution())
    unittest.main()
