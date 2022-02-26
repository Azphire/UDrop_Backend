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