import pytest
from reciteWhole import recite_whole
from reciteBySentence import recite_by_sentence
from answerQuestion import answer_question
from playGame import play_game


def test_recite_whole():
    psg_1 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧沙场君莫笑，古来征战几人回?"
    ans_1_1 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧沙场君莫笑，古来征战几人回?"
    ans_1_2 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧疆场君莫笑，古来征战几人回?"
    print(recite_whole(psg_1, ans_1_1))
    print(recite_whole(psg_1, ans_1_2))

def test_recite_by_sentence():
    psg_1 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧沙场君莫笑，古来征战几人回?"
    ans_1_1 = "欲饮琵琶马上催。"
    ans_1_2 = "古来征战几人回。"
    ans_1_3 = "醉卧疆场君莫笑"
    print(recite_by_sentence(psg_1, 1, ans_1_1))
    print(recite_by_sentence(psg_1, 3, ans_1_2))
    print(recite_by_sentence(psg_1, 2, ans_1_3))
    print(recite_by_sentence(psg_1, -1, ''))

def test_answer_question():
    print(answer_question("A", "我选A"))
    print(answer_question("A", "我选B"))

def test_play_game():
    game = {
        "title": "游戏名",
        "endings": [3, 4],
        0: {"content": "叙述0", "choices": {"选项A": 1, "选项B": 2}},
        1: {"content": "叙述1", "choices": {"选项A": 2, "选项B": 3}},
        2: {"content": "叙述2", "choices": {"选项A": 3, "选项B": 4}},
        3: {"content": "结局3"},
        4: {"content": "结局4"}
    }
    print(play_game(game, -1, ''))
    print(play_game(game, 0, '我选择选项B'))
    print(play_game(game, 2, '我选择选项B'))
    print(play_game(game, 2, '我选择选项C'))
    

if __name__ == "__main__":
    # test_recite_whole()
    # test_recite_by_sentence()
    # test_answer_question()
    test_play_game()
