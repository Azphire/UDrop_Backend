import unittest
from data.remoteData import *
from slotMatching.textMatch import match


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

    def test_match(self):
        print(match("李白"))


    def test_done_new_plan(self):
        print(done_a_new_plan(2, 483))


if __name__ == '__main__':
    unittest.main()