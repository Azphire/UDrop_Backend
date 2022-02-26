import unittest
from data.remoteData import *


class MyTestCase(unittest.TestCase):
    def test_authors(self):
        print(get_authors())

    def test_random(self):
        print(get_poem_by_author("李白"))


if __name__ == '__main__':
    unittest.main()