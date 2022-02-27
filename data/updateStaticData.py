#!/usr/bin/python3
from connection import mysqlConnector


def updateStatic():
    sql = "SELECT name FROM CHNAuthor"
    data = mysqlConnector.execute(sql)
    names = ""
    if data:
        for t in data:
            names += " " + t[0]
    with open('../static/authors.txt', 'w') as f:
        f.write(names)


    sql = "SELECT title FROM CHNPassage WHERE category=0"
    data = mysqlConnector.execute(sql)
    titles = ""
    if data:
        for t in data:
            titles += " " + t[0]
    with open('../static/poems.txt', 'w') as f:
        f.write(titles)


    sql = "SELECT title FROM CHNPassage WHERE category=1"
    data = mysqlConnector.execute(sql)
    titles = ""
    if data:
        for t in data:
            titles += " " + t[0]
    with open('../static/passages.txt', 'w') as f:
        f.write(titles)

    print("Static Updated")