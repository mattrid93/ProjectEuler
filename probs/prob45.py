"""Problem 45: Triangular, pentagonal and hexagonal"""
import unittest
from math import sqrt

def solution():
    n = 2
    while n < 100000:
        tri = (n * (n + 1)) // 2
        P_n = 1/6 + sqrt(2*tri/3 + 1/36)
        H_n = 1/4 + sqrt(tri/2 + 1/16)
        if P_n.is_integer() and H_n.is_integer() and tri != 40755:
            return tri
        n += 1

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
