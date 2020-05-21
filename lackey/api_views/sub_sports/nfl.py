from lackey.models import db, NFLScoreBoard
from lackey.external_apis.sports import nfl
from lackey.api_views import sports as api_view

# relies on hidden espn api
# NFL killed the original :/ 

def checkWeek(stored_week):
    this_week = nfl.return_week()
    if not stored_week: # if nothing in DB
        return True
    elif stored_week != this_week: # if ood in DB
        return True
    else: # if up to date
        return False

def updateNFL():
    try:
        stored_week = NFLScoreBoard.query.first().current_week
    except AttributeError:
        stored_week = False 
    if checkWeek(stored_week): # if not current week update
        NFLScoreBoard.query.delete() 
        scoreboard = nfl.return_scoreboard()
        for each in scoreboard:
            new = NFLScoreBoard(
                season=each['season'],
                current_week=each['current_week'],
                time_date=each['time_date'],
                home_team=each['home_team'],
                away_team=each['away_team'],
                data=str(each['data'])
            )
            db.session.add(new)
            db.session.commit()   
    else:
        scoreboard = NFLScoreBoard.query.all()
        clean_stats = []
        for each in scoreboard:
            data = api_view.Actions.clean_string_dict(each, 'data')
            clean_stats.append(data)
        scoreboard = clean_stats
    return {
        'scoredboard': scoreboard
    }
