from connection import mysqlConnector
from data.dataParser import *
import json
import datetime
from typing import Tuple


def get_password_by_name(name: str):
    sql = "SELECT userId, password FROM User WHERE name=%s"
    data = mysqlConnector.execute(sql, name)
    return data


def check_user_name(name: str) -> bool:
    sql = "SELECT userId FROM User WHERE name =%s"
    data = mysqlConnector.execute(sql, name)
    if len(data) > 0:
        return True
    else:
        return False


def add_user(name: str, password: str) -> dict:
    sql = "INSERT INTO User (name, password) VALUES (%s,%s)"
    param = (name, password)
    mysqlConnector.execute(sql, param)
    sql = "SELECT userId FROM User WHERE name =%s"
    data = mysqlConnector.execute(sql, name)
    return_dict = {"user_id": None, "added": 0}
    if data:
        return_dict["user_id"] = int(data[0][0])
        return_dict["added"] = 1


def get_user_detail(user_id: int) -> dict:
    sql = "SELECT * FROM User WHERE userId=" + str(user_id)
    data = mysqlConnector.execute(sql)[0]
    if data:
        info = User(data)
        return_json = {
            "user_name": info.name,
            "user_motto": info.motto,
            "learned_days": info.learnedDays
        }
        return return_json


def edit_user_detail(user_id: int, name: str, motto: str) -> bool:
    sql = "UPDATE User SET name=%s, motto=%s WHERE userId =" + str(user_id)
    param = (name, motto)
    try:
        mysqlConnector.execute(sql, param)
        return True
    except:
        return False





def get_passage_detail(title: str) -> Passage:
    sql = "SELECT * FROM CHNPassage natural join CHNAuthor WHERE title=%s"
    data = mysqlConnector.execute(sql, title)
    passage = Passage(data[0])
    return passage


def get_collection(user_id: int) -> list:
    sql = "SELECT collection FROM Collection WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        collection_list = []
        collections = json.loads(str(data[0][0]))
        for passage_id, collected_time in collections.items():
            sql = "SELECT * FROM CHNPassage natural join CHNAuthor WHERE CHNPassageId=%s"
            data = mysqlConnector.execute(sql, passage_id)
            passage = Passage(data[0]).to_dict()
            passage["collected_time"] = collected_time
            collection_list.append(passage)
        return collection_list
    else:
        return []


def check_collection(user_id: int, title: str) -> bool:
    sql = "SELECT collection FROM Collection WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        collections = json.loads(str(data[0][0]))
        passage_id = get_passage_detail(title).passageId
        if str(passage_id) in collections.keys():
            return True
        else:
            return False


def add_collection(user_id: int, title: str):
    passage = get_passage_detail(title)
    collected_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sql = "SELECT collection FROM Collection WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        collections = json.loads(data[0][0])
        if str(passage.passageId) in collections.keys():
            return False
        else:
            collections[str(passage.passageId)] = collected_time
            sql = "UPDATE Collection SET collection=%s WHERE userId=%s"
            mysqlConnector.execute(sql, (json.dumps(collections), user_id))
            return True
    else:
        sql = "INSERT INTO Collection (userId, collection) VALUES (%s,%s)"
        param = (user_id, json.dumps({str(passage.passageId): collected_time}))
        mysqlConnector.execute(sql, param)
        return True


def remove_collection(user_id: int, title: str):
    passage = get_passage_detail(title)
    sql = "SELECT collection FROM Collection WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        collections = json.loads(data[0][0])
        if str(passage.passageId) in collections.keys():
            collections.pop(str(passage.passageId))
            sql = "UPDATE Collection SET collection=%s WHERE userId=%s"
            mysqlConnector.execute(sql, (json.dumps(collections), user_id))
            return True
        else:
            return False
    else:
        return False


def get_review_list(user_id: int):
    sql = "SELECT list FROM reviewList WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        review_list = json.loads(str(data[0][0]))
        return review_list
    else:
        return []


def get_new_list(user_id: int):
    sql = "SELECT list FROM newList WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        new_list = json.loads(str(data[0][0]))
        return new_list
    else:
        return []


