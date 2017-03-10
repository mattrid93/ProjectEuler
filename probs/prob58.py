"""Problem 58: Spiral primes"""
import unittest
from utils.primes import seive_of_erat, is_prime

def get_corners(n):
    """Returns corner numbers of layer n"""
    end = end = (2*n + 1) * (2*n + 1)
    return [end-m*n for m in range(0,8,2)]

def solution():
    # primes_list = seive_of_erat(1000000000)
    # primes_set = set(primes_list)
    n = 1
    all_corners = 5
    corner_primes = 3
    while corner_primes / all_corners >= 0.1:
        n += 1
        end = (2*n + 1) * (2*n + 1)
        all_corners += 4
        corner_primes += len([1 for c in get_corners(n) if is_prime(c)])
    return 2*n + 1

class TestFunction(unittest.TestCase):
    def test_corners(self):
        self.assertEqual(get_corners(1), [9, 7, 5, 3])
        self.assertEqual(get_corners(2), [25, 21, 17, 13])
        self.assertEqual(get_corners(3), [49, 43, 37, 31])

if __name__ == "__main__":
    print(solution())
    unittest.main()
