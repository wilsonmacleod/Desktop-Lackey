import json
from datetime import datetime as dt
import locale

from lackey import logger
from lackey.models import (
    db, 
    NBAScoreBoard, NBAStandings, NBALeaders
    )
from lackey.external_apis.sports import nba
from lackey.api_views import sports as api_view

def updateNBA():
    logger.debug(f'checkNBA')

    scoreboard = NBAScoreBoard.query.all()
    if api_view.Actions.checkIfUpdate(scoreboard):
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')
        test_day = dt.strptime('2020-03-11', '%Y-%m-%d') # this will be default 
        scoreboard = nba.get_games_for_date(test_day)            # but toggleable to other dates
        if scoreboard != []:
            NBAScoreBoard.query.delete() 
            for each in scoreboard:
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

    standings = NBAStandings.query.all()
    if api_view.Actions.checkIfUpdate(standings):
        standings = nba.get_standings()
        if standings != []: 
            NBAStandings.query.delete() 
            for each in standings:
                new = NBAStandings(
                    rank=each['index'],
                    team_city=each['TeamCity'],
                    team_name=each['TeamName'],
                    conference=each['Conference'],
                    data=str(each['data'])
                )
                db.session.add(new)
                db.session.commit()
    else:
        clean_data = []
        for each in standings:
            clean = dict(each.__dict__)
            clean.pop('_sa_instance_state', None)
            clean['data'] = json.loads(clean['data'].replace("'", '"')) 
            clean_data.append(clean)
        standings = clean_data

    leaders = NBALeaders.query.all()
    if api_view.Actions.checkIfUpdate(leaders):
        leaders = nba.get_leaders()
        if leaders != []: 
            NBAStandings.query.delete() 
            for each in leaders:
                new = NBALeaders(
                    category=each['category'],
                    rank=each['RANK'],
                    player=each['PLAYER'],
                    team_abbr=each['TEAM_ABBREVIATION'],
                    stats=str(each['stats'])
                )
                db.session.add(new)
                db.session.commit()  
    else:
        clean_stats = []
        for each in leaders:
            clean = dict(each.__dict__)
            clean.pop('_sa_instance_state', None)
            clean['stats'] = json.loads(clean['stats'].replace("'", '"')) 
            clean_stats.append(clean)
        leaders = clean_stats
        
    return {
        'scorebord': scoreboard,
        'standings': standings,
        'leaders': leaders
        }