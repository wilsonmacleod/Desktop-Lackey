import requests

from .sport_urls import NFL_Urls as Urls

## https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b

# returns current week of NFL scoreboard
def return_week():
    url = Urls.urls()
    r = requests.get(url=url).json()
    return r['week']['number']

def return_scoreboard():
    url = Urls.urls()
    r = requests.get(url=url).json()
    final_json = []
    season = r['season']['year']
    week = r['week']['number']
    for each in r['events']:
        time_date = each['date']
        for e in each['competitions'][0]['competitors']:
            if e['homeAway'] == 'home':
                home_team=e['team']['displayName']
                home_team_score=e['score']
                home_team_color=e['team']['color']
                home_team_logo=e['team']['logo']
            elif e['homeAway'] == 'away':
                away_team=e['team']['displayName']
                away_team_score=e['score']
                away_team_color=e['team']['logo']
                away_team_logo=e['team']['logo']
            odds=each['competitions'][0]['odds'][0]['details']
            qtr=each['status']['period']
            time_date=each['status']['type']['detail']
            rem_time=each['status']['clock']
        obj = {
            'season': season,
            'current_week': week,
            'time_date': time_date,
            'home_team': home_team,
            'away_team': away_team,
            'data': {
                'home_team_score': home_team_score,
                'away_team_score': away_team_score,
                'odds': odds,
                'qtr': qtr,
                'rem_time': rem_time,
                'home_team_color': home_team_color,
                'home_team_logo': home_team_logo,
                'away_team_color': away_team_color,
                'away_team_logo': away_team_logo
            }
        }
        final_json.append(obj)
    return final_json