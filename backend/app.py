import time
from flask import Flask


app = Flask(__name__)


@app.route('/n')
def n():
    return "Le N. a parlé"


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5050) # threaded=True
