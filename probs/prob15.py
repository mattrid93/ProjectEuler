"""Problem 15: Longest paths.

Simple combinatorics problem"""
import unittest
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def paths(g):
    """Number of possible paths through a square grid of side g."""
    return int(nCr(2*g, g))


class TestMultiples(unittest.TestCase):
    def test_nCr(self):
        self.assertEqual(nCr(1, 1), 1)
        self.assertEqual(nCr(2, 1), 2)
        self.assertEqual(nCr(40, 20), 137846528820)
    def test_paths(self):
        self.assertEqual(paths(2), 6)

if __name__ == "__main__":
    print(paths(20))
    unittest.main()
