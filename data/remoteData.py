import json
import random
from data.crud import get_all_author_names, get_all_passage_titles, get_all_poem_titles, \
    get_passage_detail, get_passage, get_a_random_passage, get_a_random_poem, get_passages_by_author, \
    get_game, get_a_random_game_id, get_a_random_question, get_answer, add_review_item


def get_passages() -> list:
    return get_all_passage_titles()


def get_poems() -> list:
    return get_all_poem_titles()


def get_authors() -> list:
    return get_all_author_names()


def get_passage_by_id(passage_id: int) -> dict:
    return get_passage(passage_id)


def get_passage_random() -> dict:
    return get_a_random_passage()


def get_poem_random() -> dict:
    return get_a_random_poem()


def get_poem_by_author(author: str) -> dict:
    poems = get_passages_by_author(author)
    return random.choice(poems)


def get_passage_by_title(title: str) -> dict:
    passage = get_passage_detail(title)
    return passage.to_dict()


def get_game_by_id(game_id: int) -> dict:
    return get_game(game_id)


def get_random_game() -> int:
    return get_a_random_game_id()


def get_question_random() -> dict:
    return get_a_random_question()


def get_answer_by_id(question_id: int) -> str:
    return get_answer(question_id)


def add_review(user_id: int, title: str):
    add_review_item(user_id, title)
