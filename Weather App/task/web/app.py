import sys
import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.secret_key = b'_2#x4M"F3Q9z\n\xec]/'
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


db.create_all()
dict_with_weather_info = {}
app_id = '21fa0fbd891c785300f4e9c6'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            new_city = City(name=request.form['city_name'])
            db.session.add(new_city)
            db.session.commit()
            return redirect(url_for('index'))
        except IntegrityError:
            flash('The city has already been added to the list!')
            return redirect('/')
        except KeyError:
            flash('The city has already been added to the list!')
            return redirect('/')
    cities = City.query.all()
    dict_with_weather_info.clear()
    for city in cities:
        params = {'q': city.name, 'appid': app_id, 'units': 'metric'}
        r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        if r.ok:
            sunrise = int(r.json()['sys']['sunrise'])
            sunset = int(r.json()['sys']['sunset'])
            time = int(r.json()['dt'])
            if sunrise + 3600 < time < sunset - 3600:
                day_period = 'day'
            elif sunset + 1800 < time or time < sunrise - 1800:
                day_period = 'night'
            else:
                day_period = 'evening-morning'
            dict_with_weather_info[city.name] = {
                    'id': city.id,
                    'degrees': r.json()['main']['temp'],
                    'state': r.json()['weather'][0]['main'],
                    'day_period': day_period,
                }
        else:
            flash("The city doesn't exist!")
            redirect('/delete/'+str(city.id))
    return render_template('index.html', weather=dict_with_weather_info)


@app.route('/delete/<city_id>', methods=['GET', 'POST'])
def delete(city_id):
    city = City.query.filter_by(id=city_id).first()
    db.session.delete(city)
    db.session.commit()
    return redirect('/')


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
