"""Problem 36: Double base palindromes"""
import unittest

def is_palindrome(n):
    return [d for d in str(n)] == [d for d in str(n)[::-1]]

def binary_converter(n):
    pow_2 = 1
    while 2*pow_2 <= n:
        pow_2 *= 2
    bin_digits = []
    while n > 0:
        if n == 2:
            n = 0
            bin_digits.append(1)
            bin_digits.append(0)
        elif pow_2 <= n:
            bin_digits.append(1)
            n = n % pow_2
            pow_2 /= 2
        else:
            bin_digits.append(0)
            pow_2 /= 2
    return int("".join([str(d) for d in bin_digits]))

def solution():
    total = 0
    for n in range(1, 1000000, 2): # go up in odd numbers
        if is_palindrome(n) and is_palindrome(binary_converter(n)):
            total += n
    return total

class TestFunction(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertFalse(is_palindrome(10))
        self.assertFalse(is_palindrome(101001))
        self.assertFalse(is_palindrome(17653))
        self.assertTrue(is_palindrome(4))
        self.assertTrue(is_palindrome(585))
        self.assertTrue(is_palindrome(1001001001))

    def test_converter(self):
        self.assertEqual(binary_converter(1), 1)
        self.assertEqual(binary_converter(2), 10)
        self.assertEqual(binary_converter(5), 101)
        self.assertEqual(binary_converter(585), 1001001001)
        self.assertEqual(binary_converter(984327), 11110000010100000111)

if __name__ == "__main__":
    print(solution())
    unittest.main()
