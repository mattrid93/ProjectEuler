"""Problem 27: Quadratic primes"""
import unittest
from utils.primes import seive_of_erat

def quadratic_function(n, a, b):
    return n*n + a*n + b

def solution():
    best_len = 0
    best_pair = None
    primes_list = set(seive_of_erat(10000))
    for a in range(-999,1000):
        for b in range(-999, 1000):
            n = 0
            while quadratic_function(n, a, b) in primes_list:
                n += 1
            if n-1 > best_len:
                best_len = n-1
                best_pair = (a, b)
    return best_pair, best_len, best_pair[0]*best_pair[1]



class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
