"""Utilities functions for prime numbers."""
import unittest
from numpy import sqrt

def is_prime(n):
    """Checks if n is prime (pretty naive algo)"""
    if n < 2:
        return False
    elif not n%2:
        return n == 2
    for i in range(3, n //2, 2):
        if not n%i:
            return False
    return True

def find_prime_factors(n):
    """Return prime factors of n"""
    p_factors = []
    current = n
    test = 2
    while test <= current:
        if not current%test:
            p_factors.append(test)
            current = current // test
            test = 2
        else:
            test += 1
    return p_factors

def seive_of_erat(n):
    """Generates all primes up to n using Seive of Erat"""
    marked = [1]*(n-1)
    for i in range(2,int(sqrt(n)+1)):
        if marked[i-2]:
            j = i*i
            while j <= n:
                marked[j-2] = 0
                j += i
    return [i for i in range(2,n) if marked[i-2]]


class TestPrimes(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(17), True)
        self.assertEqual(is_prime(253), False)
        self.assertEqual(is_prime(15485867), True)

    def test_prime_factors(self):
        self.assertEqual(find_prime_factors(2), [2])
        self.assertEqual(find_prime_factors(10), [2, 5])
        self.assertEqual(find_prime_factors(13195), [5, 7, 13, 29])

    def test_seive(self):
        self.assertEqual(seive_of_erat(2), [])
        self.assertEqual(seive_of_erat(4), [2, 3])
        self.assertEqual(seive_of_erat(10), [2, 3, 5, 7])


if __name__ == "__main__":
    unittest.main()
