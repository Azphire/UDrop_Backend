import random
import re
from typing import Tuple
from data.remoteData import get_poem_random, get_passage_random, get_passage_by_id, get_passage_by_title, get_poem_by_author
from slotMatching import interruptMatch
from utils.errorCheck import getErrMsg, pinyin_is_same


ALL_POINT = '，|。|,|\.|？|\?|！|\!'
FULL_POINT = '。|\.|？|\?|！|\!'
COMMA = '，|,'
interrupt_words = ["不背", "结束", "停"]


def start_sentence_reciting(title: str, author: str, category: str) -> Tuple[int, str]:
    if title != "":
        if title == "random":
            if category == "poem":
                passage = get_poem_random()
            else:
                passage = get_passage_random()
        else:
            passage = get_passage_by_title(title)
    if author != "":
        passage = get_poem_by_author(author)
    passage_id = passage["id"]
    return passage_id


# param: 文章，句子编号（尚未开始背则编号为-1），背诵内容
# return: 是否已结束，下一句编号，回答内容
def recite_by_sentence(passage_id: int, sentence_num: int, text: str) -> Tuple[bool, int, str]:
    passage = get_passage_by_id(passage_id)
    sentences = [s for s in re.split(FULL_POINT, passage["content"]) if s.strip() != '']
    
    # 还没开始
    if sentence_num == -1:
        reply = "好的，请开始背诵。"
        reply += passage["title"] + "，" + passage["dynasty"] + "，" + passage["author"] + "。"
        reply += sentences[0]
        return False, 0, reply
    
    total = len(sentences)
    ans = [s for s in re.split(ALL_POINT, text) if s.strip() != '']
    sentence = [s for s in re.split(COMMA, sentences[sentence_num]) if s.strip() != '']
    res = getErrMsg(sentence, ans)

    # 背诵正确
    if len(res['-']) == 0 and len(res['!']) == 0:
        # 背完了
        if sentence_num == total - 1: 
            reply = '恭喜你，背诵完成！'
            return True, -1, reply
        else:
            reply = sentences[sentence_num + 1]
            return False, sentence_num + 1, reply
    
    # 背诵有误或者中断
    else:
        if interruptMatch.match(text, interrupt_words):
            return True, -1, "好的，背诵结束。"
        else:
            reply = '再试一次：' + sentences[sentence_num]
            return False, sentence_num, reply
