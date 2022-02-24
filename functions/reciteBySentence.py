import random
import re
from typing import Tuple


BIAODIAN='，|。|,|\.|？|\?|！|\!'

# param: 文章，句子编号（尚未开始背则编号为-1），背诵内容
# return: 是否已结束，下一句编号，回答内容
def recite_by_sentence(passage: str, sentence_num: int, ans: str) -> Tuple[bool, int, str]:
    
    sentences = [s for s in re.split(BIAODIAN, passage) if s.strip()!='']
    
    # 还没开始
    if sentence_num == -1:
        reply = '请开始逐句背诵：' + sentences[0]
        return False, 0, reply
    
    total = len(sentences)
    ans = ans.replace('。','')
    
    # 背诵正确
    if sentences[sentence_num] in ans:
        # 背完了
        if sentence_num == total - 1: 
            reply = '恭喜你，背诵完成！'
            return True, -1, reply
        else:
            reply = sentences[sentence_num + 1]
            return False, sentence_num + 1, reply
    
    # 背诵有误
    else:
        reply = '再试一遍：' + sentences[sentence_num]
        return False, sentence_num, reply
