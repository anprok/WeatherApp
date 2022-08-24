import os

from flask import Flask

app = Flask('main')

key = os.urandom(24)
app.config['SECRET_KEY'] = key
