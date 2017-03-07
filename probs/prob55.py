"""Problem 55: Lychrel numbers"""
import unittest

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    """Returns n + reversed(n)."""
    return n + int(str(n)[::-1])

def is_Lychrel(n):
    """"Tests up to 50 iterations."""
    count = 1
    current = n
    while count < 50:
        current = reverse_and_add(current)
        if is_palindrome(current):
            return False
        count += 1
    return True

def solution():
    count = 0
    for n in range(1, 10001):
        if is_Lychrel(n):
            count += 1
    return count

class TestFunction(unittest.TestCase):
    def test_tester(self):
        self.assertTrue(is_palindrome(5))
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(286682))
        self.assertFalse(is_palindrome(57))
        self.assertFalse(is_palindrome(125))
        self.assertFalse(is_palindrome(733))

    def test_reverse_and_add(self):
        self.assertEqual(reverse_and_add(349), 1292)
        self.assertEqual(reverse_and_add(1292), 4213)
        self.assertEqual(reverse_and_add(4213), 7337)

    def test_is_Lychrel(self):
        self.assertFalse(is_Lychrel(1))
        self.assertFalse(is_Lychrel(349))
        self.assertTrue(is_Lychrel(196))

if __name__ == "__main__":
    print(solution())
    unittest.main()
