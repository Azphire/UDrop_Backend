from typing import Tuple
from data.remoteData import get_game_by_id, get_random_game

def start_play_game() -> Tuple[int, int]:
    game_id = get_random_game()
    return game_id, -1

def play_game(game_id: int, plot: int, request: str) -> Tuple[bool, int, str]:
    game = get_game_by_id(game_id)
    # 刚开始
    if plot == -1:
        reply = "这个游戏叫做" + game["title"] + "，接下来，你的每一个选择都决定了结局。"
        reply += game["0"]["content"]
        return False, 0, reply

    for choice, plot_id in game[str(plot)]["choices"].items():
        if request.find(choice) != -1:
            reply = "你选择了" + choice + "。"
            reply += game[str(plot_id)]["content"]
            if plot_id in game["endings"]:
                return True, -1, reply + "游戏结束。"
            else:
                return False, plot_id, reply
    
    return False, plot, "对不起，我没有听清，请再说一次"