def update_review_list(user_id: int, review_list: list):
    sql = "SELECT list FROM reviewList WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        sql = "UPDATE reviewList SET list=%s WHERE userId=%s"
        mysqlConnector.execute(sql, (json.dumps(review_list), user_id))
        return True
    else:
        sql = "INSERT INTO reviewList (userId, list) VALUES (%s,%s)"
        param = (user_id, json.dumps(review_list))
        mysqlConnector.execute(sql, param)
        return True


def update_new_list(user_id: int, new_list: list):
    sql = "SELECT list FROM newList WHERE userId=%s"
    data = mysqlConnector.execute(sql, user_id)
    if data:
        sql = "UPDATE newList SET list=%s WHERE userId=%s"
        mysqlConnector.execute(sql, (json.dumps(new_list), user_id))
        return True
    else:
        sql = "INSERT INTO newList (userId, list) VALUES (%s,%s)"
        param = (user_id, json.dumps(new_list))
        mysqlConnector.execute(sql, param)
        return True


def get_all_passage_titles():
    sql = "SELECT title FROM CHNPassage WHERE category=1"
    data = mysqlConnector.execute(sql)
    titles = []
    if data:
        for t in data:
            titles.append(t[0])
    return titles


def get_all_poem_titles():
    sql = "SELECT title FROM CHNPassage WHERE category=0"
    data = mysqlConnector.execute(sql)
    titles = []
    if data:
        for t in data:
            titles.append(t[0])
    return titles


def get_all_author_names():
    sql = "SELECT name FROM CHNAuthor"
    data = mysqlConnector.execute(sql)
    names = []
    if data:
        for t in data:
            names.append(t[0])
    return names


def get_passage(passage_id: int):
    sql = "SELECT * FROM CHNPassage natural join CHNAuthor WHERE CHNPassageId= " + str(passage_id)
    data = mysqlConnector.execute(sql)
    if data:
        return Passage(data[0]).to_dict()

def get_passages_by_author(name: str):
    sql = "SELECT * FROM CHNPassage natural join CHNAuthor WHERE name=%s"
    data = mysqlConnector.execute(sql, name)
    passages = []
    if data:
        for t in data:
            passages.append(Passage(t).to_dict())
    return passages

def random_texts(number: int) -> list:
    sql = "SELECT * FROM CHNPassage natural join CHNAuthor ORDER BY RAND() LIMIT " + str(number)
    data = mysqlConnector.execute(sql)
    passages = []
    if data:
        for t in data:
            passages.append(Passage(t).to_dict())
    return passages

def get_a_random_poem() -> dict:
    sql = "SELECT * FROM CHNPassage natural join CHNAuthor WHERE category=0 ORDER BY RAND() LIMIT 1"
    data = mysqlConnector.execute(sql)
    if data:
        poem = Passage(data[0]).to_dict()
        return poem

def get_a_random_passage() -> dict:
    sql = "SELECT * FROM CHNPassage natural join CHNAuthor WHERE category=1 ORDER BY RAND() LIMIT 1"
    data = mysqlConnector.execute(sql)
    if data:
        passage = Passage(data[0]).to_dict()
        return passage

def get_a_random_game_id() -> int:
    sql = "SELECT gameId FROM Game ORDER BY RAND() LIMIT 1"
    data = mysqlConnector.execute(sql)
    if data:
        game_id = int(data[0][0])
        return game_id

def get_game(game_id: int) -> dict:
    sql = "SELECT game FROM Game WHERE gameId=" + str(game_id)
    data = mysqlConnector.execute(sql)
    if data:
        game = json.loads(data[0][0])
        return game

def get_a_random_question() -> dict:
    sql = "SELECT * FROM CHNQuestion ORDER BY RAND() LIMIT 1"
    data = mysqlConnector.execute(sql)
    if data:
        question_id = int(data[0][0])
        question = data[0][1]
        return {"question_id": question_id, "question": question}

def get_answer(question_id: int) -> str:
    sql = "SELECT answer FROM CHNQuestion WHERE CHNQuestionId=" + str(question_id)
    data = mysqlConnector.execute(sql)
    if data:
        answer = data[0][0]
        return answer

