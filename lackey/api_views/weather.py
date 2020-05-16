import json
from datetime import datetime
import locale

from flask import jsonify
from flask_restful import Resource

from lackey import logger
from lackey.models import db, WeatherConfig, WeatherForecast
from lackey.external_apis import weather

class WEATHER(Resource): # /Weather/<arg> (None if none)
    def get(self, arg):
        if arg == 'init':
            config = WeatherConfig.query.all()
            if config != []:
                data = Actions.updateNeeded(config)
            else:
                data = 'None'
        else:
            arg = arg.split('=')
            keyword, query = arg[0], arg[1]
            if keyword == 'query':
                data = weather.search_city(query)
            elif keyword == 'refresh':
                obj = WeatherConfig.query.filter_by(city=query).first()
                Actions.delete(obj.woied)
                data = Actions.update(obj.woied)
        logger.debug(f'get.WEATHER: {data}')
        return jsonify(status=200, text={'data': f'{data}'})

    def post(self, arg):
        j = json.loads(arg)
        new = WeatherConfig(
            city=j['city'],
            woied=j['woied']
        )
        logger.debug(f'WEATHER.POST: {new}')
        db.session.add(new)
        db.session.commit()
        return jsonify(status=200)

    def delete(self, arg):
        config = WeatherConfig.query.filter_by(city=arg).first()
        db.session.delete(config)
        db.session.commit()
        logger.debug(f'WEATHER.DELETE: {config}')

class Actions():  
    def updateNeeded(config):
        data = {}
        for each in config:
            logger.debug(each)
            woied = each.woied
            check = WeatherForecast.query.filter_by(woied=woied).first()

            if not check: # if nothing in db
                data[each.city] = (Actions.update(woied))

            elif check and Actions.checkDate(check): # if ood in db
                Actions.delete(woied)
                data[each.city] = (Actions.update(woied))

            else: # if already updated
                data[each.city] = (Actions.dontUpdate(woied))
                
        return data

    def checkDate(check):
        logger.debug('checkDate')
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')   
        active_date = datetime.strptime(check.date, '%Y-%m-%d')
        today = datetime.combine(datetime.today(), datetime.min.time())
        if today > active_date:
            logger.debug('checkDate-true')
            return True
        return False

    def delete(woied):
        logger.debug('delete')
        objs = WeatherForecast.__table__.delete().where(WeatherForecast.woied == woied)
        db.session.execute(objs)
        db.session.commit()

    def update(woied):
        logger.debug('update')
        new_data = weather.return_weather_data(woied)
        for i in new_data:
            new = WeatherForecast(
                    date=i['date'],
                    weather_state_name=i['weather_state_name'],
                    icon_link=i['icon_link'],
                    min_temp=i['min_temp'],
                    max_temp=i['max_temp'],
                    humidity=i['humidity'],
                    wind_speed=i['wind_speed'],
                    predictability=i['predictability'],
                    woied=i['woied']
                        )
            logger.debug(new)
            db.session.add(new)
            db.session.commit()
        return new_data

    def dontUpdate(woied):
        logger.debug('dontUpdate')
        return WeatherForecast.query.filter_by(woied=woied).all()