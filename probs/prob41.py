"""Problem 41: Pandigital primes"""
import unittest
from prob24 import next_perm
from utils.primes import is_prime

def is_n_pandigital(n):
    """Tests if n is 1-len(n) pandigital."""
    if len(str(n)) > 9:
        return False
    if len(str(n)) != len(set(str(n))):
        return False
    m = len(str(n))
    digits = list(range(1, m+1))
    filtered = [d for d in str(n) if int(d) in digits]
    return len(str(n)) == len(filtered)

def solution():
    digits = [1, 2, 3, 4, 5, 6, 7]
    best = 0
    current = digits
    while len(digits) < 10:
        conc = int("".join([str(d) for d in current]))
        if is_prime(conc):
            best = conc
        current = next_perm(current)
        if not current:
            digits.append(digits[-1] + 1)
            current = digits
    return best


class TestFunction(unittest.TestCase):
    def test_tester(self):
        self.assertFalse(is_n_pandigital(2))
        self.assertFalse(is_n_pandigital(445))
        self.assertFalse(is_n_pandigital(52439))
        self.assertTrue(is_n_pandigital(1))
        self.assertTrue(is_n_pandigital(21))
        self.assertTrue(is_n_pandigital(52431))

if __name__ == "__main__":
    print(solution())
    unittest.main()
