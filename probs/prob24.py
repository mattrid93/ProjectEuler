"""Problem 24: Lexographic permutations.

Iteratively generate permutations"""
import unittest

def is_permutation(n, d):
    """Checks to see if n is a permutation of the digits 0-d."""
    n = [int(i) for i in str(n)]
    if len(n) < d or len(n) > d+1:
        return False
    elif len(n) < d+1:
        n.insert(0, 0)
    while n:
        i = n.pop(0)
        if i in n or i > d:
            return False
    return True

def next_perm(digits):
    """Generate next Lexographic permutation."""
    i = -1
    for i_ in range(1, len(digits)):
        if digits[i_-1] < digits[i_]:
            i = i_
    if i == -1:
        return False
    suffix = digits[i:]
    prefix = digits[:i-1]
    pivot = digits[i-1]
    j = 0
    for j_ in range(i, len(digits)):
        if digits[j_] > pivot:
            j = j_
    suffix[j-i] = pivot
    pivot = digits[j]
    new_digits = prefix + [pivot] + suffix[::-1]
    return new_digits


def nth_finder(start, n_perm):
    if n_perm == 1:
        return start
    perm = start
    for i in range(n_perm-1):
        perm = next_perm(perm)
        if not perm:
            return False
    return perm

def solution():
    return nth_finder([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000)

class TestFunction(unittest.TestCase):
    def test_is_perm(self):
        self.assertTrue(is_permutation(1, 1))
        self.assertTrue(is_permutation(12, 2))
        self.assertTrue(is_permutation(201, 2))
        self.assertTrue(is_permutation(1234, 4))
        self.assertFalse(is_permutation(51, 2))
        self.assertFalse(is_permutation(1224, 4))
        self.assertFalse(is_permutation(130, 3))

    def test_generator(self):
        self.assertEqual(next_perm([0, 1, 2]), [0, 2, 1])
        self.assertEqual(next_perm([2, 0, 1]), [2, 1, 0])
        self.assertFalse(next_perm([2, 1, 0]))
        self.assertEqual(next_perm([1, 2, 3, 4, 5, 6, 7, 8, 9]),
                                   [1, 2, 3, 4, 5, 6, 7, 9, 8])

    def test_nth_finder(self):
        self.assertEqual(nth_finder([0, 1, 2], 3), [1, 0, 2])
        self.assertFalse(nth_finder([0, 1, 2], 7))

if __name__ == "__main__":
    print(solution())
    unittest.main()
