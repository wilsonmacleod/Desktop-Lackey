import requests
import json

import pandas as pd

from .sport_urls import Soccer_Urls as Urls

## HIGHLIGHT EMBEDDER?
##'https://www.scorebat.com/video-api/'

# https://www.football-data.org/documentation/quickstart

def get_comp_info(comp='PL'):
    """
    get general competition info for 
    macthday scoreboard and UI
    """
    url = Urls.urls_('matches', comp)
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
        score = each['score']
        obj = {
            'competition': str(comp),
            'matchday': str(matchday),
            'home_team':  str(each['homeTeam']['name']),
            'away_team': str(each['awayTeam']['name']),
            'data': {
                'status': str(each['status']),
                'winner': str(score['winner']),
                'duration': str(score['duration']),
                'fullTime': {'home': str(score['fullTime']['homeTeam']), 'away': str(score['fullTime']['awayTeam'])},
                'halfTime': {'home': str(score['halfTime']['homeTeam']), 'away': str(score['halfTime']['awayTeam'])},
                'extraTime': {'home': str(score['extraTime']['homeTeam']), 'away': str(score['extraTime']['awayTeam'])},
                'penalties': {'home': str(score['penalties']['homeTeam']), 'away': str(score['penalties']['awayTeam'])},
            }
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
    headers = Urls.headers()
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
