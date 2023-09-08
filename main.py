from flask import Flask
from mastodon import Mastodon
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
