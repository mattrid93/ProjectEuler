"""Problem 16: Power digit sum.

Keep track of digits individually"""
import unittest

def sum_power(n):
    """Sums digits of 2^n."""
    digits = [2]
    for _ in range(n-1):
        for i in range(len(digits)-1, -1, -1):
            d = digits[i]
            if 2*d > 9:
                digits[i] = (2*d)%10
                if i == len(digits)-1:
                    digits.append((2*d) // 10)
                else:
                    digits[i+1] += (2*d) // 10
            else:
                digits[i] = 2*d
    return sum(digits)

class TestMultiples(unittest.TestCase):
    def test_sum_power(self):
        self.assertEqual(sum_power(1), 2)
        self.assertEqual(sum_power(4), 7)
        self.assertEqual(sum_power(15), 26)

if __name__ == "__main__":
    print(sum_power(1000))
    unittest.main()
