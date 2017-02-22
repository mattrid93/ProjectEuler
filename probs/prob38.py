"""Problem 38: Pandigital multiples"""
import unittest

def is_pandigital(n):
    """Tests if n is a 1-9 pandigital"""
    if len(str(n)) != 9:
        return False
    if "0" in str(n):
        return False
    return len(str(n)) == len(set(str(n)))

def multiply_by_1_m(n):
    """Returns concatenated product of n with 1-m (until digits > 8)"""
    conc_product = ""
    i = 1
    while len(conc_product) < 9:
        conc_product += str(n*i)
        i += 1
    return int(conc_product)

def solution():
    largest = 0
    for n in range(10000):
        prod = multiply_by_1_m(n)
        if is_pandigital(prod) and prod > largest:
            largest = prod
    return largest

class TestFunction(unittest.TestCase):
    def test_tester(self):
        self.assertTrue(is_pandigital(192384576))
        self.assertTrue(is_pandigital(918273645))
        self.assertFalse(is_pandigital(192384575))
        self.assertFalse(is_pandigital(19236))

    def test_multiplier(self):
        self.assertEqual(multiply_by_1_m(192), 192384576)
        self.assertEqual(multiply_by_1_m(9), 918273645)

if __name__ == "__main__":
    print(solution())
    unittest.main()
