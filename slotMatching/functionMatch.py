from data.remoteData import *
from utils.functionList import Function
from slotMatching import interruptMatch

interrupt_words = ["不背", "重新", "不选", "结束", "停", "终止"]


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
                "question": 0,
                "recite": 0,
                "game": 0,
                "new": 0,
                "review": 0,
            }
        else:
            self.functionWords = function_words
        self.functionWordMatch = {
            "passage": ["课文", "篇目", "文章"],
            "poem": ["诗", "古诗", "诗词"],
            "full": ["全文", "全部"],
            "sentence": ["逐句", "一句", "跟背"],
            "random": ["随机", "随便", "都行", "任意"],
            "question": ["问答", "提问", "问题"],
            "recite": ["背"],
            "game": ["游戏", "娱乐", "玩"],
            "new": ["学习", "新学"],
            "review": ["复习", "温习"],
        }
        self.compose = {
            Function.passageFullRecite: {"propose": False, "title": ""},
            Function.passageSentenceRecite: {"propose": False, "title": ""},
            Function.poemFullRecite: {"propose": False, "title": ""},
            Function.poemSentenceRecite: {"propose": False, "title": ""},
            Function.authorRecite: {"propose": False, "name": ""},
            Function.question: {"propose": False},
        }

        if detail_words != {}:
            self.detail_compose_filling()

    def match(self):
        self.detail_match()
        return self.function_match()

    def function_match(self):
        self.function_words_match()
        return self.propose_compose()

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
            reply = {
                "function": Function.question.value,
            }
            return True, reply, ""

        # 游戏
        if self.functionWords["game"] == 1:
            reply = {
                "function": Function.game.value,
            }
            return True, reply, ""

        # 作者
        if "author" in self.detailWords.keys():
            reply = {
                "function": Function.authorRecite.value,
                "author": self.detailWords["author"]
            }

            return True, reply, ""

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
        if "poem" in self.detailWords.keys() or "passage" in self.detailWords.keys():
            has_title = True
        if self.functionWords["sentence"] == 1 or self.functionWords["full"] == 1:
            sentence_or_whole = True
        if self.functionWords["passage"] == 1 or self.functionWords["poem"] == 1:
            passage_or_poem = True

        # 填充齐全，功能确定
        if has_title and sentence_or_whole:
            if "poem" in self.detailWords.keys():
                title = self.detailWords["poem"]
                if self.functionWords["sentence"] == 1:
                    func = Function.poemSentenceRecite
                else:
                    func = Function.poemFullRecite
            else:
                title = self.detailWords["passage"]
                if self.functionWords["sentence"] == 1:
                    func = Function.passageSentenceRecite
                else:
                    func = Function.passageFullRecite
            reply = {
                "function": func.value,
                "title": title
            }
            return True, reply, ""

        # random only support for sentence
        if self.functionWords["random"] == 1:
            if self.functionWords["new"] == 1:
                reply = {
                    "function": Function.newLearn.value,
                    "random": 1
                }
                return True, reply, ""
            if self.functionWords["review"] == 1:
                reply = {
                    "function": Function.review.value,
                    "random": 1
                }
                return True, reply, ""
            if passage_or_poem:
                if self.functionWords["passage"] == 1:
                    reply = {
                        "function": Function.passageSentenceRecite.value,
                        "title": "random"
                    }
                    return True, reply, ""
                else:
                    reply = {
                        "function": Function.poemSentenceRecite.value,
                        "title": "random"
                    }
                    return True, reply, ""

        if interruptMatch.match(self.text, interrupt_words):
            return True, {}, "interrupt"

        #  填充不齐全，分别组成询问缺失信息的询问
        reply = {
            "function": Function.choosing.value,
            "detail_words": self.detailWords,
            "function_words": self.functionWords
        }

        if has_title and not sentence_or_whole:
            response = "全文背诵还是逐句背诵呢？"
            return False, reply, response

        # 学习和复习
        if self.functionWords["new"] == 1:
            reply = {
                "function": Function.newLearn.value,
                "random": 0
            }
            return True, reply, ""

        if self.functionWords["review"] == 1:
            reply = {
                "function": Function.review.value,
                "random": 0
            }
            return True, reply, ""

        if self.functionWords["random"] == 1:
            return False, reply, "请问您要背古诗还是课文呢？"

        if not has_title and not sentence_or_whole and not passage_or_poem and self.functionWords["recite"] == 0:
            return False, reply, "你可以选择背书，题目问答，或者游戏。"

        response = ""
        if not has_title:
            if self.functionWords["passage"] == 1:
                response += "要背哪篇课文呢，或者选择随机。"
            elif self.functionWords["poem"] == 1:
                response += "要背哪首诗呢，你也可以指定作者，或者选择随机。"
            else:
                response += "要背什么呢，你可以指定课文、古诗，或者选择随机。"
        return False, reply, response

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
