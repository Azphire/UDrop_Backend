# 结束会话语义识别

def match(text: str, interrupt_words: list) -> bool:
    for word in interrupt_words:
        if word in text:
            return True
        else:
            return False
