"""Problem 21: Amicable numbers."""
import unittest
from utils.factoring import find_proper_divisors

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
    def test_checker(self):
        self.assertFalse(check_amicable(1))
        self.assertFalse(check_amicable(17))
        self.assertEqual(check_amicable(220), 284)
        self.assertEqual(check_amicable(284), 220)

if __name__ == "__main__":
    print(sum_amicable_pairs(10000))
    unittest.main()
