"""Problem 46: Goldbachs other conjecture."""
import unittest
from math import sqrt
from utils.primes import seive_of_erat

def solution():
    limit = 10000
    primes_list = set(seive_of_erat(limit))
    n = 9
    while n < limit:
        if n not in primes_list:
            primes_below = seive_of_erat(n)
            conjecture_false = True
            for p in primes_below:
                if sqrt((n-p)/2).is_integer():
                    conjecture_false = False
            if conjecture_false:
                return n
        n += 2

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
