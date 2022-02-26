from functions.reciteWhole import recite_whole
from functions.reciteBySentence import recite_by_sentence
from functions.answerQuestion import answer_question
from functions.playGame import play_game
from mainFunction import reply
from data.memoryData import set_user_data, get_user_data
from utils.functionList import Function
import unittest

class MyTestCase(unittest.TestCase):
    def test_recite_whole(self):
        psg_1 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧沙场君莫笑，古来征战几人回?"
        ans_1_1 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧沙场君莫笑，古来征战几人回?"
        ans_1_2 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧疆场君莫笑，古来征战几人回?"
        print(recite_whole(1, ans_1_1))
        print(recite_whole(1, ans_1_2))

    def test_recite_by_sentence(self):
        psg_1 = "葡萄美酒夜光杯，欲饮琵琶马上催!醉卧沙场君莫笑，古来征战几人回?"
        ans_1_1 = "欲饮琵琶马上催。"
        ans_1_2 = "古来征战几人回。"
        ans_1_3 = "醉卧疆场君莫笑"
        print(recite_by_sentence(psg_1, 1, ans_1_1))
        print(recite_by_sentence(psg_1, 3, ans_1_2))
        print(recite_by_sentence(psg_1, 2, ans_1_3))
        print(recite_by_sentence(psg_1, -1, ''))

    def test_answer_question(self):
        print(answer_question("A", "我选A"))
        print(answer_question("A", "我选B"))

    def test_play_game(self):
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


    def test_main_function_1(self):
        set_user_data(9, {"function": Function.passageFullRecite.value, "title": "登鹳雀楼", "start": 0})
        print(reply(9, ""))
        print(get_user_data(9))
        print(reply(9, "白日依山尽，黄河入海流。欲穷千，更上一层楼。"))
        print(get_user_data(9))


    def test_main_function_2(self):
        print(reply(9, "我要背诗"))
        print(get_user_data(9))
        print(reply(9, "登鹳雀楼"))
        print(get_user_data(9))
        print(reply(9, "全文"))
        print(get_user_data(9))
        print(reply(9, "白日依山尽，黄河入海流。欲穷千，更上一层楼。"))
        print(get_user_data(9))


    def test_main_function_3(self):
        print(reply(9, "我要背诗"))
        print(get_user_data(9))
        print(reply(9, "登鹳雀楼"))
        print(get_user_data(9))
        print(reply(9, "逐句"))
        print(get_user_data(9))
        print(reply(9, "白日依山尽。"))
        print(get_user_data(9))
        print(reply(9, "黄河入海流。"))
        print(get_user_data(9))
        print(reply(9, "欲穷千"))
        print(get_user_data(9))
        print(reply(9, "欲穷千里目。"))
        print(get_user_data(9))
        print(reply(9, "更上一层楼。"))
        print(get_user_data(9))

if __name__ == '__main__':
    unittest.main()