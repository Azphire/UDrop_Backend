import random
from typing import Tuple

from data.remoteData import get_review_list_titles, get_new_list_titles, get_passage_by_title
from utils.functionList import Function
from slotMatching import interruptMatch

random_words = ["随机", "随便", "都行", "任意"]
interrupt_words = ["停", "不", "终止"]
full_words = ["全文", "全部"]
sentence_words = ["逐句", "一句", "跟背"]


def plan_list(user_id: int, function_value: int) -> dict:
    reply = ''
    if function_value == Function.review.value:
        plans = get_review_list_titles(user_id)
        if plans:
            reply += "你的复习计划有"
            for plan in plans:
                reply += '，' + plan
            reply += '。你可以选择一个篇目进行全文背诵或逐句跟背，或者随机抽取一篇复习。'
        else:
            return {"interrupt": True, "reply": "你今天没有复习计划。"}
    else:
        plans = get_new_list_titles(user_id)
        if plans:
            reply += "你的学习计划有"
            for plan in plans:
                reply += '，' + plan
            reply += '。你可以选择一个篇目进行逐句跟背，或者随机抽取一篇学习。'
        else:
            return {"interrupt": True, "reply": "你今天没有学习计划。"}
    return {"interrupt": False, "reply": reply}


def match_list(user_id: int, match_data: dict, text: str) -> dict:
    if len(match_data) == 1:
        match_data["title"] = ''
        match_data["mode"] = ''
        match_data["interrupt"] = False
    match_data["reply"] = ''

    if match_data["title"] == '':
        if match_data["function_value"] == Function.review.value:
            titles = get_review_list_titles(user_id)
        else:
            titles = get_new_list_titles(user_id)
        for each in titles:
            if '·' not in each:
                if each in text:
                    match_data["title"] = each
                    break
            else:
                title = each.split('·')
                matched = True
                for t in title:
                    if t not in text:
                        matched = False
                        break
                if matched:
                    # 检索到诗名
                    match_data["title"] = each
                    break

    if match_data["title"] == '':
        for word in random_words:
            if word in text:
                match_data["title"] = "random"
                break

    if match_data["mode"] == '':
        for word in full_words:
            if word in text:
                match_data["mode"] = "full"
                break

    if match_data["mode"] == '':
        for word in sentence_words:
            if word in text:
                match_data["mode"] = "sentence"
                break

    if match_data["function_value"] == Function.review.value:
        if match_data["title"] == '':
            match_data["reply"] += "你要复习哪篇文章？"
        if match_data["mode"] == '':
            match_data["reply"] += "全文背诵还是逐句跟背？"
        if match_data["title"] != '' and match_data["mode"] != '':
            if match_data["title"] == 'random':
                match_data["title"] = random_review(user_id)
            passage_category = get_passage_by_title(match_data["title"])["category"]
            if match_data["mode"] == "full":
                if passage_category == 0:
                    match_data["function_value"] = Function.poemFullRecite.value
                else:
                    match_data["function_value"] = Function.passageFullRecite.value
            else:
                if passage_category == 0:
                    match_data["function_value"] = Function.poemSentenceRecite.value
                else:
                    match_data["function_value"] = Function.passageSentenceRecite.value
            return match_data

    if match_data["function_value"] == Function.newLearn.value:
        if match_data["title"] == '':
            match_data["reply"] += "你要学习哪篇文章？"
        else:
            if match_data["title"] == 'random':
                match_data["title"] = random_new(user_id)
            passage_category = get_passage_by_title(match_data["title"])["category"]
            if passage_category == 0:
                match_data["function_value"] = Function.poemSentenceRecite.value
            else:
                match_data["function_value"] = Function.passageSentenceRecite.value
            return match_data

    if interruptMatch.match(text, interrupt_words):
        match_data["interrupt"] = True

    return match_data


def random_review(user_id: int) -> str:
    plans = get_review_list_titles(user_id)
    return random.choice(plans)


def random_new(user_id: int) -> str:
    plans = get_new_list_titles(user_id)
    return random.choice(plans)
