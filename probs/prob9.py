"""Problem 9: Special Pythagorean triplet.

Brute force."""
import unittest

def find_triple(s):
    """Returns abc where a^2+b^2=c^2 with a+b+c=s."""
    a, b, c = 998, 1, 1
    while b < 999:
        if a**2 + b**2 == c**2:
            return a*b*c
        if a == 1:
            c += 1
            b = 1
            a = 1000 - b - c
        else:
            b += 1
            a -= 1

if __name__ == "__main__":
    print(find_triple(1000))
