"""Problem 4: Largest palindrome product.

Brute force check."""
import unittest

def is_palindrome(n):
    """Tests if n is a palindrome"""
    return str(n) == str(n)[::-1]

def largest_palindrome_product(d):
    """Finds the largest palindrome product of 2 numbers with d digits"""
    lim = int("1"+"0"*d)
    largest = 0
    for i in range(lim):
        for j in range(lim):
            if is_palindrome(i*j) and i*j > largest:
                largest = i*j
    return largest

class TestMultiples(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertEqual(is_palindrome(0), True)
        self.assertEqual(is_palindrome(7), True)
        self.assertEqual(is_palindrome(15), False)
        self.assertEqual(is_palindrome(192), False)
        self.assertEqual(is_palindrome(14241), True)

    def test_largest_palindrom_product(self):
        self.assertEqual(largest_palindrome_product(2), 9009)

if __name__ == "__main__":
    print(largest_palindrome_product(3))
    unittest.main()
