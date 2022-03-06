import random
import re
import difflib
from typing import Tuple
from data.remoteData import get_poem_by_author, get_passage_by_id, get_passage_by_title
from slotMatching import interruptMatch
from utils.errorCheck import pinyin_is_same, getErrMsg

# BIAODIAN='，|。|？|！|、|,|\.|?|!'
BIAODIAN='，|。|,|\.|？|\?|！|\!'
interrupt_words = ["不背", "结束", "停"]


def start_full_reciting(title: str, author: str) -> Tuple[int, str]:
    reply = "好的，请开始背诵"
    if title != "":
        passage = get_passage_by_title(title)
        passage_id = passage["id"]
        reply += passage["title"]
        return passage_id, reply
    if author != "":
        passage = get_poem_by_author(author)
        passage_id = passage["id"]
        reply += passage["title"]
        return passage_id, reply


def recite_whole(passage_id: int, ans: str) -> Tuple[bool, dict, str]:
    if len(ans) < 10:
        if interruptMatch.match(ans, interrupt_words):
            return True, {}, "好的，背诵结束。"
    passage = get_passage_by_id(passage_id)
    ans = [s for s in re.split(BIAODIAN, ans) if s.strip() != '']
    sentences = [s for s in re.split(BIAODIAN, passage["content"]) if s.strip() != '']
    res = getErrMsg(sentences, ans)
    reply = ''
    if len(res['-']) == 0 and len(res['!']) == 0:
        reply = "恭喜你，全文背诵正确！"
        return True, res, reply
    if len(res['!']) > 0:
        reply = reply + "背错的部分有："
        for s in res['!']:
            reply = reply + "将：" + s[0] + "，"
            reply = reply + "背成了：" + s[1] + "。"
    if len(res['-']) > 0:
        reply = reply + "漏背的部分有："+"，".join(res['-']) + "。"
    reply += "复习计划已更新。"
    return False, res, reply
