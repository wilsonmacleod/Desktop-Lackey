import requests
import json

"""
only GW2 fractals timers for now
"""

def urls(url_name):
    url_dict = {
        'dailys': 'https://api.guildwars2.com/v2/achievements/daily', #'/tomorrow'
        'resolve_dailys': 'https://api.guildwars2.com/v2/achievements?' #+ids={ids}'
    }
    return url_dict[url_name]

def return_obj(ids):
    url = urls('resolve_dailys') + f'ids={ids}'
    r = requests.get(url=url).json()
    dailys = [
        r[6]['name'],
        r[10]['name'],
        r[14]['name']
        ]
    return dailys

def get(flag): # flag True = today, False = tom.
    if flag:
        url = urls('dailys')
    else:
        url = urls('dailys') + '/tomorrow'
    r = requests.get(url=url).json()
    id_list = [i['id'] for i in r['fractals']]
    ids = str(id_list).strip(']').strip('[').replace(" ", "")
    return return_obj(ids)

def main():
    today = get(True)
    tomorrow = get(False)
    return today, tomorrow
    # EXAMPLE
    #(['Daily Tier 4 Chaos',
  #'Daily Tier 4 Uncategorized',
  #'Daily Tier 4 Urban Battleground'],
 #['Daily Tier 4 Deepstone',
  #"Daily Tier 4 Siren's Reef",
  #'Daily Tier 4 Molten Furnace'])