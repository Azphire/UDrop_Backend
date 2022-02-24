from typing import Tuple


def answer_question(answer: str, request: str) -> Tuple[bool, str]:
    if request.find(answer) != -1:
        return True, "回答正确！"
    else:
        return False, "正确答案是:" +answer
