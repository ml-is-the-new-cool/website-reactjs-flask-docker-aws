import time
from flask import Flask

app = Flask(__name__)


@app.route('/n')
def n():
    return "Le N. a parlé"


@app.route('/')
def hello():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
