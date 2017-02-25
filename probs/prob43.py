"""Problem 43: Sub string divisibilty"""
import unittest

def next_perm_string(digits):
    """Generate next Lexographic permutation, digits is string"""
    i = -1
    for i_ in range(1, len(digits)):
        if int(digits[i_-1]) < int(digits[i_]):
            i = i_
    if i == -1:
        return False
    suffix = digits[i:]
    prefix = digits[:i-1]
    pivot = digits[i-1]
    j = 0
    for j_ in range(i, len(digits)):
        if int(digits[j_]) > int(pivot):
            j = j_
    suffix = suffix[:j-i] + pivot + suffix[j-i+1:]
    pivot = digits[j]
    new_digits = prefix + pivot + suffix[::-1]
    return new_digits

def property_test(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i, p in enumerate(primes):
        d = int(n[i+1:i+4])
        if d % p:
            return False
    return True

def solution():
    total = 0
    n = "0123456789"
    while next_perm_string(n):
        n = next_perm_string(n)
        if property_test(n):
            total += int(n)
    return total



class TestFunction(unittest.TestCase):
    def test_permuter(self):
        self.assertEqual(next_perm_string("012"), "021")
        self.assertEqual(next_perm_string("021"), "102")
        self.assertEqual(next_perm_string("0123456789"), "0123456798")
        self.assertFalse(next_perm_string("210"))

    def test_property_tester(self):
        self.assertTrue(property_test("1406357289"))
        self.assertFalse(property_test("1406353289"))
        self.assertFalse(property_test("0123456789"))

if __name__ == "__main__":
    print(solution())
    unittest.main()
