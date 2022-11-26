from flask import Flask, request, jsonify, Blueprint
from flask_cors import CORS
from flasgger import Swagger
from service.weather import Weather
from service.home import Home


app = Flask(__name__)
swagger = Swagger(app)
blueprint = Blueprint('api', __name__)
app.register_blueprint(blueprint)
CORS(app)

# weather routes
@app.route('/', methods=['GET'])
def home():
       return Home.home()


@app.route('/weather/', methods=['GET'])
def weather_forecast():
    local = request.args.get('local')
    return Weather.weather_forecast(local)


@app.route('/weather_history/', methods=['GET'])
def weather_forecast_history():
    return Weather.weather_forecast_history()



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
