"""Problem 29: Distinct powers"""
import unittest

def distinct_terms(n):
    """Finds number of distinct terms a^b for 2<=a<=n, 2<=b<=n"""
    return len(set([a**b for a in range(2, n+1) for b in range(2, n+1)]))

def solution():
    return distinct_terms(100)

class TestFunction(unittest.TestCase):
    def test_distinct_terms(self):
        self.assertEqual(distinct_terms(5), 15)

if __name__ == "__main__":
    print(solution())
    unittest.main()
