from flask import jsonify
from flasgger import Swagger


class Home:
    def __init__(self) -> None:
        pass

    def home():

          return jsonify("please visit this documention : http://0.0.0.0:5000/apidocs"), 200