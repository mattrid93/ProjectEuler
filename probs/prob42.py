"""Problem 42: Coded triangle numbers"""
import unittest

def gen_triangle_numbers(limit):
    """Generates triangle numbers less than limit"""
    n = 1
    tris = []
    while 0.5*n*(n + 1) < limit:
        tris.append(int(0.5*n*(n + 1)))
        n += 1
    return tris

def word_to_number(word):
    number = 0
    for char in word:
        number += ord(char) - ord("A") + 1
    return number

def solution():
    with open("inputs/prob42.txt") as f:
        line = f.readline()[1:-1]
        words = line.split('","')
        tris = set(gen_triangle_numbers(350)) # limit based off longest word
        n = 0
        for word in words:
            if word_to_number(word) in tris:
                n += 1
        return n

class TestFunction(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(gen_triangle_numbers(2), [1])
        self.assertEqual(gen_triangle_numbers(56), [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])

    def test_scorer(self):
        self.assertEqual(word_to_number("SKY"), 55)

if __name__ == "__main__":
    print(solution())
    unittest.main()
