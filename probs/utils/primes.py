"""Utilities functions for prime numbers."""
import unittest

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

if __name__ == "__main__":
    unittest.main()
