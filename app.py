from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!!! Python'
    name = 'Yuriy'
    a = 1 + 4
    return render_template('index.html', title='Welcome', username=name, a=a)

if __name__ == '__main__':
    app.run(host='0.0.0.0')