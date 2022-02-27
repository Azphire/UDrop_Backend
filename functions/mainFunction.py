from typing import Tuple
from slotMatching.functionMatch import FunctionMatch
from data.memoryData import get_user_data, set_user_data, remove_user_data
from utils.functionList import Function
from functions.reciteWhole import start_full_reciting, recite_whole
from functions.reciteBySentence import start_sentence_reciting, recite_by_sentence
from functions.playGame import start_play_game, play_game
from functions.answerQuestion import start_question, answer_question

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
    if user_data["function"] == Function.passageFullRecite.value \
            or user_data["function"] == Function.poemFullRecite.value:
        if user_data["start"] == 0:
            passage_id, response = start_full_reciting(user_data["title"], "")
            user_data["start"] = 1
            user_data["passage_id"] = passage_id
            set_user_data(user_id, user_data)
            return False, response
        else:
            res, response = recite_whole(user_data["passage_id"], request)
            remove_user_data(user_id)
            return True, response

    # SentenceRecite
    if user_data["function"] == Function.passageSentenceRecite.value \
            or user_data["function"] == Function.poemSentenceRecite.value \
            or user_data["function"] == Function.authorRecite.value:
        if user_data["start"] == 0:
            if user_data["function"] == Function.passageSentenceRecite.value:
                category = "passage"
            else:
                category = "poem"
            if user_data["function"] == Function.authorRecite.value:
                passage_id = start_sentence_reciting("", user_data["author"], category)
            else:
                passage_id = start_sentence_reciting(user_data["title"], "", category)
            user_data["start"] = 1
            user_data["passage_id"] = passage_id
            user_data["sentence_id"] = -1

        is_finished, sentence_id, response = \
            recite_by_sentence(user_data["passage_id"], user_data["sentence_id"], request)

        if is_finished:
            remove_user_data(user_id)
            return True, response
        else:
            user_data["sentence_id"] = sentence_id
            set_user_data(user_id, user_data)
            return False, response

    # Game
    if user_data["function"] == Function.game.value:
        if user_data["start"] == 0:
            game_id, plot_id = start_play_game()
            user_data["start"] = 1
            user_data["game_id"] = game_id
            user_data["plot_id"] = plot_id
            set_user_data(user_id, user_data)
        is_finished, plot_id, response = play_game(user_data["game_id"], user_data["plot_id"], request)
        if is_finished:
            remove_user_data(user_id)
            return True, response
        else:
            user_data["plot_id"] = plot_id
            set_user_data(user_id, user_data)
            return False, response

    # Question
    if user_data["function"] == Function.question.value:
        if user_data["start"] == 0:
            question_id, response = start_question()
            user_data["start"] = 1
            user_data["question_id"] = question_id
            set_user_data(user_id, user_data)
            return False, response
        else:
            yes, response = answer_question(user_data["question_id"], request)
            remove_user_data(user_id)
            return True, response
