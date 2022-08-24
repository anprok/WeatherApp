from flask import Flask

app = Flask('main')

app.config.update({
    'DEBUG': True,
    'TESTING': True,
})