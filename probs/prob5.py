"""Problem 5: Smallest multiple.

Calculate using GCD method of finding LCM. Calculate GCD using Euclids
method."""
import unittest

def greatest_common_divisor(a, b):
    """Returns greatest common divisor of a and b"""
    assert a > 0
    assert b > 0
    while b:
        a, b = b, a%b
    return a

def lowest_common_multiple(a, b):
    """Returns lowest common multiple of a and b"""
    assert a > 0
    assert b > 0
    return a*b // greatest_common_divisor(a, b)

def lcm_list(nums):
    assert all(nums) > 0
    if len(nums) == 2:
        return lowest_common_multiple(nums[0], nums[1])
    else:
        return lcm_list([nums[0], lcm_list(nums[1:])])


class TestMultiples(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(greatest_common_divisor(1, 1), 1)
        self.assertEqual(greatest_common_divisor(1, 100), 1)
        self.assertEqual(greatest_common_divisor(24, 54), 6)
        self.assertEqual(greatest_common_divisor(48, 180), 12)

    def test_lcm(self):
        self.assertEqual(lowest_common_multiple(1, 1), 1)
        self.assertEqual(lowest_common_multiple(1, 100), 100)
        self.assertEqual(lowest_common_multiple(48, 180), 720)

    def test_lcm_plural(self):
        self.assertEqual(lcm_list([8, 9, 21]), 504)
        self.assertEqual(lcm_list(list(range(1,11))), 2520)

if __name__ == "__main__":
    print(lcm_list(list(range(1,21))))
    unittest.main()
