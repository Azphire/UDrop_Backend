import os

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
        print(get_all_author_names())

    def test_os(self):
        base = os.getcwd()
        path = os.path.join(base, "static", "poems.txt")
        with open(path, 'r') as f:
            data = f.read().split(" ")
        data.pop(0)
        print(data)

    def test_time(self):
        t = datetime.datetime.strptime("2022-02-28", "%Y-%m-%d")
        print(t)
        current = datetime.datetime.today()
        print(current)
        print((current - t).days)

    def test_list(self):
        add_review_item(4, "出塞")

    def test_get_passages_by_author(self):
        print(get_passages_by_author("王维"))

    def test_random_texts(self):
        print(random_texts(3))

    def test_random(self):
        print(get_a_random_poem())
        print(get_a_random_passage())

    def test_get_passage(self):
        print(get_passage(5))

    def test_get_a_game(self):
        game_id = get_a_random_game_id()
        print(game_id)
        print(get_game(game_id))

    def test_question(self):
        question = get_a_random_question()
        print(question)
        print(get_answer(question["question_id"]))

    def test_check(self):
        print(check_collection(3, "静夜思"))


if __name__ == '__main__':
    unittest.main()
