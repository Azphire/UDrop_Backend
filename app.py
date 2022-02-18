from flask import Flask, request, Response, jsonify
from connection import mysqlConnector
from utils import dataParser

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Connected!"


# form: name, password
# return: success, userId
@app.route('/user/login', methods=["POST"])
def login():
    if request.method == "POST":
        form = request.get_json()
        try:
            sql = "SELECT userId, password FROM User WHERE name=%s"
            data = mysqlConnector.execute(sql, form["name"])
            return_json = {"userId": -1, "success": 0}
            if (data):
                if (data[0][1] == form["password"]):
                    return_json["userId"] = int(data[0][0])
                    return_json["success"] = 1
            return jsonify(return_json)
        except:
            return "Failed"


# 1.2 check_existed_user
# param: [name: String]
# return:
# "Exist", "Not exist", "Failed"
@app.route('/user/name', methods=["GET"])
def get_name():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            sql = "SELECT userId FROM User WHERE name =%s"
            data = mysqlConnector.execute(sql, args["name"])
            if len(data) > 0:
                return "Exist"
            else:
                return "Not exist"
        except:
            return "Failed"


# 1.1 add_new_user
# form: [name: String, password: String]
# return:
# user_id: Integer
# added: Integer: 0, new user added; 1, not added (exist)
@app.route('/user/register', methods=["POST"])
def register():
    if request.method == "POST":
        form = request.get_json()
        try:
            sql = "INSERT INTO User (name, password) VALUES (%s,%s)"
            param = (form["name"], form["password"])
            mysqlConnector.execute(sql, param)
            sql = "SELECT userId FROM User WHERE name =%s"
            data = mysqlConnector.execute(sql, form["name"])
            return_json = {"user_id": None, "added": 0}
            if data:
                return_json["user_id"] = int(data[0][0])
                return_json["added"] = 1
            return jsonify(return_json)
        except:
            return "Failed"


# 1.3 get_user_info
# form: (user_id: Int)
# return: (name: String, user_motto: String, learned_days: Int)

# 1.4 change_user_info
# param: (user_id: Int, name: String, user_motto: String)
# return:
# "Failed", "Success"
@app.route('/user/basic_info', methods=["GET", "POST"])
def basicInfo():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            sql = "SELECT * FROM User WHERE userId=" + str(args["user_id"])
            data = mysqlConnector.execute(sql)[0]
            if data:
                info = dataParser.user(data)
                return_json = {
                    "user_name": info.name,
                    "user_motto": info.motto,
                    "learned_days": info.learnedDays
                }
                return jsonify(return_json)
        except:
            return "Failed"

    if request.method == "POST":
        form = request.get_json()
        try:
            sql = "UPDATE User SET name=%s, motto=%s WHERE userId =" + str(form["user_id"])
            param = (form["name"], form["user_motto"])
            mysqlConnector.execute(sql, param)
            return "Success"
        except:
            return "Failed"

# 2.1 get_schedule
# param: (user_id: Int)
# return: (new_list: Array, review_list: Array)
# new_list: 今日所有需要新学的课文，每个课文信息中包含是否已背诵
# review_list: 今日所有需要复习的课文，每个课文信息中包含是否已背诵
@app.route('/study/schedule', methods=["GET"])
def schedule():
    # TODO：code
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            userId = args["user_id"]
            print(userId)
            result = {
                "new_list": [{"title": "静夜思", "done": 1}, {"title": "出师表", "done": 0}, {"title": "蜀道难", "done": 0}],
                "review_list": [{"title": "离骚", "done": 0}, {"title": "桃花源记", "done": 1}]
            }
            return jsonify(result)
        except:
            return "Failed"

if __name__ == '__main__':
    app.run()
