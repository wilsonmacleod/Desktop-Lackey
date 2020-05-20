import json
import datetime
from datetime import datetime as dt
import locale

from flask import jsonify
from flask_restful import Resource

from lackey import logger
from lackey.models import (
    db, 
    NBAScoreBoard, NBAStandings, NBALeaders
    )
from lackey.external_apis.sports import nba

class SPORTS(Resource): #/Sports/<arg> (None if none)
    def get(self, arg):
        data = 'None'
        if arg == 'init':
            data = Actions.update()
        logger.debug(f'get.SPORTS: {data}')
        return jsonify(status=200, text={'data': f'{data}'})


class Actions():

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
            NBAScoreBoard.query.delete() # delete all
            return True
        else: # if already in and updated
            return False

    def updateNBA():
        logger.debug(f'checkNBA')
        scoreboard = NBAScoreBoard.query.all()
        if Actions.checkIfUpdate(scoreboard): # check date too
            locale.setlocale(locale.LC_ALL, 'en_US.utf8')
            test_day = datetime.datetime.strptime('2020-03-11', '%Y-%m-%d') # this will be default 
            games = nba.get_games_for_date()            # but toggleable to other dates
            if games != []:
                for each in games:
                    new = NBAScoreBoard(
                        game_id=each['GAME_ID'],
                        team_abbr=each['TEAM_ABBREVIATION'],
                        team_city_name=each['TEAM_CITY_NAME'],
                        team_name=each['TEAM_NAME'],
                        record=each['TEAM_WINS_LOSSES'],
                        quarter_scores=each['quarter_scores'],
                    )
                    db.session.add(new)
                    db.session.commit()                
        return {
            'scorebord': NBAScoreBoard.query.all()

            }

    def update():
        return {
            'nba': Actions.updateNBA()
        }