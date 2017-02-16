"""Problem 10: Summation of primes.

Generate primes using Sieve of Erat"""
import unittest
from numpy import sqrt

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

def sum_n_primes(n):
    """Returns sum of all primes below n"""
    return sum(seive_of_erat(n))

class TestMultiples(unittest.TestCase):
    def test_seive(self):
        self.assertEqual(seive_of_erat(2), [])
        self.assertEqual(seive_of_erat(4), [2, 3])
        self.assertEqual(seive_of_erat(10), [2, 3, 5, 7])
    def test_sum(self):
        self.assertEqual(sum_n_primes(10), 17)

if __name__ == "__main__":
    print(sum_n_primes(2000000))
    unittest.main()
