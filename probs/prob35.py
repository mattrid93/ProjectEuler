"""Problem 35: Circular primes."""
import unittest
from utils.primes import seive_of_erat

def rotations(n):
    """Returns rotations of digits of n"""
    if n < 10:
        return [n]
    digits = [d for d in str(n)]
    rotations = []
    for i in range(len(digits)):
        rotated = digits[i:] + digits[:i]
        rotations.append(int("".join(rotated)))
    return rotations

def solution():
    list_of_primes = seive_of_erat(1000000)
    set_of_primes = set(list_of_primes)
    num_circ_primes = 0
    for prime in list_of_primes:
        circ = True
        for rotation in rotations(prime):
            if rotation not in set_of_primes:
                circ = False
        if circ:
            num_circ_primes += 1
    return num_circ_primes

class TestFunction(unittest.TestCase):
    def test_rotator(self):
        self.assertEqual(rotations(6), [6])
        self.assertEqual(rotations(14), [14, 41])
        self.assertEqual(rotations(634), [634, 346, 463])


if __name__ == "__main__":
    print(solution())
    unittest.main()
