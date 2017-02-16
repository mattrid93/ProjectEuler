"""Problem 17: Number letter counts.

Directly sum"""
import unittest

units = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "one thousand",
}

def converter(i):
    """Converts number i to words"""
    if i < 21 or i == 1000:
        return units[i]
    if i < 100:
        return units[i//10*10] + " " + units[i%10]
    if not i%100:
        return units[i//100] + " " + "hundred"
    if i%100 < 21:
        return units[i//100] + " " + "hundred and " + units[i%100]
    return units[i//100] + " " + "hundred and " + units[(i%100)//10 * 10] + " " + units[i%10]

def counter(n):
    """Counts letters used in writing numbers 1-n."""
    total = 0
    for i in range(1, n+1):
        words = converter(i)
        total += len(words.replace(" ", ""))
    return total


class TestMultiples(unittest.TestCase):
    def test_converter(self):
        self.assertEqual(converter(1), "one")
        self.assertEqual(converter(7), "seven")
        self.assertEqual(converter(11), "eleven")
        self.assertEqual(converter(101), "one hundred and one")
        self.assertEqual(converter(576), "five hundred and seventy six")
        self.assertEqual(converter(1000), "one thousand")

    def test_counter(self):
        self.assertEqual(counter(5), 19)

if __name__ == "__main__":
    print(counter(1000))
    unittest.main()
