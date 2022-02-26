import unittest
from data.remoteData import *


class MyTestCase(unittest.TestCase):
    def test_authors(self):
        print(get_authors())


if __name__ == '__main__':
    unittest.main()