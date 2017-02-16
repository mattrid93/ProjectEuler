"""Problem 20: Factorial digit sum.

Track digits individually"""
import unittest

def sum_factorial(n):
    """Return sum of all digits in n!"""
    current = n
    digits = [int(d) for d in str(n)[::-1]]
    while current > 2:
        current -= 1
        carry = [0, 0]
        for i in range(len(digits)):
            d = digits[i]
            d *= current
            d += carry[0]
            carry[0], carry[1] = carry[1], 0
            digits[i] = d%10
            carry[0] += d//10 - d//100*10
            carry[1] += d//100
            if i == len(digits)-1 and (carry[0] or carry[1]):
                digits.append(carry[0])
                if carry[1]:
                    digits.append(carry[1])
    return sum(digits)

class TestFunction(unittest.TestCase):
    def test_sum_facorial(self):
        self.assertEqual(sum_factorial(10), 27)

if __name__ == "__main__":
    print(sum_factorial(100))
    unittest.main()
