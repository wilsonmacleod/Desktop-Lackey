import requests
import json

import datetime
import pandas as pd

from sport_urls import NBA_Urls as Urls

"""
NEED TO FIGURE OUT 
SEASON RESOLUTION (2019-20)
"""

today = datetime.datetime.today().strftime('%Y-%m-%d')
def get_games_for_date(date=today): # default = today
    url = Urls.scoreboard_url(date)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    column_headers = r['resultSets'][1]['headers']
    data = r['resultSets'][1]['rowSet']
    df = pd.DataFrame(data, columns=column_headers)
    df.drop(df.columns[[0,1,3,21,22,23,24,25,26,27,28]], axis=1, inplace=True)
    df['link'] = "linked"
    return df

def create_df(r):
    column_headers = r['resultSets'][0]['headers']
    data = r['resultSets'][0]['rowSet']
    return pd.DataFrame(data, columns=column_headers)    

def get_standings(season='2019-20'): # season needs to be current automatically
    url = Urls.leaguestandings(season)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    league = create_df(r)
    drop_range = range(20, 81)
    league.drop(league.columns[drop_range], axis=1, inplace=True)
    league.drop(league.columns[[0,1,2,7,12,13,15]], axis=1, inplace=True)
    east = league[league['Conference'] == 'East'].reset_index()
    west = league[league['Conference'] == 'West'].reset_index()
    return {'league': league, 'east': east, 'west': west}

## Args: 
# PlayerScope = ^(All+Players)|(Rookies)$
 # Season needs to be current automatically
# StatCategory = (Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Efficiency)|
def leaders(scope='All+Players', season='2019-20', category='Points'):  
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
    return df
