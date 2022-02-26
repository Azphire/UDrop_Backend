from flask import Flask, request, jsonify
from connection import mysqlConnector
from data import dataParser
from data import crud
from slotMatching import textMatch
from mainFunction import reply

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
            data = crud.get_password_by_name(str(form["name"]))
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
                info = dataParser.User(data)
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
            new_list = crud.get_new_list(userId)
            review_list = crud.get_review_list(userId)
            result = {
                "new_list": new_list,
                "review_list": review_list
            }
            return jsonify(result)
        except:
            return "Failed"


#### 2.2 set_new_schedule
# - param: (user_id: Int, new_schedule: JSONArray) 这里的JSONArray就是你前面返回的古诗列表格式，不用管它是个什么词
# - return: (resultCode: Int)
#   - 0: failure
#   - 1: success
@app.route('/study/new_schedule', methods=["POST"])
def new_list():
    if request.method == "POST":
        form = request.get_json()
        try:
            success = crud.update_new_list(int(form["user_id"]), form["new_schedule"])
            if success:
                return "Success"
            else:
                return "Failed"
        except:
            return "Failed"


#### 2.3 set_review_schedule
# - param: (user_id: Int, review_schedule: JSONArray)
# - return: (resultCode: Int)
#   - 0: failure
#   - 1: success
@app.route('/study/review_schedule', methods=["POST"])
def review_list():
    if request.method == "POST":
        form = request.get_json()
        try:
            success = crud.update_review_list(int(form["user_id"]), form["review_schedule"])
            if success:
                return "Success"
            else:
                return "Failed"
        except:
            return "Failed"


# 3.1 get_text_detail
# - param: (title: String)
# - return: (title: String, writer: String, writer_info: String, content: String)
@app.route('/passage/detail', methods=["GET"])
def passageDetail():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            passage = crud.get_passage_detail(args["title"])
            return_json = {
                "title": passage.title,
                "author": passage.author,
                "author_info": passage.introduction,
                "content": passage.content
            }
            return jsonify(return_json)
        except:
            return "Failed"


# 4.1 get_collection
# - param: (user_id: Int)
# - return: (collection_list: JSONArray)
# 4.2 remove_collection
# - param: (user_id: Int, title: String)
# - return:
#   - "Failed", "Success"
# 4.3 add_collection
# - param: (user_id: Int, title: String)
# - return:
#   - "Failed", "Success"
@app.route('/user/collection', methods=["GET", "POST", "DELETE"])
def collection():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            collection_list = crud.get_collection(int(args["user_id"]))
            return jsonify({"collection_list": collection_list})
        except:
            return "Failed"

    if request.method == "POST":
        form = request.get_json()
        try:
            added = crud.add_collection(int(form["user_id"]), form["title"])
            if added:
                return "Added"
            else:
                return "No Change"
        except:
            return "Failed"

    if request.method == "DELETE":
        form = request.get_json()
        try:
            removed = crud.remove_collection(int(form["user_id"]), form["title"])
            if removed:
                return "Removed"
            else:
                return "No Change"
        except:
            return "Failed"


#### 3.2 search_text
# - param: (key: String)
# - return: (result_list: JSONArray) 诗名或作者与关键词匹配
@app.route('/poems/search', methods=["GET"])
def key_search():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            passages = textMatch.match(args["key"])
            return jsonify({"result_list": passages})
        except:
            return "Failed"


#### 3.3 random_poems
# - GET
# - param: (number: Int) 随机返回的数量
# - return: (result_list: JSONArray)
@app.route('/poems/random', methods=["GET"])
def random_poems():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            passages = crud.random_texts(int(args["number"]))
            return jsonify({"result_list": passages})
        except:
            return "Failed"

# 语音功能
@app.route('/reply', methods=["POST"])
def response():
    if request.method == "POST":
        form = request.get_json()
        try:
            user_id = int(form["user_id"])
            text = form["text"]
            is_finished, response = reply(user_id, text)
            return jsonify({"is_finished": is_finished, "response": response})
        except:
            return "Failed"

if __name__ == '__main__':
    app.run()
