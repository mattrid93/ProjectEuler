"""Problem 10: Summation of primes.

Generate primes using Sieve of Erat"""
import unittest
from numpy import sqrt

def sum_n_primes(n):
    """Returns sum of all primes below n"""
    return sum(seive_of_erat(n))

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_n_primes(10), 17)

if __name__ == "__main__":
    print(sum_n_primes(2000000))
    unittest.main()
