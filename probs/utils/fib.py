"""Utilities functions for the Fibonacci sequence."""
import unittest

def generate_term(n):
    """Generates nth term in the Fibonacci sequence"""
    assert n >= 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return generate_term(n-1) + generate_term(n-2)

def generate_sequence(n):
    """Generates Fibonacci sequence up to n terms"""
    return [generate_term(i) for i in range(1, n+1)]

class TestFib(unittest.TestCase):
    def test_term_generator(self):
        self.assertEqual(generate_term(1), 1)
        self.assertEqual(generate_term(2), 2)
        self.assertEqual(generate_term(10), 89)

    def test_generate_sequence(self):
        self.assertEqual(generate_sequence(1), [1])
        self.assertEqual(generate_sequence(2), [1, 2])
        self.assertEqual(generate_sequence(10), [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

if __name__ == "__main__":
    unittest.main()
