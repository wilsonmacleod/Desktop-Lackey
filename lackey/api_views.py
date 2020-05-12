import json
import datetime
from datetime import timedelta
import locale

from flask import jsonify
from flask_restful import Resource
from lackey.models import db, CalendarTasks

class API_ROUTER(Resource):

    def get(self, view): # '/api/<view>'
        if view == 'Calendar':
            query = CalendarTasks.query.all()
            return jsonify(status=200, text={"data": f"{query}"})
        else:
            return jsonify(status=400)

    def post(self, view):
        #try:
        j = json.loads(view)
        new = CalendarTasks(task=j['name'], 
                        description=j['description'], 
                        target_date=j['targetDate'],
                        time=j['time'],
                        recurring=j['recurring'],
                        interval=j['interval'])
        db.session.add(new)
        db.session.commit()


        if j['recurring'] == True:
            control = int(j['interval']) # 7 
            interval = int(j['interval']) #7 
            for i in range(0,154):
                x = j['targetDate'].replace(',', '/')
                locale.setlocale(locale.LC_ALL, 'en_US.utf8')   
                new = datetime.datetime.strptime(x, '%B/%d/%Y') + datetime.timedelta(days=interval)
                new_date = new.strftime("%b/%d/%Y").replace("/", ",")
                recurring_task = CalendarTasks(task=j['name'], 
                            description=j['description'], 
                            target_date=new_date,
                            time=j['time'],
                            recurring=j['recurring'],
                            interval=j['interval']) 
                db.session.add(recurring_task)
                db.session.commit()
                interval += control # 7, 14, 21, 28, 35,

        return jsonify(status=200)
        #except:
        #    return jsonify(status=400)

    def delete(self, view):
        #try:
        task = CalendarTasks.query.filter_by(id=view).first()
        db.session.delete(task)
        db.session.commit()

        if task.recurring:
            delete_recurring = CalendarTasks.__table__.delete().where(CalendarTasks.task == task.task and CalendarTasks.recurring == True)
            db.session.execute(delete_recurring)
            db.session.commit()

        return jsonify(status=200)
        #except:
        #    return jsonify(status=400)

            