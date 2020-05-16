import json
import datetime
from datetime import timedelta
import locale

from flask import jsonify
from flask_restful import Resource

from .. import logger
from ..models import db, CalendarTasks

class CALENDAR(Resource): # '/Calendar/<arg> (None if none)
    def get(self, arg): 
        data = CalendarTasks.query.all()
        return jsonify(status=200, text={'data': f'{data}'})

    def post(self, arg):
        j = json.loads(arg)
        new = CalendarTasks(
                        task=j['name'], 
                        description=j['description'], 
                        target_date=j['targetDate'],
                        time=j['time'],
                        recurring=j['recurring'],
                        interval=j['interval'],
                        color=j['color']
                        )
        logger.debug(f'CALENDAR.POST: {new}')
        db.session.add(new)
        db.session.commit()

        if j['recurring'] == True:
            control = int(j['interval']) 
            interval = int(j['interval'])  
            for i in range(0,154):
                x = j['targetDate'].replace(',', '/')
                locale.setlocale(locale.LC_ALL, 'en_US.utf8')   
                new = datetime.datetime.strptime(x, '%B/%d/%Y') + datetime.timedelta(days=interval)
                new_date = new.strftime('%b/%d/%Y').replace('/', ',')
                recurring_task = CalendarTasks(
                            task=j['name'], 
                            description=j['description'], 
                            target_date=new_date,
                            time=j['time'],
                            recurring=j['recurring'],
                            interval=j['interval'],
                            color=j['color']
                            ) 
                db.session.add(recurring_task)
                db.session.commit()
                interval += control 

        return jsonify(status=200)

    def delete(self, arg):
        task = CalendarTasks.query.filter_by(id=arg).first()
        db.session.delete(task)
        db.session.commit()
        logger.debug(f'CALENDAR.DELETE: {task}')
        
        if task.recurring:
            delete_recurring = CalendarTasks.__table__.delete().where(CalendarTasks.task == task.task and CalendarTasks.recurring == True)
            db.session.execute(delete_recurring)
            db.session.commit()

        return jsonify(status=200)