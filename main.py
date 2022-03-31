import os

from flask import Flask, make_response, jsonify
from data import db_session, news_resources

app = Flask(__name__)


@app.route("/")
def index():
    return 'Привет от приложения Flask'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
