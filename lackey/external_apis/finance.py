# https://www.alphavantage.co/documentation/
# key = R68BP5MK5TL0KDXQ

def urls(name, keywords, key):
    """
    https://www.alphavantage.co/documentation/
    """
    url_dict = {
        'search': f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={key}', # Search Endpoint
        'default': f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={keywords}&interval=60min&apikey={key}', # TIME_SERIES_INTRADAY
        'daily_compact': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={keywords}&apikey={key}', # TIME_SERIES_DAILY
        'daily_full': f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={keywords}&outputsize=full&apikey={key}', # TIME_SERIES_DAILY
    }
    return url_dict[name] 

def search_fund(query):
    keywords= query
    key = 'R68BP5MK5TL0KDXQ' ### 
    url = urls('search', keywords, key)
    
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
    
def main_get(url_name, stock_symbol):
    """
    gets daily info for 
    'url_name' args should be:
    a) default (most recent 100 data point by 60 min intervals)
    b) daily_compact (last 100 data points by day intervals)
    c) daily_full (all info available (20+ years) by day intervals)
    """
    name = url_name
    keywords= stock_symbol
    key = 'R68BP5MK5TL0KDXQ' ### 
    url = urls(name, keywords, key)
    
    r = requests.get(url)
    if r.status_code == 200:
        data_key = json_key_resolver(url_name)
        results = json.loads(r.text)
        final_json = [{'Meta Data': results['Meta Data']}]
        results = results[data_key]
        for each in results:
            obj = {
            'date': each,
            'open': results[each]['1. open'],
            'high': results[each]['2. high'],
            'low': results[each]['3. low'],
            'close': results[each]['4. close']
            }
            final_json.append(obj)
        return final_json
        