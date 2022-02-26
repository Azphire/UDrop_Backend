from data.crud import *
from data.dataParser import *
import unittest


class CRUDTest(unittest.TestCase):
    def test_get_passage_detail(self):
        data = get_passage_detail("出塞")
        passage = Passage(data[0])
        print(passage)

    def test_add_collection(self):
        add_collection(6, "登鹳雀楼")

    def test_get_collection(self):
        print(get_collection(6))

    def test_remove_collection(self):
        remove_collection(6, "出塞")

if __name__ == '__main__':
    unittest.main()
