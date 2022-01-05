from flask import Flask, request, Response, jsonify
from connection import connecter

app = Flask(__name__)


@app.route('/')
def hello_world():
    return connecter.execute("SELECT * FROM User")[0][1]


# form: name, password
@app.route('/user/login', methods=["POST"])
def login():
    if request.method == "POST":
        form = request.form.to_dict()
        try:
            data = connecter.execute("SELECT userId, password FROM User WHERE name=" + form["name"])
            return_json = {"userId": "", "success": "no"}
            if (data):
                if (data[1] == form["password"]):
                    return_json["userId"] = data[0]
                    return_json["success"] = "yes"
            return jsonify(return_json)
        except:
            return None


if __name__ == '__main__':
    app.run()
