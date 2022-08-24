from flask import Flask, redirect

app = Flask('main')

url = input()


@app.route(url)
def view_function():
    return "Haha! I'm out of reach!"

@app.route('/just/redirect/me')
def redirector_func():
    redirect(url)