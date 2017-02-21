"""Problem 33: Digit cancelling fractions.

Weird that it's 100"""
import unittest
from functools import reduce
from utils.primes import find_prime_factors

def is_curious(num, den):
    """Returns if fraction is of curious type"""
    num_d = [int(d) for d in str(num)]
    den_d = [int(d) for d in str(den)]
    intersection = [d for d in num_d if d in den_d]
    if len(intersection) in [0, 2]:
        return False
    int_d = intersection[0]
    if int_d == 0:
        return False
    num_d.remove(int_d)
    den_d.remove(int_d)
    if den_d == [0]:
        return False
    return num/den == num_d[0]/den_d[0]

def solution():
    fractions = [(num, den) for den in range(10, 100)
                            for num in range(10, den)
                            if is_curious(num, den)]
    numerator = reduce(lambda x, y: x * y, [f[0] for f in fractions])
    denominator = reduce(lambda x, y: x * y, [f[1] for f in fractions])
    print(fractions)
    print(numerator, denominator)
    i = 2
    while i < denominator:
        if (not numerator%i) and (not denominator%i):
            numerator //= i
            denominator //= i
            i = 2
        else:
            i += 1
    return denominator

class TestFunction(unittest.TestCase):
    def test_is_curious(self):
        self.assertTrue(is_curious(49, 98))
        self.assertFalse(is_curious(34, 75))
        self.assertFalse(is_curious(20, 22))

if __name__ == "__main__":
    print(solution())
    unittest.main()
