import requests
from os import environ
from flask import Flask, jsonify

APIKEY = environ.get('APIKEY')

app = Flask(__name__)

cities = [
    "Reno,NV",
    "Austin,TX",
    "Tampa,FL"
]


def getForecasts():
    data = []
    for c in cities:
        r = requests.get(
            "https://api.weatherapi.com/v1/forecast.json?days=14&q={}&key={}".format(c, APIKEY))
        r = r.json()
        data.append(r)
    return data


@app.route("/")
def home():
    return jsonify(getForecasts())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
