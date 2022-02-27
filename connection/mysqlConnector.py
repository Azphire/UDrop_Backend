import pymysql
import json
import os


def execute(sql: str, param=None):
    base = os.path.dirname(os.path.abspath(__file__))
    with open(base + '/mysqlConfig.json', 'r', encoding='utf8')as conf:
        mysql_info = json.load(conf)

    db = pymysql.connect(host=mysql_info["host"],
                         user=mysql_info["user"],
                         password=mysql_info["password"],
                         database=mysql_info["database"])
    cursor = db.cursor()
    if param:
        cursor.execute(sql, param)
    else:
        cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data
