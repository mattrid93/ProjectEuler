"""Problem 3: Largest prime factor"""
import unittest

def prime_factors(n):
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


class TestMultiples(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(13195), [5, 7, 13, 29])

if __name__ == "__main__":
    print(max(prime_factors(600851475143)))
    unittest.main()
