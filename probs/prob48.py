"""Problem 48: Self powers"""
import unittest

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(sum([(x**x)%10000000000 for x in range(1, 1001)])%10000000000)
    unittest.main()
