"""Problem 24: Lexographic permutations.

Iteratively generate next permutation"""
import unittest

def next_perm(perm):
    """Generate next Lexographic permutation."""
    for i in range(len(perm)-1, 0, -1):
        if perm[i] > perm[i-1]:
            perm[i], perm[i-1] = perm[i-1], perm[i]
            return perm
    return False

def nth_finder(start, n_perm):
    if n_perm == 1:
        return start
    perm = start
    for i in range(n_perm-1):
        print(perm)
        perm = next_perm(perm)
        if not perm:
            return False
    return perm

def solution():
    pass

class TestFunction(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(next_perm([0, 1, 2]), [0, 2, 1])
        self.assertEqual(next_perm([2, 0, 1]), [2, 1, 0])
        self.assertFalse(next_perm([2, 1, 0]))
        self.assertEqual(next_perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                                   [0, 1, 2, 3, 4, 5, 6, 7, 9, 8])

    def test_nth_finder(self):
        self.assertEqual(nth_finder([0, 1, 2], 3), [1, 0, 2])
        self.assertFalse(nth_finder([0, 1, 2], 7))

if __name__ == "__main__":
    print(solution())
    unittest.main()
