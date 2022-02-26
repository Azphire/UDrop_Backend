from connection import mysqlConnector
from data.dataParser import *
import json
import datetime


def get_password_by_name(name: str):
    sql = "SELECT userId, password FROM User WHERE name=%s"
    data = mysqlConnector.execute(sql, name)
    return data


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
    pass

def get_passages_by_author(name: str):
    sql = "SELECT * FROM CHNPassage natural join CHNAuthor WHERE name=%s"
    data = mysqlConnector.execute(sql, name)
    passages = []
    if data:
        for t in data:
            passages.append(Passage(t).to_dict())
    return passages

