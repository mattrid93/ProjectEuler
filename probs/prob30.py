"""Problem ?: ???"""
import unittest

def is_sum(n, power):
    """Returns whether n is equal to the sum of its digits to the given power"""
    if n == 1:
        return False
    return n == sum([int(d)**power for d in str(n)])

def summer(power):
    """Sums all numbers that can be written as sum of their digits to given
    power"""
    total = 0
    for i in range(2, 300000): # hardcoded limit based on 5*(9**5)
        if is_sum(i, power):
            total += i
    return total

def solution():
    return summer(5)

class TestFunction(unittest.TestCase):
    def test_is_sum(self):
        self.assertFalse(is_sum(1, 4))
        self.assertFalse(is_sum(100, 4))
        self.assertFalse(is_sum(1432, 4))
        self.assertTrue(is_sum(1634, 4))
        self.assertTrue(is_sum(8208, 4))
        self.assertTrue(is_sum(9474, 4))

    def test_summer(self):
        self.assertEqual(summer(4), 19316)


if __name__ == "__main__":
    print(solution())
    unittest.main()
