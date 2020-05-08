from flask import jsonify
from flask_restful import Resource
from lackey.models import db, CalendarTasks

class API_ROUTER(Resource):
    def get(self, view): # '/api/<view>'
        if view == 'Calendar':
            results = CalendarTasks.query.all()
            return jsonify(status=200, text={"data": f"{results}"})
        else:
            return jsonify(status=404)
    def post(self, view):
        if view == 'Calendar':
            