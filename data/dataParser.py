#!/usr/bin/python3
import datetime


class user:
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
