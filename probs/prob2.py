"""Problem 2: Even Fibonacci numbers.

Easy to just perform sum."""
import unittest

def sum_even_fib_numbers(n):
    """Sum even terms of Fib sequence up to n"""
    assert n >= 0
    total = 0
    current_term = 1
    last_term = 1
    while current_term <= n:
        if not current_term%2:
            total += current_term
        current_term, last_term = current_term + last_term, current_term
    return total

class TestMultiples(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_even_fib_numbers(89), 44)

if __name__ == "__main__":
    print(sum_even_fib_numbers(4e6))
    unittest.main()
