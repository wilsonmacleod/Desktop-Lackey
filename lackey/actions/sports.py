import requests
import json

import pandas as pd

class Urls():
    def headers():
        return {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'x-nba-stats-origin': 'stats',
        'x-nba-stats-token': 'true'
        }

    def scoreboard_url(date):
        #https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/scoreboardv2.md
        return f"https://stats.nba.com/stats/scoreboardv2?DayOffset=0&GameDate={date}&LeagueID=00"
    
    def leaguestandings(season):
        #https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/leaguestandings.md
        return f'https://stats.nba.com/stats/leaguestandings?LeagueID=00&Season={season}&SeasonType=Regular+Season&SeasonYear=' ###
    
    def leaders(scope, season, category):
        #https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/homepageleaders.md
        return f'https://stats.nba.com/stats/homepageleaders?GameScope=Season&LeagueID=00&PlayerOrTeam=Player&PlayerScope={scope}&Season={season}&SeasonType=Regular+Season&StatCategory={category}'


def get_games_for_date(date='2020-03-11'): # default = today
    date = '2020-03-11'
    url = Urls.scoreboard_url(date)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        r = r.json()
        column_headers = r['resultSets'][1]['headers']
        data = r['resultSets'][1]['rowSet']
        df = pd.DataFrame(data, columns=column_headers)
        df.drop(df.columns[[0,1,3,21,22,23,24,25,26,27,28]], axis=1, inplace=True)
        return df
    else:
        return "API DOWN :/"

def create_df(r):
    r = r.json()
    column_headers = r['resultSets'][0]['headers']
    data = r['resultSets'][0]['rowSet']
    return pd.DataFrame(data, columns=column_headers)    

def get_standings(season="2019-20"): # season needs to be current automatically
    url = Urls.leaguestandings(season)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        league = create_df(r)
        drop_range = range(20, 81)
        league.drop(league.columns[drop_range], axis=1, inplace=True)
        league.drop(league.columns[[0,1,2,7,12,13,15]], axis=1, inplace=True)
        east = league[league['Conference'] == 'East'].reset_index()
        west = league[league['Conference'] == 'West'].reset_index()
        return {'league': league, 'east': east, 'west': west}
    else:
        return "API DOWN :/"

## Args: 
# PlayerScope = ^(All+Players)|(Rookies)$
 # Season needs to be current automatically
# StatCategory = (Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Efficiency)|
def leaders(scope='All+Players', season='2019-20', category='Points'):  
    url = Urls.leaders(scope, season, category)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
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
    else:
        return "API DOWN :/"