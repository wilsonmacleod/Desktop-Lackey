from flask import jsonify
from flask_restful import Resource

class API_ROUTER(Resource):
    def get(self, view):
        if view == 'Hello':
            return jsonify(status=200, text={"Hello": "Here is a test response"})
        else:
            return jsonify(status=404)