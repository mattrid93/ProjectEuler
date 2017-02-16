"""Problem 18: Maximum path sum I.

Dijsktra's algorithm"""
import unittest

class Node:
    def __init__(self, weight):
        self.weight = weight
        self.children = []
        self.dist = None
        self.prev = None

    def add_child(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, headnode):
        self.headnode = headnode

    def calc_max_path_sum(self):
        

    def _calc_max_path_sum(self):
        # depth first search to generate dicts
        S, V = [], []
        dist = {}
        prev = {}
        S.insert(0, self.headnode)
        while S != []:
            v = S.pop(0)
            if v not in V:
                v.dist = 0
                V.append(v)
                for c in v.children:
                    S.insert(0, c)
        # Dijsktra's algorithm
        source = Node(0)
        source.children.append(self.headnode)
        source.dist = 0
        V.insert(0, source)
        while V:
            print([n.dist for n in V])
            u = V.pop(0)
            if not u.children:
                max_sum = 0
                while u.prev:
                    u = u.prev
                    max_sum += u.weight
                return -max_sum
            for v in u.children:
                if v in V:
                    alt = u.dist + v.weight
                    if alt < v.dist:
                        v.dist = alt
                        v.prev = u
            V.sort(key=lambda n: n.dist)
        return False



def tree_parser(filename):
    """Parses file and returns connected tree"""
    with open(filename) as f:
        hn_weight = int(f.readline())
        headnode = Node(hn_weight)
        tree = Tree(headnode)
        upper_layer = [headnode]
        for line in f.readlines():
            weights = [-int(x) for x in line.split()]
            current_layer = [Node(x) for x in weights]
            for i, node in enumerate(current_layer[:-1]):
                upper_layer[i].add_child(node)
            for i, node in enumerate(current_layer[1:]):
                upper_layer[i].add_child(node)
            upper_layer = current_layer
        target = Node(0)
        target.dist = 0
        for n in upper_layer:
            n.children.append(target)
        return tree


class TestFunctions(unittest.TestCase):
    def test_max_path(self):
        tree = tree_parser("inputs/prob18_test.txt")
        self.assertEqual(tree.calc_max_path_sum(), 23)
        tree = tree_parser("inputs/prob18_test2.txt")
        self.assertEqual(tree.calc_max_path_sum(), 308)

if __name__ == "__main__":
    tree = tree_parser("inputs/prob18.txt")
    print(tree.calc_max_path_sum())
    unittest.main()
