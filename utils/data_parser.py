#!/usr/bin/python3

def into_user(data):
    return {
        "userId": data[0],
        "name": data[1],
        "vip": data[2],
        "gender": data[3],
        "age": data[4],
        "audioType": data[5],
        "speed": data[6],
        # "password": data[7]
    }
