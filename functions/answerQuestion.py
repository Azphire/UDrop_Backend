from typing import Tuple
from data.remoteData import get_random_questions
from utils.errorCheck import pinyin_is_include
from slotMatching import interruptMatch
interrupt_words = ["不答", "不背", "别问", "结束", "停"]


def start_question() -> Tuple[list, str]:
    questions = get_random_questions()
    return questions, "以下共有五个随机问题，请开始回答。" + questions[0]["question"]


def answer_question(question_list: list, request: str) -> Tuple[bool, list, str]:
    question = question_list[0]
    answer = question["answer"]
    question_list.remove(question)
    is_finished = False
    if not question_list:
        is_finished = True
    if pinyin_is_include(answer, request):
        if is_finished:
            return True, question_list, "回答正确！问答结束。"
        else:
            return False, question_list, "回答正确！" + question_list[0]["question"]
    else:
        if interruptMatch.match(request, interrupt_words):
            return True, [], "问答结束。"
        if is_finished:
            return True, question_list, "正确答案是:" + answer + "。问答结束。"
        else:
            return False, question_list, "正确答案是:" + answer + "。" + question_list[0]["question"]
