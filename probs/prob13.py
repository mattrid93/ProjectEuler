"""Problem 13: Large sum.

Directly calculate."""
import unittest

def first_10_digits_of_sum(filename):
    """Calculates first 10 digits of sum of numbers in file."""
    summ = 0
    with open(filename) as f:
        for line in f.readlines():
            summ += int(line[:12])
    return str(summ)[:10]


if __name__ == "__main__":
    filename = "inputs/prob13.txt"
    print(first_10_digits_of_sum(filename))
