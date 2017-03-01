"""Problem 52: Permuted multiples"""
import unittest
from utils.primes import seive_of_erat

def get_multiples(n):
    """Returns 2,3,4,5,6x multiples on n"""
    return [i*n for i in range(2, 7)]

def is_permutation(n, m):
    if len(str(n)) != len(str(m)):
        return False
    for d in str(n):
        if d not in str(m):
            return False
    for d in str(m):
        if d not in str(n):
            return False
    return True

def solution():
    limit = 1000000
    for p in range(1, limit):
        permutes = get_multiples(p)
        i = 0
        while is_permutation(p, permutes[i]):
            i += 1
            if i == 5:
                return p
    return False

class TestFunction(unittest.TestCase):
    def test_multiples(self):
        self.assertEqual(get_multiples(1), [2, 3, 4, 5, 6])
        self.assertEqual(get_multiples(101), [202, 303, 404, 505, 606])

    def test_permuter(self):
        self.assertTrue(is_permutation(125874, 251748))
        self.assertFalse(is_permutation(125874, 251745))
        self.assertFalse(is_permutation(125834, 251748))

if __name__ == "__main__":
    print(solution())
    unittest.main()
