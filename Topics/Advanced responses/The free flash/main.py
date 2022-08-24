from flask import Flask, flash, get_flashed_messages

app = Flask('main')

@app.route('/')
def main_view():
    flash("It's cold in the graveyard", 'info')
    flash("You don't know whos is behind you.", 'ahtung')
    flash('There is no pain', 'error')
    flash('What are you receiving', 'interest')

    return get_flashed_messages(category_filter='error')