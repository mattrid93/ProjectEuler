"""Problem 37: Trucatable primes.

Build up primes from each side and find intersections"""
import unittest
from utils.primes import is_prime

def truncator(n):
    """Return left-right and right-left truncations of n"""
    digits = [d for d in str(n)]
    truncs = []
    for i in range(1, len(digits)):
        truncs.append(int("".join(digits[i:])))
        truncs.append(int("".join(digits[:-i])))
    return truncs

def add_digit(n, d, left):
    if left:
        return int(str(d)+str(n))
    else:
        return int(str(n)+str(d))

def solution():
    t_primes = []
    left_right = [3, 7]
    right_left = [2, 5, 3, 7]
    while len(t_primes) < 11:
        left_right = [add_digit(n, d, 1) for n in left_right
                                         for d in range(1, 10)]
        right_left = [add_digit(n, d, 0) for n in right_left
                                         for d in range(1, 10)]
        left_right = [p for p in left_right if is_prime(p)]
        right_left = [p for p in right_left if is_prime(p)]
        t_primes += [p for p in left_right if p in right_left]
    return sum(t_primes)

class TestFunction(unittest.TestCase):
    def test_truncator(self):
        for n in truncator(3797):
            self.assertIn(n, [3, 37, 379, 797, 97, 7])

    def test_adder(self):
        self.assertEqual(add_digit(5, 1, 1), 15)
        self.assertEqual(add_digit(243, 4, 1), 4243)
        self.assertEqual(add_digit(100, 7, 1), 7100)
        self.assertEqual(add_digit(5, 1, 0), 51)
        self.assertEqual(add_digit(243, 4, 0), 2434)
        self.assertEqual(add_digit(100, 7, 0), 1007)

if __name__ == "__main__":
    print(solution())
    unittest.main()
