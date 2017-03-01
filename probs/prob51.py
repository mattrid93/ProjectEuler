"""Problem ?: ???"""
import unittest
from utils.primes import seive_of_erat

def replace_digits(p, digits):
    """If p contains more than one of the same digit, replace them will all
    other possible digits."""
    if 0 in digits:
        other_digits = [str(d) for d in list(range(1, 10))
                                if str(d) != str(p)[digits[0]]]
    else:
        other_digits = [str(d) for d in list(range(10))
                                if str(d) != str(p)[digits[0]]]
    generated_numbers = []
    p_d = [str(d) for d in str(p)]
    for od in other_digits:
        for d in digits:
            p_d[d] = od
        generated_numbers.append(int("".join(p_d)))
    return generated_numbers


def get_digits(n):
    """Get digits to replace in n"""
    d_tab = {}
    digits = []
    for i, d in enumerate(str(n)):
        if d in d_tab:
            d_tab[d].append(i)
        else:
            d_tab[d] = [i]
    for d, locs in d_tab.items():
        if len(locs) > 1:
            digits.append(locs)
    return digits

def find_family(n, limit=100000):
    """Finds lowest prime in family of n primes, searches up to limit"""
    primes_list = seive_of_erat(limit)
    primes_set = set(primes_list)
    for p in primes_list:
        digits = get_digits(p)
        for d in digits:
            family = replace_digits(p, d)
            if family:
                size = len([m for m in family if m in primes_set])
                if size + 1 == n:
                    return p
    return False

def solution():
    return find_family(8, limit=1000000)

class TestFunction(unittest.TestCase):
    def test_replacer(self):
        self.assertEqual(replace_digits(13, [0]), [23, 33, 43, 53, 63, 73, 83,
                                                   93])
        self.assertEqual(replace_digits(56003, [2, 3]), [56113, 56223, 56333,
                                                         56443, 56553, 56663,
                                                         56773, 56883, 56993])

    def test_digits(self):
        for digits in get_digits(13):
            self.assertIn(digits, [[0], [1]])
        for digits in get_digits(56003):
            self.assertIn(digits, [[0], [1], [2, 3], [4]])

    def test_finder(self):
        self.assertEqual(find_family(7), 56003)

if __name__ == "__main__":
    print(solution())
    unittest.main()
