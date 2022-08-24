from flask import Flask, request

app = Flask('main')


@app.route('/', methods=['GET', 'POST'])
def deassemle_request():
    return request.method
