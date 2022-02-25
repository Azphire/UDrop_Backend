from typing import Tuple
from slotMatching.functionMatch import FunctionMatch
from data.memoryData import get_user_data, set_user_data, remove_user_data
from utils.functionList import Function
from functions.reciteWhole import start_reciting, recite_whole


def reply(user_id: int, request: str) -> Tuple[bool, str]:
    # get redis data
    user_data = get_user_data(user_id)

    if user_data is None or user_data["function"] == Function.choosing.value:
        if user_data is None:
            matcher = FunctionMatch(request, {}, {})
        else:
            matcher = FunctionMatch(request, user_data["detail_words"], user_data["function_words"])
        is_matched, user_data, response = matcher.match()
        # matching succeeded, set user data, reload user_data, and go on
        if is_matched:
            user_data["start"] = 0
            set_user_data(user_id, user_data)
        # matching failed, set user data and return reply
        else:
            set_user_data(user_id, user_data)
            return False, response

    # FullRecite
    if user_data["function"] == Function.passageFullRecite.value or user_data["function"] == Function.poemFullRecite.value:
        if user_data["start"] == 0:
            passage_id, response = start_reciting(user_data["title"], "")
            user_data["start"] = 1
            user_data["passage_id"] = passage_id
            set_user_data(user_id, user_data)
            return False, response
        else:
            res, response = recite_whole(user_data["passage_id"], request)
            remove_user_data(user_id)
            return True, response
