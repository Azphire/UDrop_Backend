#!/usr/bin/python3
import datetime


class User:
    def __init__(self, data):
        self.userId = int(data[0])

        self.name = data[1]

        self.vip = data[2]
        if self.vip:
            self.vip = int(self.vip)

        self.gender = data[3]
        if self.gender:
            self.gender = int(self.gender)

        self.age = data[4]
        if self.age:
            self.age = int(self.age)

        self.audioType = data[5]
        if self.audioType:
            self.audioType = int(self.audioType)

        self.speed = data[6]
        if self.speed:
            self.speed = int(self.speed)

        # self.password = data[7]

        self.motto = data[8]

        current = datetime.datetime.now()
        self.learnedDays = (current - data[9]).days + 1


class Passage:
    def __init__(self, data):
        self.passageId = data[1]
        self.title = data[2]
        self.author = data[7]
        self.introduction = data[9]
        self.dynasty = data[8]
        self.content = data[5]
        self.category = data[6]  # 0: poem, 1: passage

    def to_dict(self):
        return {
            "passage_id": self.passageId,
            "title": self.title,
            "author": self.author,
            # "author_info": self.introduction,
            "dynasty": self.dynasty,
            "content": self.content,
            "category": self.category
        }