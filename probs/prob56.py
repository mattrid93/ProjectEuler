"""Problem 56: Maximal digit sum"""
import unittest

def solution():
    return max([sum([int(d) for d in str(a**b)]) for a in range(100) for b in range(100)])

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
