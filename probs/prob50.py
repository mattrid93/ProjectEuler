"""Problem 50: Consequetive prime sum."""
import unittest
from utils.primes import seive_of_erat

def solution():
    limit = 1000000
    primes_list = seive_of_erat(limit)
    primes_set = set(primes_list)
    best = (0, 0)
    for i, pstart in enumerate(primes_list):
        running_sum = pstart
        point = i
        while running_sum < limit and point < len(primes_list) - 1:
            point += 1
            running_sum += primes_list[point]
            if running_sum in primes_set and point - i + 1> best[1]:
                best = (running_sum, point - i + 1)
    return best[0]



class TestFunction(unittest.TestCase):
    pass

if __name__ == "__main__":
    print(solution())
    unittest.main()
