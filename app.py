from flask import Flask, request, jsonify
from datetime import date
import requests

from os import environ
APIKEY = environ.get('APIKEY')

print('Loi', APIKEY)


app = Flask(__name__)


def getDate():
    today = date.today()
    return "{}-{}-{}".format(today.year, today.month, today.day)


cities = [
    "Reno,NV",
    "Austin,TX",
    "Tampa,FL"
]


def getForecasts():
    data = []
    for c in cities:
        r = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=14".format(APIKEY, c))
        r = r.json()
        data.append(r)
    return data


@app.route("/")
def hello_world():
    return jsonify(getForecasts())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
