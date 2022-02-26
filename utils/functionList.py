from enum import Enum, unique


@unique
class Function(Enum):
    choosing = 0
    passageFullRecite = 1
    passageSentenceRecite = 2
    poemFullRecite = 3
    poemSentenceRecite = 4
    authorRecite = 5
    question = 6
    game = 7
