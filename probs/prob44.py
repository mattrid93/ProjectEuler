"""Problem 44: Pentagon numbers"""
import unittest
from math import sqrt

def generate_pents(limit):
    """Generates pentagonal numbers up to limit"""
    n = 1
    pents = []
    while n*(3*n - 1)/2 < limit:
        pents.append((n*(3*n - 1)//2))
        n += 1
    return pents

def solution():
    j = 2
    while j < 100000:
        P_j = j * (3*j - 1) // 2
        m = 2
        while m < j:
            P_m = m * (3*m - 1) // 2
            add = P_m + P_j
            n = 1/6 + sqrt(2*add/3 + 1/36)
            if n.is_integer():
                add2 = P_j + 2*P_m
                k = 1/6 + sqrt(2*add2/3 + 1/36)
                if k.is_integer():
                    return P_j
            m += 1
        j += 1



class TestFunction(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(generate_pents(2), [1])
        self.assertEqual(generate_pents(146), [1, 5, 12, 22, 35, 51, 70, 92, 117, 145])

if __name__ == "__main__":
    print(solution())
    unittest.main()
