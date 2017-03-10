"""Problem 59: XOR decryption"""
import unittest

def file_reader(filename):
    with open(filename) as f:
        data = [int(d) for d in f.readline().split(",")]
        return data

def decrypter(data, key):
    while len(key) < len(data):
        key += key
    key = key[:len(data)]
    decrypted = []
    for d, k in zip(data, key):
        decrypted.append(d ^ k)
    return decrypted

def convert_to_words(data):
    return "".join([chr(d) for d in data])

def solution():
    data = file_reader("inputs/prob59.txt")
    keys = [[a, b, c] for a in range(97, 123)
                      for b in range(97, 123)
                      for c in range(97, 123)]
    for key in keys:
        decrypted = decrypter(data, key.copy())
        english = convert_to_words(decrypted)
        if "beginning" in english:
            print(key, english)
            return sum(decrypted)


class TestFunction(unittest.TestCase):
    def test_decrypter(self):
        self.assertEqual(decrypter(
                         decrypter([1, 2, 3, 4, 5, 6, 7], [1, 2, 3]),
                            [1, 2, 3]),
                         [1, 2, 3, 4, 5, 6, 7])

    def test_converter(self):
        self.assertEqual(convert_to_words([ord(c) for c in "hello"]), "hello")

if __name__ == "__main__":
    print(solution())
    unittest.main()
