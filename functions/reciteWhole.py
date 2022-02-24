import random
import re
import difflib
from typing import Tuple

# BIAODIAN='，|。|？|！|、|,|\.|?|!'
BIAODIAN='，|。|,|\.|？|\?|！|\!'

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


def recite_whole(passage: str, ans: str) -> Tuple[dict, str]:
    ans=[s for s in re.split(BIAODIAN, ans) if s.strip()!='']
    sentences = [s for s in re.split(BIAODIAN, passage) if s.strip()!='']
    res=getErrMsg(sentences,ans)
    reply=''
    if len(res['-'])==0 and len(res['+'])==0 and len(res['?'])==0:
        reply = reply + "恭喜你，全文背诵正确！"
        return res, reply
    if len(res['?'])>0:
        reply = reply + "背错的部分有："
        for s in res['?']:
            reply = reply + "将："+s[0] + ","
            reply = reply + "背成了："+s[1] + "。"
    if len(res['-'])>0:
        reply = reply + "漏背的部分有："+",".join(res['-']) + "。"
    if len(res['+'])>0:
        reply = reply + "多余的部分有："+",".join(res['+']) + "。"
    return res, reply
