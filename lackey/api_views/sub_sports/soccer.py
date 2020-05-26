from lackey.models import (
    db, 
    SoccerScoreboard, EPLTable, SoccerTopScorers
    )
from lackey.external_apis.sports import soccer
from lackey.api_views import sports as api_view

def scoreboard():
    scoreboard = SoccerScoreboard.query.all()
    if api_view.Actions.checkIfUpdate(scoreboard):
        comp_info = soccer.get_comp_info() # arg for leagues can be here
        scoreboard = soccer.fixture_list(comp_info['matchday'], comp_info['code'])
        if scoreboard != []:
            SoccerScoreboard.query.delete() 
            for each in scoreboard:
                new = SoccerScoreboard(
                    competition=comp_info['name'],
                    matchday=each['matchday'],
                    home_team=each['home_team'],
                    away_team=each['away_team'],
                    data=str(each['data'])
                )
                db.session.add(new)
                db.session.commit()   
    else:
        clean_data = []
        for each in scoreboard:
            clean_data.append(api_view.Actions.clean_string_dict(each, 'data'))
        scoreboard = clean_data
    return scoreboard    

def standings(): 
    standings = EPLTable.query.all()
    if api_view.Actions.checkIfUpdate(standings):
        standings = soccer.get_PL_table()
        if standings != []: 
            EPLTable.query.delete() 
            for each in standings:
                new = EPLTable(
                    rank=each['position'],
                    team=each['team'],
                    crest=each['crest'],
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
    leaders = SoccerTopScorers.query.all()
    if api_view.Actions.checkIfUpdate(leaders):
        comp_info = soccer.get_comp_info()
        leaders = soccer.get_top_scorers(comp_info['code'])
        if leaders != []: 
            SoccerTopScorers.query.delete() 
            for each in leaders:
                new = SoccerTopScorers(
                    competition=comp_info['name'],
                    name=each['name'],
                    nationality=each['nationality'],
                    team=each['team'],
                    number_goals=each['numberOfGoals']
                )
                db.session.add(new)
                db.session.commit()  
    return leaders

def refreshScoreboard():
    SoccerScoreboard.query.delete()

def updateSoccer(): #PL exclusive for now
    return {
        'scoreboard': scoreboard(),
        'standings': standings(),
        'leaders': leaders()
    }
