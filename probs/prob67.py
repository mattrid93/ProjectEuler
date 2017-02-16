"""Problem 67: Maximum path sum II.

Dynamic programming"""
import unittest

def file_reader(filename):
    with open(filename) as f:
        tree = []
        for line in f.readlines():
            weights = [int(x) for x in line.split()]
            tree.append(weights)
        return tree

def path_finder(tree):
    paths = []
    for row in tree:
        paths.append([0]*len(row))
    paths[0][0] = tree[0][0]
    for i in range(1, len(tree)):
        for j in range(len(tree[i])-1):
            paths[i][j] = tree[i][j] + paths[i-1][j]
        for j in range(1, len(tree[i])):
            paths[i][j] = max(paths[i][j], tree[i][j] + paths[i-1][j-1])
    return max(paths[-1])

class TestFunctions(unittest.TestCase):
    def test_file_reader(self):
        self.assertEqual(file_reader("inputs/prob18_test.txt"), [[3], [7, 4],
                                                                 [2, 4, 6],
                                                                 [8, 5, 9, 3]])

    def test_path_finder(self):
        tree = file_reader("inputs/prob18_test.txt")
        self.assertEqual(path_finder(tree), 23)
        tree = file_reader("inputs/prob18_test2.txt")
        self.assertEqual(path_finder(tree), 308)


if __name__ == "__main__":
    tree = file_reader("inputs/prob67.txt")
    print(path_finder(tree))
    unittest.main()
