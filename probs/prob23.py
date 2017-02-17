"""Problem 23: Non abundant sums"""
import unittest
from utils.primes import find_prime_factors_table

def sum_proper_divisors(n):
    """Sums proper divisors of n using prime factoring"""
    prime_factors = find_prime_factors_table(n)
    d_sum = 1
    for pf, a in prime_factors.items():
        d_sum *= int((pf**(a+1) - 1)/(pf - 1))
    return d_sum - n

def is_abundant(n):
    """Checks if n is an abundant number."""
    if n == 0:
        return False
    return sum_proper_divisors(n) > n

def solution():
    """Sum all integers that cannot be written as the sum of two abundant
    numbers."""
    # Calculate all abundant numbers < 28123/2
    abundants = [x for x in range(28124) if is_abundant(x)]
    # Seive out numbers that can be written as sums
    numbers = {}
    for i in range(28124):
        numbers[i] = True
    for i in abundants:
        for j in abundants:
            numbers[i+j] = False
    return sum([x for x in range(28124) if numbers[x]])



class TestFunction(unittest.TestCase):
    def test_summer(self):
        self.assertEqual(sum_proper_divisors(1), 0)
        self.assertEqual(sum_proper_divisors(12), 16)
        self.assertEqual(sum_proper_divisors(1800), 4245)
    def test_is_abundant(self):
        self.assertFalse(is_abundant(0))
        self.assertFalse(is_abundant(1))
        self.assertFalse(is_abundant(5))
        self.assertTrue(is_abundant(12))
        self.assertFalse(is_abundant(28))
        self.assertFalse(is_abundant(28123))

if __name__ == "__main__":
    print(solution())
    unittest.main()
