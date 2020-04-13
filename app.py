from flask import Flask, Response


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    res = Response('Hello, world!')
    res.headers['Connection'] = 'close'
    return res
