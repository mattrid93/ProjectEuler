"""Problem 49: Prime permutations"""
import unittest
from utils.primes import seive_of_erat

class TestFunction(unittest.TestCase):
    pass

def solution():
    four_digit_primes = [p for p in seive_of_erat(10000) if p > 999]
    for i, prime1 in enumerate(four_digit_primes):
        if prime1 == 1487:
            continue
        for prime2 in four_digit_primes[i+1:]:
            prime3 = 2*prime2 - prime1
            if prime3 in four_digit_primes:
                if set(str(prime1)) == set(str(prime2)) == set(str(prime3)):
                    return str(prime1) + str(prime2) + str(prime3)



if __name__ == "__main__":
    print(solution())
    unittest.main()
