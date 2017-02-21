"""Problem 34: Digit factorials"""
import unittest

def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = n
    while n > 1:
        n = n-1
        fact *= n
    return fact

def solution():
    total = 0
    for i in range(3, 100000): # limit found by trial and error
        digits = [int(d) for d in str(i)]
        if i == sum([factorial(d) for d in digits]):
            total += i
    return total


class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
