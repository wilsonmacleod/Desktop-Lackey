# https://www.alphavantage.co/documentation/
import json
import requests
import datetime

from lackey import logger

from lackey.__info__ import API_KEYS

def urls(name, keywords):
    key = API_KEYS['finance_key']
    """
    https://www.alphavantage.co/documentation/,
    https://docs.gemini.com/rest-api/
    """
    url_dict = {
        'search': f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={key}', # Search Endpoint
        'default': f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={keywords}&interval=60min&outputsize=full&apikey={key}', # TIME_SERIES_INTRADAY
        'daily_compact': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={keywords}&apikey={key}', # TIME_SERIES_DAILY
        'daily_full': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={keywords}&outputsize=full&apikey={key}', # TIME_SERIES_DAILY
        'search_crypto': f'https://api.gemini.com/v1/symbols/details/{keywords}',
        'get_crypto': f'https://api.gemini.com/v2/candles/{keywords}/1day'
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
        keywords = keywords.lower()+'usd' ## search Gemini crypto exchange
        url = urls('search_crypto', keywords)
        r = requests.get(url)
        if r.status_code == 200:
            r = r.json()
            obj = {
                'stock_symbol': keywords,
                'name': r['base_currency'],
                'type': 'Crypto Currency',
                'region': 'US',
                'currency': 'USD'
            }
            final_json.append(obj)
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

def calc_change(final_json):
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

def get(url_name, stock_symbol):
    """
    gets daily info for 
    'url_name' args should be:
    a) default (most recent 100 data point by 60 min intervals)
    b) daily_compact (last 100 data points by day intervals)
    c) daily_full (all info available (20+ years) by day intervals)
    """
    try:
        return crypto(stock_symbol)
    except:
        try:
            return traditional(url_name, stock_symbol)
        except Exception as e:
            raise Exception(f'{e}')

def traditional(url_name, stock_symbol):
    name = url_name
    keywords= stock_symbol
    url = urls(name, keywords)
    
    r = requests.get(url)
    if r.status_code == 200:
        data_key = json_key_resolver(url_name)
        results = json.loads(r.text)
        try:
            results = results[data_key]
        except KeyError:
            url = urls('daily_compact', keywords)
            r = requests.get(url)
            results = json.loads(r.text)
            results = results['Time Series (Daily)']
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
        return calc_change(final_json)

def crypto(stock_symbol):
    logger.info(f'crypto({stock_symbol})')
    url = urls('get_crypto', stock_symbol)
    r = requests.get(url)
    if r.status_code == 200:
        r = r.json()
        final_json = []
        for each in r:
            epoch = each[0] / 1000.0
            date = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')
            final_json.append({
                'stock_symbol': stock_symbol,
                'date': date,
                'open': each[1],
                'high': each[2],
                'low': each[3],
                'close': each[4],
            })
        return calc_change(final_json)
    else:
        raise Exception(f'external_apis/finance.py/def crypto could not find endpoint - {url}')
