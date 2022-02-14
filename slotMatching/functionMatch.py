from data import *
from enum import Enum, unique


@unique
class Function(Enum):
    choosing = 0
    passageRecite = 1
    poemRecite = 2
    question = 3


class FunctionMatch:
    def __init__(self, text: str):
        self.text = text
        self.function = Function.choosing
        self.detail = ''

    def match(self):
        self.function_match()
        self.detail_match()

    def function_match(self):
        pass

    def detail_match(self):
        pass
