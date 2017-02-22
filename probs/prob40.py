"""Problem ?: ???"""
import unittest
from functools import reduce

def solution():
    frac = ""
    n = 1
    while len(frac) < 1000000:
        frac += str(n)
        n += 1
    return reduce(lambda x, y: x*y, [int(frac[d-1])
                        for d in [1, 10, 100, 1000, 10000, 100000, 1000000]])

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
