import random
import re
import difflib
from typing import Tuple
from data.remoteData import get_poem_by_author, get_passage_by_id, get_passage_by_title
from slotMatching import interruptMatch

# BIAODIAN='，|。|？|！|、|,|\.|?|!'
BIAODIAN='，|。|,|\.|？|\?|！|\!'
interrupt_words = ["不背", "结束", "停"]


def getErrMsg(text1, text2):
    m={'-':[],'+':[],'?':[]}
    diff = difflib.Differ()
    d = list(diff.compare(text1, text2))
    i=0
    size=len(d)
    while i<size:
        tag=False
        c=d[i][0]
        if c in ['+','-']:
            if i+1<size and d[i+1][0]=='?':
                tag=True
            else:
                m[c].append(d[i][2:])
        if tag:
            m['?'].append((d[i][2:],d[i+2][2:]))
            i+=4
        else:
            i+=1
    return m


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
    res = getErrMsg(sentences,ans)
    reply = ''
    if len(res['-'])==0 and len(res['+'])==0 and len(res['?'])==0:
        reply = reply + "恭喜你，全文背诵正确！"
        return True, res, reply
    if len(res['?'])>0:
        reply = reply + "背错的部分有："
        for s in res['?']:
            reply = reply + "将："+s[0] + ","
            reply = reply + "背成了："+s[1] + "。"
    if len(res['-'])>0:
        reply = reply + "漏背的部分有："+",".join(res['-']) + "。"
    if len(res['+'])>0:
        reply = reply + "多余的部分有："+",".join(res['+']) + "。"
    reply += "复习计划已更新。"
    return False, res, reply
