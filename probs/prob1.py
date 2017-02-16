"""Problem 1: Multiples of three and five."""
import unittest

def sum_multiples(n):
    """Returns the sum of multiples of three and five below n"""
    assert n >= 0
    return sum([i for i in range(n) if (not i%3) or (not i%5)])

class TestMultiples(unittest.TestCase):
    def test_10(self):
        self.assertEqual(sum_multiples(10), 23)

if __name__ == "__main__":
    print(sum_multiples(10000))
    unittest.main()
