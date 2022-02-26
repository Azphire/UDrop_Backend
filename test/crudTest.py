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

    def test_update_review_list(self):
        review_list = [{
            "done": 0,
            "title": "离骚"
        },
        {
            "done": 1,
            "title": "桃花源记"
        }]
        update_review_list(2, review_list)

    def test_get_review_list(self):
        print(get_review_list(2))

    def test_update_new_list(self):
        new_list = [
        {
            "done": 1,
            "title": "静夜思"
        },
        {
            "done": 0,
            "title": "出师表"
        },
        {
            "done": 0,
            "title": "蜀道难"
        }
    ]
        update_new_list(2, new_list)

    def test_get_new_list(self):
        print(get_new_list(2))

    def test_get_all_titles(self):
        print(get_all_passage_titles())
        print(get_all_poem_titles())

    def test_get_passages_by_author(self):
        print(get_passages_by_author("王维"))

if __name__ == '__main__':
    unittest.main()
