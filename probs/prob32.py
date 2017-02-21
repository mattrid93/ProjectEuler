"""Problem 32: Pandigital products"""
import unittest
from numpy import sqrt

def digits_are_unique(n):
    """Returns whether digits in n are unique (and no 0)"""
    digits = set([int(d) for d in str(n)])
    if 0 in digits:
        return False
    return len(str(n)) == len(digits)

def is_pandigital(a, b, c):
    """Returns whether identity is pandigital"""
    digits = [int(d) for d in str(a) + str(b) + str(c)]
    if len(digits) != 9:
        return False
    if 0 in digits:
        return False
    while digits:
        d = digits.pop(0)
        if d in digits:
            return False
    return True

def solution():
    products = set()
    for a in range(50000): # order of mag guess for limit
        if digits_are_unique(a):
            for b in range(50000//a):
                if digits_are_unique(b):
                    c = a*b
                    if is_pandigital(a, b, c):
                        products.add(c)

    return sum(products)

class TestFunction(unittest.TestCase):
    def test_digits(self):
        self.assertTrue(digits_are_unique(123))
        self.assertTrue(digits_are_unique(7492))
        self.assertFalse(digits_are_unique(113))
        self.assertFalse(digits_are_unique(8268))

    def test_is_pandigital(self):
        self.assertTrue(is_pandigital(123, 456, 789))
        self.assertTrue(is_pandigital(12, 4536, 879))
        self.assertTrue(is_pandigital(39, 186, 7254))
        self.assertFalse(is_pandigital(103, 456, 789))
        self.assertFalse(is_pandigital(1, 4, 7))
        self.assertFalse(is_pandigital(113, 456, 789))

if __name__ == "__main__":
    print(solution())
    unittest.main()
