import requests
import json
import xmltodict

import NFL_Urls from sport_urls as Urls
"""
very unstable and hacky 
since there are no official APIs
see *** https://stackoverflow.com/a/59970147 ***
"""

def get_current_week():
    url = Urls.urls('currentWeek')
    r = requests.get(url=url).json()
    return r # {'seasonId': ##, 'seasonType': ##, 'week': ##}

def get_game_ids(season, seasonType, week):
    url = Urls.urls('week') + f'season={season}&seasonType={seasonType}&week={week}'
    # test 'http://www.nfl.com/ajax/scorestrip?season=2019&seasonType=REG&week=16'
    r = requests.get(url=url)
    xml_parsed = xmltodict.parse(r.text)
    to_json = json.dumps(xml_parsed)
    json_obj = json.loads(to_json)
    games = json_obj['ss']['gms']['g']
                    ### can get game times and dates here if wanted
    game_ids = []
    if type(games) == list:
        for each in games:
            game_ids.append(each['@eid'])
    else:
        game_ids.append(games['@eid'])
    return game_ids # list of game ids,
                    # can turn into dict and include 
                    #  game times and dates here if wanted

def get_games(game_ids):
    final_json = []
    for each in game_ids:
        url = Urls.urls('liveupdate') + f'{each}/{each}_gtd.json'
        r = requests.get(url=url).json()
        game = r[str(each)]
        game_dict = {
            'home_team': game['home']['abbr'],
            'home_box_score': game['home']['score'],
            'away_team': game['away']['abbr'],
            'away_box_score': game['away']['score'],
            'poss': game['posteam'],
            'time_rem': game['clock'],
            'qtr': game['qtr'],
            'rz': game['redzone']
        }
        final_json.append(game_dict)
    return final_json

def main_scoreboard(): # will need to implement switch for customer lookups
    info_dict = get_current_week()
    season = info_dict['seasonId']
    seasonType = info_dict['seasonType']
    week = info_dict['week']
    gids = get_game_ids(season, seasonType, week)
    scoreboard = get_games(gids)
    return scoreboard
    ## EXAMPLE scoreboard:
#[{'home_team': 'KC',
  #'home_box_score': {'1': 7, '2': 3, '3': 0, '4': 21, '5': 0, 'T': 31},
  #'away_team': 'SF',
  #'away_box_score': {'1': 3, '2': 7, '3': 10, '4': 0, '5': 0, 'T': 20},
  #'poss': 'SF',
  #'time_rem': '00:00',
  #'qtr': 'Final',
  #'rz': True}]
  