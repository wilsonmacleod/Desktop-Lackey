import requests
import json

import datetime
import pandas as pd

from .sport_urls import NBA_Urls as Urls

## TODO
## SEASON RESOLUTION (2019-20)

def convert_quarters(string):
    r = int(string[-1])
    if string[-3:-1] == "OT":
        r += 4
    return r

def get_games_for_date(date):
    url = Urls.scoreboard_url(date)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    column_headers = r['resultSets'][1]['headers']
    data = r['resultSets'][1]['rowSet']
    df = pd.DataFrame(data, columns=column_headers)
    df.drop(df.columns[[0,1,3,21,22,23,24,25,26,27,28]], axis=1, inplace=True)
    df = df.fillna(0)

    obj = df.to_dict(orient='records')
    game_details = [
            'GAME_ID', 
            'TEAM_ABBREVIATION', 
            'TEAM_CITY_NAME', 
            'TEAM_NAME',
            'TEAM_WINS_LOSSES'
                    ]
    final_json = []
    for each in obj:
        quarter_scores = {convert_quarters(k):v for k,v in each.items() if k not in game_details}
        game = {k:v for k,v in each.items() if k in game_details}
        game['quarter_scores'] = str(quarter_scores)
        final_json.append(game)
    return final_json

def create_df(r):
    column_headers = r['resultSets'][0]['headers']
    data = r['resultSets'][0]['rowSet']
    return pd.DataFrame(data, columns=column_headers)    

def get_standings(season='2019-20'):
    url = Urls.leaguestandings(season)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    league = create_df(r)
    drop_range = range(20, 81)
    league.drop(league.columns[drop_range], axis=1, inplace=True)
    league.drop(league.columns[[0,1,2,7,12,13,15]], axis=1, inplace=True)
    league = league.reset_index()
    league = league.to_dict(orient='records')
    final_json = []
    specific = [
                'index', 
                'TeamName',
                'TeamCity', 
                'Conference'
                    ]
    for each in league:
        data = {k:v for k,v in each.items() if k not in specific}
        specifics = {k:v for k,v in each.items() if k in specific}
        specifics['data'] = data
        final_json.append(specifics)
    return final_json
 
# PlayerScope = ^(All+Players)|(Rookies)$
# Season needs to be current automatically
# StatCategory = (Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Efficiency)|
def get_leaders(scope='All+Players', season='2019-20', category='Points'):  
    url = Urls.leaders(scope, season, category)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    df = create_df(r)
    drop_dict = {
        'Points': [1,3,5,10,11,12],
        'Rebounds': [1,3,5,9,10,11],
        'Assists': [1,3,5,8,9,10],
        'Defense': [1,3,5,9,10,11,12],
        'Clutch': [1,3,5,11,12],
        'Efficiency': [1,3,5,6,7]
    }
    df.drop(df.columns[drop_dict[category]], axis=1, inplace=True)
    obj = df.to_dict(orient='records')
    player_details = [
                'RANK', 
                'PLAYER', 
                'TEAM_ABBREVIATION', 
                    ]
    final_json = []
    for each in obj:
        stats = {k:v for k,v in each.items() if k not in player_details}
        player = {k:v for k,v in each.items() if k in player_details}
        player['stats'] = stats
        player['category'] = category
        final_json.append(player)
    return final_json

if __name__ == "__main__":
    x = get_leaders() 
    print(x)