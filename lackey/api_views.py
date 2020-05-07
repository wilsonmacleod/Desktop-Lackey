from flask import jsonify
from flask_restful import Resource
from lackey.models import db, WeatherConfig

class API_ROUTER(Resource):
    def get(self, view): # '/api/<view>'
        if view == 'Hello':
            x = WeatherConfig.query.all()
            return jsonify(status=200, text={"Hello": f"{x}"})
        else:
            return jsonify(status=404)