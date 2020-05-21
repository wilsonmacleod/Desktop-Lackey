from datetime import datetime as dt
import locale

from lackey.models import (
    db, 
    NBAScoreBoard, NBAStandings, NBALeaders
    )
from lackey.external_apis.sports import nba
from lackey.api_views import sports as api_view


def scoreboard():
    scoreboard = NBAScoreBoard.query.all()
    if api_view.Actions.checkIfUpdate(scoreboard):
        locale.setlocale(locale.LC_ALL, 'en_US.utf8')
        test_day = dt.strptime('2020-03-11', '%Y-%m-%d') # this will be default (today)
        scoreboard = nba.get_games_for_date(test_day) # but toggleable to other dates
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
    return scoreboard    

def standings():
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
            clean_data.append(api_view.Actions.clean_string_dict(each, 'data'))
        standings = clean_data
    return standings

def leaders():
    leaders = NBALeaders.query.all()
    if api_view.Actions.checkIfUpdate(leaders):
        leaders = nba.get_leaders()
        if leaders != []: 
            NBALeaders.query.delete() 
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
            clean_stats.append(api_view.Actions.clean_string_dict(each, 'stats'))
        leaders = clean_stats
    return leaders
        
def updateNBA():
    return {
        'scorebord': scoreboard(),
        'standings': standings(),
        'leaders': leaders()
        }