from flask import jsonify, abort
from models import weather
from datetime import datetime

import requests

weather = weather.Weather()


class Weather:

    def __init__(self):
        self.url = "https://api.openweathermap.org/data/2.5/"
        self.appID_local = "83927a7a47f1f0b415c2caa40c46b2a4"
        self.appID_generic = "439d4b804bc8187953eb36d2a8c26a02"

    @staticmethod
    def weather_forecast(local):

        dado_tempo = []
        data_tempo = []
        url = "https://api.openweathermap.org/data/2.5/weather?appid=83927a7a47f1f0b415c2caa40c46b2a4&q=" + \
            str(local)
        payload = {}
        headers = {}

        response_lon_lat = requests.request("GET", url, headers=headers, data=payload)

        if response_lon_lat.status_code == 200:
            lon_lat = response_lon_lat.json()
            url = "https://api.openweathermap.org/data/2.5//forecast?lat="+str(lon_lat['coord']['lat'])+"&lon="+str(lon_lat['coord']['lon'])+"&units=metric&appid=b0cd5caaf7ed18c0dd90a06e67250c4c&"
            payload = {}
            headers = {}

            response = requests.request(
                "GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                    return jsonify(abort(404, description="Resource not found"))

            for dates in response.json()['list']:
                    dados = {
                        "city": str(response.json()['city']['name']),
                        "temp": dates['main']['temp'],
                        "temp_min": dates['main']['temp_min'],
                        "temp_max": dates['main']['temp_max'],
                        "description": dates['weather'],
                        "dt": str(dates['dt_txt'])
                    }
                    if dates['dt_txt'][0:10] not in data_tempo:
                        data_tempo.append(dates['dt_txt'][0:10])
                        dado_tempo.append(dados)
                        weather.create(dados)
            return jsonify(dado_tempo)
        
        
    @staticmethod
    def weather_forecast_history():
             return jsonify(weather.find({})), 200