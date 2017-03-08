"""Problem 57: Square root convergents"""
import unittest

def square_root_iterations(num, denom):
    """Returns next numerator and denominator is series"""
    num += denom
    num, denom = denom, num
    num += denom
    return num, denom

def series_generator(n):
    """Return n terms in series"""
    count = 0
    num, denom = 3, 2
    while count < n:
        yield num, denom
        num, denom = square_root_iterations(num, denom)
        count += 1

def solution():
    count = 0
    for num, denom in series_generator(1000):
        if len(str(num)) > len(str(denom)):
            count += 1
    return count

class TestFunction(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(square_root_iterations(3, 2), (7, 5))
        self.assertEqual(square_root_iterations(7, 5), (17, 12))
        self.assertEqual(square_root_iterations(17, 12), (41, 29))

if __name__ == "__main__":
    print(solution())
    unittest.main()
