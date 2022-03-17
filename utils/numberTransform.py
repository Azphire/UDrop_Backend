import re

num = input()
num = str(num)
w = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
n = ['千', '百', '十', '', '千', '百', '十', '']


def trans(num):
    lengt = len(num)
    if lengt > 8:
        return ""
    return_str = ''
    islastIsEro = False
    i = 0
    while i < lengt:
        # print(num[i])
        tmp = int(num[i])
        if tmp == 0:
            if islastIsEro != True:
                return_str += w[tmp]
                # str+=n[8-lengt+i]
                islastIsEro = True
            if lengt - i == 5:
                if islastIsEro == True:
                    return_str = return_str[:-1]
                return_str += '万'
        else:
            return_str += w[tmp]
            return_str += n[8 - lengt + i]
            islastIsEro = False
            if lengt - i == 5:
                if islastIsEro == True:
                    return_str = return_str[:-1]
                return_str += '万'

        i += 1
    if return_str[-1] == w[0]:
        return_str = return_str[:-1]
    if return_str[0:2] == "一十":
        return_str = return_str[1:]
    return return_str


def replace_num(text: str) -> str:
    num_list = re.findall('\d+', text)
    for num in num_list:
        char = trans(num)
        text = text.replace(num, char)
    return text
