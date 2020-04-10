from flask import Flask, Response


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return Response('Hello, world!')
