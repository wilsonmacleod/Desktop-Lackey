from flask import jsonify
from flask_restful import Resource

from lackey import logger
#from lackey.models import db
from lackey.actions.model_actions.weather import ShouldWeatherUpdate
from lackey.actions.external_actions import weather as ext_act_weather

class WEATHER(Resource): # /Weather/<action> (None if none)
    def get(self, action):
        if action == "init":
            if ShouldWeatherUpdate.checkConfig():
                data = "get data for config funcs"
            else:
                data = "None"
        else:
            action = action.split("=")
            keyword = action[0]
            query = action[1]
            if keyword == "query":
                data = ext_act_weather.search_city(query)
        logger.debug(data)
        return jsonify(status=200, text={"data": f"{data}"})