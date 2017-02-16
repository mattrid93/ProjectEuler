"""Problem 7: 100001st prime.

Brute force again"""
import unittest
from utils.primes import is_prime

def nth_prime(n):
    """Returns nth prime"""
    current = 1
    primes = 0
    while primes < n:
        current += 1
        if is_prime(current):
            primes += 1
    return current


class TestNthPrime(unittest.TestCase):
    def test_nth_prime(self):
        self.assertEqual(nth_prime(1), 2)
        self.assertEqual(nth_prime(6), 13)

if __name__ == "__main__":
    print(nth_prime(10001))
    unittest.main()
