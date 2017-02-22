"""Problem 39: Integer right triangles"""
import unittest

def find_b(p, a):
    """Calculates b for p and a combo using derived formula. False if b not
    int"""
    num = p*p/2 - a*p
    den = p - a
    if num % den:
        return False
    return num // den

def solution():
    best = (0, 0)
    for p in range(1001):
        n_sols = 0
        for a in range(p//3):
            if find_b(p, a):
                n_sols += 1
        if n_sols > best[1]:
            best = (p, n_sols)
    return best[0]


class TestFunction(unittest.TestCase):
    def test_finder(self):
        self.assertEqual(find_b(120, 20), 48)
        self.assertEqual(find_b(120, 24), 45)
        self.assertEqual(find_b(120, 30), 40)

if __name__ == "__main__":
    print(solution())
    unittest.main()
