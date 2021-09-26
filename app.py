from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World!!! Python'
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')