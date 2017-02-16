"""Problem 14: Longest Collatz sequence.

Directly calculate, use hash table to speed up."""
import unittest

def next_term(n):
    """Generates next term in Collatz sequence after n."""
    if n%2:
        return 3*n + 1
    return n // 2


def generate_collatz_sequence(start):
    """Generates Collatz sequence starting from start."""
    sequence = [start]
    current = start
    while current != 1:
        current = next_term(current)
        sequence.append(current)
    return sequence

def find_longest_sequence(limit):
    """Finds starting point of longest Collatz sequence under limit."""
    table = {}
    n = 2
    best_start, best_length = 0, 0
    while n < limit:
        if n not in table:
            table[n] = 1
            current = n
            while current != 1:
                current = next_term(current)
                if current in table:
                    table[n] += table[current]
                    break
                table[n] += 1
        if table[n] > best_length:
            best_length = table[n]
            best_start = n
        n += 1
    return best_start


class TestMultiples(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(generate_collatz_sequence(1), [1])
        self.assertEqual(generate_collatz_sequence(13), [13, 40, 20, 10, 5,
                                                         16, 8, 4, 2, 1])

if __name__ == "__main__":
    print(find_longest_sequence(1e6))
    unittest.main()
