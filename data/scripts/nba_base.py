import requests
import json

import pandas as pd

def team_ids_resolved():
    url = 'https://stats.nba.com/stats/leaguestandings?LeagueID=00&Season=2019-20&SeasonType=Regular+Season&SeasonYear='
    response = requests.get(url=url, headers=headers).json()
    column_headers = response['resultSets'][0]['headers']
    data = response['resultSets'][0]['rowSet']
    df = pd.DataFrame(data, columns=column_headers)

    resolved_ids = {}
    for column, row in df.iterrows():
        resolved_ids[row['TeamID']] = {
                'city': row['TeamCity'],
                'name': row['TeamName'],
                }
    return resolved_ids

## resolved_ids = 
#{1610612749: {'city': 'Milwaukee', 'name': 'Bucks'},
# 1610612747: {'city': 'Los Angeles', 'name': 'Lakers'},
# 1610612761: {'city': 'Toronto', 'name': 'Raptors'},
# 1610612746: {'city': 'LA', 'name': 'Clippers'},
# 1610612743: {'city': 'Denver', 'name': 'Nuggets'},
# 1610612738: {'city': 'Boston', 'name': 'Celtics'},
# 1610612762: {'city': 'Utah', 'name': 'Jazz'},
# 1610612748: {'city': 'Miami', 'name': 'Heat'},
# 1610612760: {'city': 'Oklahoma City', 'name': 'Thunder'},
# 1610612754: {'city': 'Indiana', 'name': 'Pacers'},
# 1610612755: {'city': 'Philadelphia', 'name': '76ers'},
# 1610612745: {'city': 'Houston', 'name': 'Rockets'},
# 1610612742: {'city': 'Dallas', 'name': 'Mavericks'},
# 1610612751: {'city': 'Brooklyn', 'name': 'Nets'},
# 1610612753: {'city': 'Orlando', 'name': 'Magic'},
# 1610612763: {'city': 'Memphis', 'name': 'Grizzlies'},
# 1610612764: {'city': 'Washington', 'name': 'Wizards'},
# 1610612757: {'city': 'Portland', 'name': 'Trail Blazers'},
# 1610612740: {'city': 'New Orleans', 'name': 'Pelicans'},
# 1610612766: {'city': 'Charlotte', 'name': 'Hornets'},
# 1610612741: {'city': 'Chicago', 'name': 'Bulls'},
# 1610612758: {'city': 'Sacramento', 'name': 'Kings'},
# 1610612759: {'city': 'San Antonio', 'name': 'Spurs'},
# 1610612752: {'city': 'New York', 'name': 'Knicks'},
# 1610612765: {'city': 'Detroit', 'name': 'Pistons'},
# 1610612756: {'city': 'Phoenix', 'name': 'Suns'},
# 1610612750: {'city': 'Minnesota', 'name': 'Timberwolves'},
# 1610612737: {'city': 'Atlanta', 'name': 'Hawks'},
# 1610612744: {'city': 'Golden State', 'name': 'Warriors'},
# 1610612739: {'city': 'Cleveland', 'name': 'Cavaliers'}}