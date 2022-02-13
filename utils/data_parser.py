#!/usr/bin/python3
import datetime


class user:
    def __init__(self, data):
        self.userId = int(data[0])
        self.name = data[1]
        self.vip = int(data[2])
        self.gender = int(data[3])
        self.age = int(data[4])
        self.audioType = int(data[5])
        self.speed = int(data[6])
        # self.password = data[7]
        self.motto = data[8]
        current = datetime.datetime.now()
        self.learnedDays = (current - data[9]).days + 1
