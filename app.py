import os
import requests
import json

from datetime import datetime

from dotenv import load_dotenv

from flask import render_template
from flask import request
from flask import jsonify
from flask_caching import Cache

from config import DevelopConfig

from services import create_app
from services.utils.form import BasicForm


load_dotenv()

cacheConfig = {
    'CACHE_TYPE': "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 120
}

cache = Cache(config=cacheConfig)

app = create_app(DevelopConfig)

cache.init_app(app)

TITLE = "Weather API"

@app.route('/')
def index():
    return render_template('index.html',
                           title=TITLE), 200

@app.route('/weather', methods=['GET', 'POST'])
@app.route('/weather/<string:city>/<string:code>')
@cache.cached(timeout=120)
def weather(city="Mexico City", code="mx"):

    if len(request.path.split('/')) > 3:
        weather = get_weather(city, code)
        weather = json.loads(weather.text)

        celsius = weather['main']['temp']
        fahrenheit = round(convert(float(celsius)), 2)

        sunrise = datetime.fromtimestamp(weather['sys']['sunrise'])
        sunset = datetime.fromtimestamp(weather['sys']['sunset'])

        req_time = datetime.fromtimestamp(weather['dt'])

        return jsonify({
            'success': True,
            'data': {
                'location_name': weather['name'] + ", " + weather['sys']['country'], 
                'temperature': {
                    'celsius': str(celsius) + " C",
                    'farenheit': str(fahrenheit) + "F"
                },
                'wind': str(weather['wind']['speed']) + "km/h",
                'cloudiness': weather['clouds']['all'],
                'pressure': str(weather['main']['pressure']) + "hpa",
                'himidity': str(weather['main']['humidity']) + "%",
                'sunrise': sunrise,
                'sunset': sunset,
                'geocoordinates': {
                    'longitud': weather['coord']['lon'],
                    'latitud': weather['coord']['lat']
                },
                'request_time': req_time
            }
        }), 200
    
    query = BasicForm(request.form)
    
    if request.method == "POST":
        weather = get_weather(query.city.data, query.country_code.data)
        weather = json.loads(weather.text)

        celsius = weather['main']['temp']
        fahrenheit = round(convert(float(celsius)), 2)

        sunrise = datetime.fromtimestamp(weather['sys']['sunrise'])
        sunset = datetime.fromtimestamp(weather['sys']['sunset'])

        req_time = datetime.fromtimestamp(weather['dt'])

        return render_template('weather.html',
                            title=TITLE, 
                            query=query,
                            location=weather['name'],
                            country=weather['sys']['country'],
                            tempC=weather['main']['temp'],
                            tempF=fahrenheit,
                            wind=weather['wind']['speed'],
                            cloud=weather['clouds']['all'],
                            pressure=weather['main']['pressure'],
                            humidity=weather['main']['humidity'],
                            sunrise=sunrise,
                            sunset=sunset,
                            longitud=weather['coord']['lon'],
                            latitud=weather['coord']['lat'],
                            req_time=req_time), 200
    else:
        return render_template('weather.html',
                            title=TITLE, 
                            query=query,
                            location="",
                            country="",
                            tempC="",
                            tempF="",
                            wind="",
                            cloud="",
                            pressure="",
                            humidity="",
                            sunrise="",
                            sunset="",
                            longitud="",
                            latitud="",
                            req_time=""), 200

def get_weather(city, country):
    api_key = os.getenv('API_KEY')
    url = os.getenv('API_URL') +\
            city + "," + country +\
            "&units=metric" +\
            "&appid=" + api_key
    
    response = requests.get(url)

    return response


def convert(degrees):
    fahrenheit = (degrees * (9/5)) + 32

    return fahrenheit

if __name__ == '__main__':
    app.run()