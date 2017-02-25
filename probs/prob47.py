"""Problem ?: ???"""
import unittest
from utils.primes import find_prime_factors, seive_of_erat

def solution():
    conseq = 4
    limit = 200000
    primes_list = set(seive_of_erat(limit))
    n = 10
    while n < limit:
        n += 1
        if n in primes_list:
            continue
        distinct = True
        for m in range(n, n+conseq):
            facts = find_prime_factors(m)
            if len(set(facts)) != conseq:
                distinct = False
                n = m
                break
        if distinct:
            return n

class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
