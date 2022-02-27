import unittest
from data.remoteData import *


class MyTestCase(unittest.TestCase):
    def test_authors(self):
        print(get_authors())

    def test_random(self):
        print(get_poem_by_author("李白"))

    def test_static(self):
        with open('../static/authors.txt', 'r') as f:
            data = f.read().split(" ")
            data.pop(0)
            print(data)



if __name__ == '__main__':
    unittest.main()