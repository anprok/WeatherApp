import datetime as dt
import logging

from flask import Flask, make_response, request

app = Flask('main')
logging.basicConfig(filename='app.txt', level=logging.DEBUG)
status_ok = 200


@app.route('/')
def main_view():
    return make_response('<h1>Today is a good day</h1>', status_ok)


@app.after_request
def processor(response):
    logging.info(' '.join([str(dt.datetime.now()),
                           str(request.remote_addr),
                           str(request.method),
                           str(request.scheme),
                           str(request.full_path),
                           str(response.status)]))
    return response
