"""Problem 25: 1000-digit Fibonnaci number.

Store digits in array"""
import unittest

def add_arrays(digits1, digits2):
    """Adds numbers represented by arrays of digits."""
    if len(digits1) > len(digits2):
        longer = digits1[::-1]
        shorter = digits2[::-1]
    else:
        longer = digits2[::-1]
        shorter = digits1[::-1]
    sum_digits = []
    carry = 0
    for i, d in enumerate(shorter):
        sum_digits.append(d + longer[i] + carry)
        carry = 0
        if sum_digits[i] > 9:
            carry = sum_digits[i] // 10
            sum_digits[i] = sum_digits[i] % 10
    if len(longer) > len(shorter):
        for d in longer[len(shorter):]:
            sum_digits.append(d + carry)
            carry = 0
    if carry != 0:
        sum_digits.append(carry)
    return sum_digits[::-1]

def find_fib_number(d):
    """Returns index of first Fib number with d digits"""
    prev = [1]
    current = [1]
    i = 2
    while len(current) < d:
        helper = current
        current = add_arrays(helper, prev)
        prev = helper
        i += 1
    return i

def solution():
    return find_fib_number(1000)


class TestFunction(unittest.TestCase):
    def test_adder(self):
        self.assertEqual(add_arrays([1], [1]), [2])
        self.assertEqual(add_arrays([1, 0], [1]), [1, 1])
        self.assertEqual(add_arrays([5], [5]), [1, 0])

    def test_fib_finder(self):
        self.assertEqual(find_fib_number(3), 12)

if __name__ == "__main__":
    print(solution())
    unittest.main()
