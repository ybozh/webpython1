from flask import Flask
from flask import render_template
from flask import request
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # return 'Hello World!!! Python'
    # s = Request.form.get("TEXT_1")
    # a = Request.form.get()
    name = 'Yurii'
    e = 3
    return render_template('index.html', title=e, username=name)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")



@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        sum = int(request.form["TEXT_2"]) + int(request.form["TEXT_1"])
        return redirect(url_for("user", usr = sum))
    else:
        return render_template("form.html")


@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
    # return render_template("login.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)