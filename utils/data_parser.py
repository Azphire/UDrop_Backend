#!/usr/bin/python3
import datetime


class user:
    def __init__(self, data):
        self.userId = data[0]
        self.name = data[1]
        self.vip = data[2]
        self.gender = data[3]
        self.age = data[4]
        self.audioType = data[5]
        self.speed = data[6]
        # self.password = data[7]
        self.motto = data[8]
        current = datetime.datetime.now()
        self.learnedDays = (current - data[9]).days + 1
