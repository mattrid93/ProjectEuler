"""Problem 3: Largest prime factor"""
import unittest
from utils.primes import prime_factors

if __name__ == "__main__":
    print(max(prime_factors(600851475143)))
    unittest.main()
