from flask import Flask, request, Response, jsonify
from connection import connecter
from utils import data_parser

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Connected!"


# form: name, password
# return: success, userId
@app.route('/user/login', methods=["POST"])
def login():
    if request.method == "POST":
        form = request.form.to_dict()
        try:
            sql = "SELECT userId, password FROM User WHERE name=%s"
            data = connecter.execute(sql, form["name"])
            return_json = {"userId": "", "success": "no"}
            if (data):
                if (data[0][1] == form["password"]):
                    return_json["userId"] = data[0][1]
                    return_json["success"] = "yes"
            return jsonify(return_json)
        except:
            return "Failed"


# get: name
# return: exist or not exist
@app.route('/user/name', methods=["GET"])
def get_name():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            sql = "SELECT userId FROM User WHERE name =%s"
            data = connecter.execute(sql, args["name"])
            if len(data) > 0:
                return "exist"
            else:
                return "not exist"
        except:
            return "Failed"


# form: name, password
# return: success, userId
@app.route('/user/register', methods=["POST"])
def register():
    if request.method == "POST":
        form = request.form.to_dict()
        try:
            sql = "INSERT INTO User (name, password) VALUES (%s,%s)"
            param = (form["name"], form["password"])
            connecter.execute(sql, param)
            sql = "SELECT userId FROM User WHERE name =%s"
            data = connecter.execute(sql, form["name"])
            return_json = {"userId": "", "success": "no"}
            if data:
                return_json["userId"] = data[0][0]
                return_json["success"] = "yes"
            return jsonify(return_json)
        except:
            return "Failed"


# args: userId
# return: json
@app.route('/user/info', methods=["GET", "POST"])
def info():
    if request.method == "GET":
        args = request.args.to_dict()
        try:
            sql = "SELECT * FROM User WHERE userId=" + args["userId"]
            data = connecter.execute(sql)[0]
            if data:
                return_json = data_parser.into_user(data)
                return jsonify(return_json)
        except:
            return "Failed"

    # TODO: 修改数据的逻辑，注意数字单独转一下
    if request.method == "POST":
        form = request.form.to_dict()
        pass


if __name__ == '__main__':
    app.run()
