"""Problem 31: Coin sums.

Dynamic programming."""
import unittest

def number_of_ways(amount):
    """Returns number of ways to make given amount (pence) using british
    coins."""
    coins = {
        1: 1,
        2: 2,
        3: 5,
        4: 10,
        5: 20,
        6: 50,
        7: 100,
        8: 200,
    }
    m = {} # m[i, j] is ways to make j using at least one coin i
    for i in range(len(coins)+1):
        m[(i, 0)] = 0
    for j in range(amount+1):
        m[(0, j)] = 0
    for i in range(1, len(coins)+1):
        for j in range(amount+1):
            if coins[i] < j:
                m[(i, j)] = sum([m[(x, j-coins[i])] for x in range(i)]) + m[(i, j-coins[i])]
            elif coins[i] == j:
                m[(i, j)] = 1
            else:
                m[(i, j)] = 0
    return sum([m[(i, amount)] for i in range(len(coins)+1)])

def solution():
    return number_of_ways(200)

class TestFunction(unittest.TestCase):
    def test_number_of_ways(self):
        self.assertEqual(number_of_ways(3), 2)
        self.assertEqual(number_of_ways(5), 4)
        self.assertEqual(number_of_ways(7), 6)

if __name__ == "__main__":
    print(solution())
    unittest.main()
