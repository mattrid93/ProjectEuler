"""Problem 26: Reciprocal cycles"""
import unittest

def divider(d):
    """Return decimal fraction of 1/d in array form."""
    carry = 10
    df = []
    while carry:
        if carry < d:
            carry *= 10
            df.append(0)
        else:
            df.append(carry // d)
            carry = (carry % d)*10
    return df

def recurring(d):
    """Return recurring part of decimal fraction of 1/d in array form"""
    carry = 10
    i = 0
    carry_tab = {}
    df = []
    while carry and carry not in carry_tab:
        carry_tab[carry] = i
        if carry < d:
            carry *= 10
            df.append(0)
        else:
            df.append(carry // d)
            carry = (carry % d)*10
        i += 1
    if not carry:
        return False
    return df[carry_tab[carry]:]

def solution():
    """Find d < 1000 for which 1/d has longest recurring cycle in decimal"""
    best_len = 0
    best_d = 0
    for d in range(2, 1000):
        rec = recurring(d)
        if rec:
            if len(rec) > best_len:
                best_len = len(rec)
                best_d = d
    return best_d


class TestFunction(unittest.TestCase):
    def test_divider(self):
        self.assertEqual(divider(2), [5])
        self.assertEqual(divider(4), [2, 5])
        self.assertEqual(divider(10), [1])

    def test_recurring(self):
        self.assertFalse(recurring(2))
        self.assertFalse(recurring(5))
        self.assertFalse(recurring(10))
        self.assertEqual(recurring(3), [3])
        self.assertEqual(recurring(6), [6])
        self.assertEqual(recurring(6), [6])
        self.assertEqual(recurring(7), [1, 4, 2, 8, 5, 7])
        self.assertEqual(recurring(9), [1])

if __name__ == "__main__":
    print(solution())
    unittest.main()
