"""Problem 21: Amicable numbers."""
import unittest
from numpy import sqrt

def find_proper_divisors(n):
    """Finds proper divisors of n"""
    if n == 1:
        return []
    divisors = [1]
    i = 2
    while i < sqrt(n):
        if not n%i:
            divisors.append(i)
            divisors.append(n//i)
        i += 1
    return divisors

def check_amicable(n):
    """Tests if n is an amicable number. If true, returns other half of pair."""
    other_side = sum(find_proper_divisors(n))
    if n == other_side:
        return False
    if sum(find_proper_divisors(other_side)) == n:
        return other_side
    return False

def sum_amicable_pairs(n):
    """Sums amicable pairs below n."""
    candidates = list(range(1, n))
    sum_pairs = 0
    for i in candidates:
        check = check_amicable(i)
        if check:
            sum_pairs += i
            candidates.remove(i)
            sum_pairs += check
            candidates.remove(check)
    return sum_pairs


class TestFunction(unittest.TestCase):
    def test_finder(self):
        self.assertEqual(find_proper_divisors(1), [])
        self.assertEqual(find_proper_divisors(2), [1])
        for d in find_proper_divisors(220):
            self.assertIn(d, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110])

    def test_checker(self):
        self.assertFalse(check_amicable(1))
        self.assertFalse(check_amicable(17))
        self.assertEqual(check_amicable(220), 284)
        self.assertEqual(check_amicable(284), 220)

if __name__ == "__main__":
    print(sum_amicable_pairs(10000))
    unittest.main()
