import json
from data.crud import get_all_author_names, get_all_passage_titles, get_all_poem_titles, get_passage_detail


passage = {
        "id": 1,
        "title": "登鹳雀楼",
        "author": "王之涣",
        "content": "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"
    }


def get_passages() -> list:
    return get_all_passage_titles()


def get_poems() -> list:
    return get_all_poem_titles()


def get_authors() -> list:
    return get_all_author_names()


def get_passage_by_id(passage_id: int) -> dict:
    print(passage_id)
    return passage


def get_passage_random() -> dict:
    return passage


def get_poem_random() -> dict:
    return passage


def get_poem_by_author(author: str) -> dict:
    return passage


def get_passage_by_title(title: str) -> dict:
    passage = get_passage_detail(title)
    return passage.to_dict()


def get_game_random() -> dict:
    game = {
        "title": "游戏名",
        "endings": [3, 4],
        0: {"content": "叙述0", "choices": {"选项A": 1, "选项B": 2}},
        1: {"content": "叙述1", "choices": {"选项A": 2, "选项B": 3}},
        2: {"content": "叙述2", "choices": {"选项A": 3, "选项B": 4}},
        3: {"content": "结局3"},
        4: {"content": "结局4"}
    }
    return game


def get_question_random() -> dict:
    question = {
        "content": "9-4=",
        "answer": "6"
    }
    return question


def get_game_by_id() -> dict:
    game = {
        "title": "游戏名",
        "endings": [3, 4],
        0: {"content": "叙述0", "choices": {"选项A": 1, "选项B": 2}},
        1: {"content": "叙述1", "choices": {"选项A": 2, "选项B": 3}},
        2: {"content": "叙述2", "choices": {"选项A": 3, "选项B": 4}},
        3: {"content": "结局3"},
        4: {"content": "结局4"}
    }
    return game


def get_question_by_id() -> dict:
    question = {
        "content": "9-4=",
        "answer": "6"
    }
    return question
