import json
from connection.mysqlConnector import execute


passages = [
    "岳阳楼记", "桃花源记", "出师表"
]

poems = [
    "登鹳雀楼", "登高", "静夜思"
]

authors = [
    "李白", "杜甫", "白居易"
]

passage = {
        "id": 1,
        "title": "登鹳雀楼",
        "author": "王之涣",
        "content": "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"
    }


def get_passages() -> list:
    return passages


def get_poems() -> list:
    return poems


def get_authors() -> list:
    return authors


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
    return passage


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
