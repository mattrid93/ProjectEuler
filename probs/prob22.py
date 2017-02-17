"""Problem 22: Name scores.

Trivial in Python"""
import unittest

def read_names(filename):
    with open(filename) as f:
        line = f.readline()
        names = line.split('","')
        # strip off missed "
        names[0] = names[0][1:]
        names[-1] = names[-1][:-1]
        return names

def name_score(name):
    score = 0
    name = name.lower()
    for char in name:
        score += ord(char) - 96
    return score

def score_list(lst):
    lst.sort()
    score = 0
    for i, name in enumerate(lst):
        score += (i+1)*name_score(name)
    return score

def solution():
    names = read_names("inputs/prob22.txt")
    return score_list(names)

class TestFunction(unittest.TestCase):
    def test_scorer(self):
        self.assertEqual(name_score("COLIN"), 53)

if __name__ == "__main__":
    print(solution())
    unittest.main()
