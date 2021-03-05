import requests
import json

import pandas as pd

from lackey import logger

from lackey.__info__ import API_KEYS
from .sport_urls import Soccer_Urls as Urls

## HIGHLIGHT EMBEDDER?
##'https://www.scorebat.com/video-api/'

# https://www.football-data.org/documentation/quickstart

headers = API_KEYS['soccer_key']

def get_comp_info(comp='PL'):
    """
    get general competition info for 
    macthday scoreboard and UI
    """
    url = Urls.urls_('matches', comp)
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

def replace(x):
    if x == 'None' or x is None:
        return 0
    else:
        return x

def fixture_list(matchday, comp='PL'):
    """
    get matches and match details
    for specificied matchday
    """
    url = Urls.urls_('matches', comp) + f'?matchday={matchday}'
    r = requests.get(url=url, headers=headers).json()
    
    final_json = []
    for each in r['matches']:
        score = each['score']
        obj = {
            'competition': str(comp),
            'matchday': str(matchday),
            'home_team':  str(each['homeTeam']['name']),
            'away_team': str(each['awayTeam']['name']),
            'data': {
                'date': str(each['utcDate'][0:10]),
                'status': str(each['status']),
                'winner': str(score['winner']),
                'duration': str(score['duration']),
                'fullTime': {'home': replace(score['fullTime']['homeTeam']), 'away': replace(score['fullTime']['awayTeam'])},
                'halfTime': {'home': replace(score['halfTime']['homeTeam']), 'away': replace(score['halfTime']['awayTeam'])},
                'extraTime': {'home': replace(score['extraTime']['homeTeam']), 'away': replace(score['extraTime']['awayTeam'])},
                'penalties': {'home': replace(score['penalties']['homeTeam']), 'away': replace(score['penalties']['awayTeam'])},
            }
        }
        obj['data'] = replace(obj['data'])
        final_json.append(obj)
    return final_json

def get_PL_table():
    """
    returns table for PL
    """
    url = Urls.urls_('table', "PL")
    r = requests.get(url=url, headers=headers).json()
    table = r['standings'][0]['table']

    final_json = []
    for each in table:
        obj = {
            'position': each['position'],
            'team': each['team']['name'],
            'crest': each['team']['crestUrl'],
            'data': {
                'playedGames': each['playedGames'],
                'won': each['won'],
                'draw': each['draw'],
                'lost': each['lost'],
                'points': each['points'],
                'goalsFor': each['goalsFor'],
                'goalsAgainst': each['goalsAgainst'],
                'goalDifference': each['goalDifference']
            }
        }
        final_json.append(obj)
    return final_json

def get_top_scorers(comp='PL'):
    """
    returns table of comp top scorers
    """
    url = Urls.urls_('scorers', comp)
    r = requests.get(url=url, headers=headers).json()
    table = r['scorers']

    final_json = []
    for each in table:
        obj = {
            'name': each['player']['name'],
            'nationality': each['player']['nationality'],
            'team': each['team']['name'],
            'numberOfGoals': each['numberOfGoals'],
            }
        final_json.append(obj)
    return final_json
