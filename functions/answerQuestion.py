from typing import Tuple
from data.remoteData import get_answer, get_question_random


def start_question() -> Tuple[int, str]:
    question = get_question_random()
    return question["question_id"], question["question"]


def answer_question(question_id: int, request: str) -> Tuple[bool, str]:
    answer = get_answer(question_id)
    if request.find(answer) != -1:
        return True, "回答正确！"
    else:
        return False, "正确答案是:" +answer
