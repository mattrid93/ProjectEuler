"""Problem 12: Highly divisible triangle number.

Brute force."""
import unittest
from utils.primes import find_prime_factors

def number_of_divisors(n):
    """Calculates number of divisors of n."""
    if n == 1:
        return 1
    prime_factors = find_prime_factors(n)
    table = {}
    for f in prime_factors:
        if f in table:
            table[f] += 1
        else:
            table[f] = 1
    divisors = 1
    for m in table.values():
        divisors *= (m+1)
    return divisors


def find_first_divisible_tri(n):
    """Finds first triangle number with more than n divisors"""
    tri = 1
    m = 1
    while(number_of_divisors(tri) <= n):
        m += 1
        tri += m
    return tri

class TestMultiples(unittest.TestCase):
    def test_n_divs(self):
        self.assertEqual(number_of_divisors(1), 1)
        self.assertEqual(number_of_divisors(2), 2)
        self.assertEqual(number_of_divisors(10), 4)
        self.assertEqual(number_of_divisors(28), 6)

    def test_ffdt(self):
        self.assertEqual(find_first_divisible_tri(5), 28)

if __name__ == "__main__":
    print(find_first_divisible_tri(500))
    unittest.main()
