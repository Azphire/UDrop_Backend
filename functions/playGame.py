
from typing import Tuple


def play_game(game: dict, plot: int, request: str) -> Tuple[bool, int, str]:
    # 刚开始
    if plot == -1:
        reply = "这个游戏叫做" + game["title"] + "，接下来，你的每一个选择都决定了结局。"
        reply += game[0]["content"]
        return False, 0, reply

    for choice, id in game[plot]["choices"].items():
        if request.find(choice) != -1:
            reply = "你选择了" + choice + "。"
            reply += game[id]["content"]
            if id in game["endings"]:
                return True, -1, reply + "游戏结束。"
            else:
                return False, id, reply
    
    return False, plot, "对不起，我没有听清，请再说一次"
