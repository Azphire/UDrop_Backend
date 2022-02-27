#!/usr/bin/python3
import datetime
import json


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
            "id": self.passageId,
            "title": self.title,
            "author": self.author,
            # "author_info": self.introduction,
            "dynasty": self.dynasty,
            "content": self.content,
            "category": self.category
        }


class ReviewList:
    def __init__(self, data=None):
        self.current = datetime.datetime.today()
        if data is None:
            self.today = []
            self.future = []
            return

        total = json.loads(data)
        for i in range(len(total)):
            total[i]["time"] = datetime.datetime.strptime(total[i]["time"], "%Y-%m-%d")
        self.today = [item for item in total if (self.current - item["time"]).days == 0]
        self.future = [item for item in total if (self.current - item["time"]).days < 0]

    def add_review_items(self, title: str) -> list:
        days = [1, 7, 30]
        for day in days:
            already_in_list = False
            for i in range(len(self.future)):
                if (self.future[i]["time"] - self.current).days + 1 == day and self.future[i]["title"] == title:
                    already_in_list = True
                    break
            if not already_in_list:
                self.future.append({
                    "title": title,
                    "done": 0,
                    "time": self.current + datetime.timedelta(days=day)
                })
        for i in range(len(self.future)):
            self.future[i]["time"] = self.future[i]["time"].strftime("%Y-%m-%d")
        for i in range(len(self.today)):
            self.today[i]["time"] = self.today[i]["time"].strftime("%Y-%m-%d")
        return self.today + self.future

    def update_today(self, data: list) -> list:
        new_today = data
        for i in range(len(self.future)):
            self.future[i]["time"] = self.future[i]["time"].strftime("%Y-%m-%d")
        return new_today + self.future

    def get_today(self) -> list:
        for i in range(len(self.today)):
            self.today[i]["time"] = self.today[i]["time"].strftime("%Y-%m-%d")
        return self.today
