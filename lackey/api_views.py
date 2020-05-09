import json
import datetime

from flask import jsonify
from flask_restful import Resource
from lackey.models import db, CalendarTasks

class API_ROUTER(Resource):
    def get(self, view): # '/api/<view>'
        if view == 'Calendar':
            query = CalendarTasks.query.all()
            return jsonify(status=200, text={"data": f"{query}"})
        else:
            return jsonify(status=404)
    def post(self, view):
        try:
            j = json.loads(view)
            new = CalendarTasks(task=j['name'], 
                            description=j['description'], 
                            target_date=j['targetDate'],
                            recurring=j['recurring'])
            db.session.add(new)
            db.session.commit()
            return jsonify(status=200)
        except:
            return jsonify(status=400)

            