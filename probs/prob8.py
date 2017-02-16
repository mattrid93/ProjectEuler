"""Problem 8: ???"""
import unittest

def max_adjacent(filename, n):
    """Finds maximum product of n adjacent numbers in input number"""
    digits = []
    with open(filename) as f:
        for line in f.readlines():
            digits += [int(d) for d in line if d != "\n"]
    highest = 0
    for i in range(len(digits)-n):
        current = 1
        for j in range(n):
            current *= digits[i+j]
        highest = max(current, highest)
    return highest


class TestMultiples(unittest.TestCase):
    def test_max_adjacent(self):
        filename = "inputs/prob8.txt"
        self.assertEqual(max_adjacent(filename, 4), 5832)

if __name__ == "__main__":
    filename = "inputs/prob8.txt"
    print(max_adjacent(filename, 13))
    unittest.main()
