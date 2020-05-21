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
        obj = {
            'competition': str(comp),
            'matchday': str(matchday),
            'home_team':  str(each['homeTeam']['name']),
            'away_team': str(each['awayTeam']['name']),
            'data': {
                'status': str(each['status']),
                'winner': str(each['score']['winner']),
                'duration': str(each['score']['duration']),
                'fullTime': f"home:{each['score']['fullTime']['homeTeam']},away:{each['score']['fullTime']['awayTeam']}",
                'halfTime': f"home:{each['score']['halfTime']['homeTeam']},away:{each['score']['halfTime']['awayTeam']}",
                'extraTime': f"home:{each['score']['extraTime']['homeTeam']},away:{each['score']['extraTime']['awayTeam']}",
                'penalties': f"home:{each['score']['penalties']['homeTeam']},away:{each['score']['penalties']['awayTeam']}",
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
