"""Utilities functions for factoring."""
import unittest
from numpy import sqrt

def find_proper_divisors(n):
    """Finds proper divisors of n"""
    if n == 1:
        return []
    divisors = [1]
    i = 2
    while i < sqrt(n):
        if not n%i:
            divisors.append(i)
            divisors.append(n//i)
        i += 1
    return divisors

class TestFunction(unittest.TestCase):
    def test_finder(self):
        self.assertEqual(find_proper_divisors(1), [])
        self.assertEqual(find_proper_divisors(2), [1])
        for d in find_proper_divisors(220):
            self.assertIn(d, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])

if __name__ == "__main__":
    unittest.main()
