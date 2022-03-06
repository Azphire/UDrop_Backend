import pypinyin
import difflib


def getErrMsg(text1, text2):
    m = {'-': [], '!': []}
    pinyin1 = ["".join(pypinyin.lazy_pinyin(text))for text in text1]
    pinyin2 = ["".join(pypinyin.lazy_pinyin(text)) for text in text2]
    diff_list = list(difflib.context_diff(pinyin1, pinyin2))
    if diff_list:
        pinyin_list = diff_list[4:]
        for value in pinyin_list:
            if '---' in value:
                break
            if value[0] == ' ':
                continue
            if value[0] == '!':
                m["!"].append(text1[pinyin1.index(value[2:])])
            elif value[0] == '-':
                m["-"].append(text1[pinyin1.index(value[2:])])
    return m


def pinyin_is_include(short_text: str, long_text:str) -> bool:
    short_pinyin = "".join(pypinyin.lazy_pinyin(short_text))
    long_pinyin = "".join(pypinyin.lazy_pinyin(long_text))
    if short_pinyin in long_pinyin:
        return True
    else:
        return False


def pinyin_is_same(short_text: str, long_text:str) -> bool:
    short_pinyin = "".join(pypinyin.lazy_pinyin(short_text))
    long_pinyin = "".join(pypinyin.lazy_pinyin(long_text))
    if short_pinyin == long_pinyin:
        return True
    else:
        return False
