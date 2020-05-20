import requests
import json

import pandas as pd

from sport_urls import Soccer_Urls as Urls

## HIGHLIGHT EMBEDDER?
##'https://www.scorebat.com/video-api/'

# https://www.football-data.org/documentation/quickstart

def get_comp_info(comp='PL'):
    """
    get general competition info for 
    macthday scoreboard and UI
    """
    urls = Urls.urls_('matches', comp)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    current_matchday = r['matches'][0]['season']['currentMatchday']
    stage = r['matches'][0]['stage']
    comp_info = r['competition']
    return {
        'name': comp_info['name'],
        'code': comp_info['code'],
        'matchday': current_matchday,
        'stage': stage,
        'pulled': comp_info['lastUpdated']
    }

def fixture_list(matchday, comp='PL'):
    """
    get matches and match details
    for specificied matchday
    """
    url = Urls.urls_('matches', comp) + f'?matchday={matchday}'
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    
    final_json = []
    for each in r['matches']:
        obj = {
            'home_team':  each['homeTeam']['name'],
            'away_team': each['awayTeam']['name'],
            'status': each['status'],
            'winner': each['score']['winner'],
            'duration': each['score']['duration'],
            'fullTime': each['score']['fullTime'],
            'halfTime': each['score']['halfTime'],
            'extraTime': each['score']['extraTime'],
            'penalties': each['score']['penalties'],
        }
        final_json.append(obj)
    return final_json

def get_PL_table():
    """
    returns table for PL
    """
    url = Urls.urls_('table', "PL")
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    table = r['standings'][0]['table']

    df_data = []
    for each in table:
        obj = {
            'position': each['position'],
            'team': each['team']['name'],
            'crest': each['team']['crestUrl'],
            'playedGames': each['playedGames'],
            'won': each['won'],
            'draw': each['draw'],
            'lost': each['lost'],
            'points': each['points'],
            'goalsFor': each['goalsFor'],
            'goalsAgainst': each['goalsAgainst'],
            'goalDifference': each['goalDifference'],
        }
        df_data.append(obj)

    return pd.DataFrame(df_data)

def get_top_scorers(comp='PL'):
    """
    returns table of comp top scorers
    """
    url = Urls.urls_('scorers', comp)
    headers = Urls.headers()
    r = requests.get(url=url, headers=headers).json()
    table = r['scorers']

    df_data = []
    for each in table:
        obj = {
            'name': each['player']['name'],
            'nationality': each['player']['nationality'],
            'team': each['team']['name'],
            'numberOfGoals': each['numberOfGoals'],
            }
        df_data.append(obj)

    return pd.DataFrame(df_data)

def main(comp='PL'): #can add UCL to this or other comps
    comp_info = get_comp_info(comp)
    fixture_list = fixture_list(comp_info['matchday'])
    table = get_PL_table()
    scorers = get_top_scorers(comp)
    return {
        'competition': comp_info,
        'fixtures': fixture_list,
        'table': table,
        'scorers': scorers
    }