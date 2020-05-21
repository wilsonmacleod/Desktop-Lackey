import json
from datetime import datetime as dt
import locale

from flask import jsonify
from flask_restful import Resource

from lackey import logger
from lackey.api_views.sub_sports import nba, soccer, nfl

class SPORTS(Resource): #/Sports/<arg> (None if none)
    """
    this controls API call processing
    """
    def get(self, arg):
        data = 'None'
        if arg == 'init':
            data = Actions.update()
        logger.debug(f'get.SPORTS: {data}')
        return jsonify(status=200, text={'data': f'{data}'})\

class Actions():
    """
    this controls standard checks/logic
    actual updating is handled per sport
    in "sub_sports"
    """
    def checkDate(check):
        logger.debug(f'checkDate')
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')   
        active_date = dt.strptime(check, '%Y-%m-%d')
        today = dt.combine(dt.today(), dt.min.time())
        if today > active_date:
            logger.debug('checkDate-true')
            return True
        return False 
    
    def checkIfUpdate(sql_obj):
        logger.debug(f'checkIfUpdate')
        if sql_obj == []: # if nothing in db
            return True
        elif sql_obj and Actions.checkDate(sql_obj[0].entered_date): # if ood in db
            return True
        else: # if already in and updated
            logger.debug('dontUpdate')
            return False
    
    def clean_string_dict(object, keyword):
        """
        clean sub-dicts stored as 
        strings in db.Texts
        """
        dict_convert = dict(object.__dict__)
        dict_convert.pop('_sa_instance_state', None)
        dict_convert[keyword] = json.loads(dict_convert[keyword].replace("'", '"')) 
        return dict_convert

    def update():
        return {
            'nba': nba.updateNBA(),
            'soccer': soccer.updateSoccer(),
            'nfl': nfl.updateNFL()
            }