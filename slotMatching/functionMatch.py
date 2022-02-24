from data import *
from functionList import Function


class FunctionMatch:
    def __init__(self, text: str, detail_words: dict, function_words: dict):
        self.text = text
        self.function = Function.choosing
        self.detailWords = detail_words
        if function_words == {}:
            self.functionWords = {
                "passage": 0,
                "poem": 0,
                "full": 0,
                "sentence": 0,
                "random": 0,
                "question": 0
            }
        else:
            self.functionWords = function_words
        self.functionWordMatch = {
            "passage": ["课文", "篇目", "文章"],
            "poem": ["诗", "古诗", "诗词"],
            "full": ["全文", "全部"],
            "sentence": ["逐句", "一句", "跟背"],
            "random": ["随机", "随便", "都行", "任意"],
            "question": ["问答", "提问", "问题"]
        }
        self.compose = {
            Function.passageFullRecite: {"propose": False, "title": ""},
            Function.passageSentenceRecite: {"propose": False, "title": ""},
            Function.poemFullRecite: {"propose": False, "title": ""},
            Function.poemSentenceRecite: {"propose": False, "title": ""},
            Function.authorRecite: {"propose": False, "name": ""},
            Function.question: {"propose": False}
        }

        if detail_words != {}:
            self.detail_compose_filling()

    def match(self):
        self.detail_match()
        self.function_match()

    def function_match(self):
        self.function_words_match()
        self.propose_compose()
        pass

    # 指定篇目或作者名词匹配
    def detail_match(self):
        if self.poems_match():
            return True
        if self.passages_match():
            return True
        if self.authors_match():
            return True
        return False

    # 意图合成
    def propose_compose(self):
        # 问答
        if self.functionWords["question"] == 1:
            self.function = Function.question
            return True

        # 作者
        if "author" in self.detailWords.keys():
            self.function = Function.authorRecite
            return True

        # 处理random
        if self.functionWords["random"] == 1:
            self.compose[Function.poemFullRecite]["title"] = "random"
            self.compose[Function.poemSentenceRecite]["title"] = "random"
            self.compose[Function.passageFullRecite]["title"] = "random"
            self.compose[Function.passageSentenceRecite]["title"] = "random"

        # 下面都是背诵，确定课文or诗文、逐句or整篇、题目
        has_title = False
        passage_or_poem = False
        sentence_or_whole = False
        if "poem" in self.detailWords.keys() or "passage" in self.detailWords.keys() or self.functionWords["random"] == 1:
            has_title = True

        # 填充齐全，功能确定

        # 填充不齐全，分别组成询问缺失信息的询问
        pass

    def poems_match(self):
        poems = get_poems()
        for each in poems:
            if self.text.find(each) != -1:
                # 检索到诗名
                self.detailWords["poem"] = each
                return True
        return False

    def passages_match(self):
        passages = get_passages()
        for each in passages:
            if self.text.find(each) != -1:
                # 检索到篇目名
                self.detailWords["passage"] = each
                return True
        return False

    def authors_match(self):
        authors = get_authors()
        for each in authors:
            if self.text.find(each) != -1:
                # 检索到作者名
                self.detailWords["author"] = each
                return True
        return False

    def function_words_match(self):
        for key in self.functionWordMatch:
            for word in self.functionWordMatch[key]:
                if word in self.text:
                    self.functionWords[key] = 1
                    break

    # 把细节匹配到意图合成里
    def detail_compose_filling(self):
        if "poem" in self.detailWords.keys():
            self.compose[Function.poemFullRecite]["title"] = self.detailWords["poem"]
            self.compose[Function.poemSentenceRecite]["title"] = self.detailWords["poem"]
        elif "passage" in self.detailWords.keys():
            self.compose[Function.passageFullRecite]["title"] = self.detailWords["passage"]
            self.compose[Function.passageSentenceRecite]["title"] = self.detailWords["passage"]
        elif "author" in self.detailWords.keys():
            self.compose[Function.authorRecite]["name"] = self.detailWords["author"]
            self.compose[Function.authorRecite]["compose"] = True

