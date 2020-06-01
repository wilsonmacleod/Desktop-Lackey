# https://www.alphavantage.co/documentation/
import json
import requests

from lackey import logger

from lackey.__info__ import API_KEYS

def urls(name, keywords):
    key = API_KEYS['finance_key']
    """
    https://www.alphavantage.co/documentation/
    """
    url_dict = {
        'search': f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={key}', # Search Endpoint
        'default': f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={keywords}&interval=60min&outputsize=full&apikey={key}', # TIME_SERIES_INTRADAY
        'daily_compact': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={keywords}&apikey={key}', # TIME_SERIES_DAILY
        'daily_full': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={keywords}&outputsize=full&apikey={key}', # TIME_SERIES_DAILY
    }
    return url_dict[name] 

def search_fund(query):
    keywords= query
    url = urls('search', keywords)
    
    r = requests.get(url)
    if r.status_code == 200:
        results = json.loads(r.text)
        final_json = []
        for each in results['bestMatches']:
            obj = {
                'stock_symbol': each['1. symbol'],
                'name': each['2. name'],
                'type': each['3. type'],
                'region': each['4. region'],
                'currency': each['8. currency']
            }
            final_json.append(obj)
        # stock_symbol = search_fund('VTSAX')[0]['stock_symbol'];
        return final_json
    else:
        return "API down, response != 200"

def json_key_resolver(url_name):
    translate = {
        'default': 'Time Series (60min)',
        'daily_compact': 'Time Series (Daily)',
        'daily_full': 'Time Series (Daily)',
    }
    return translate[url_name]
    
def get(url_name, stock_symbol):
    """
    gets daily info for 
    'url_name' args should be:
    a) default (most recent 100 data point by 60 min intervals)
    b) daily_compact (last 100 data points by day intervals)
    c) daily_full (all info available (20+ years) by day intervals)
    """
    name = url_name
    keywords= stock_symbol
    url = urls(name, keywords)
    
    r = requests.get(url)
    if r.status_code == 200:
        data_key = json_key_resolver(url_name)
        results = json.loads(r.text)
        results = results[data_key]
        final_json = []
        for key, value in results.items():
            obj = {
            'stock_symbol': stock_symbol,
            'date': key,
            'open': value['1. open'],
            'high': value['2. high'],
            'low': value['3. low'],
            'close': value['4. close']
            }
            final_json.append(obj)
        index = 0
        for each in final_json:
            try:
                new = float(final_json[index]['close'])
                old = float(final_json[index + 1]['close'])
                if new > old:
                    x = '+'
                    change = (((new - old) / old) *  100)
                else:
                    x = '-'
                    change = (((old - new) / old) *  100)
                change = round(change, 2)

            except IndexError:
                x = 'N/A'
                change = ''
            final_json[index]['change'] = f'{x},{change}'
            index += 1
        return final_json
        