import requests
import json
import datetime
import locale

# https://www.metaweather.com/api/

urls = {
    'query_url': 'https://www.metaweather.com/api/location/search/?query=', #+{query}
    'location_url': 'https://www.metaweather.com/api/location/', #+{woied}/
    'icons': 'https://www.metaweather.com/static/img/weather/', #+{each["weather_state_abbr"]}.svg',
    'date': 'https://www.metaweather.com/api/location/' #+{woied}/{today}

}

def return_object(result, woied):
    final_json = []
    for each in result:
        obj = {
            'date': each['applicable_date'],
            'weather_state_name': each['weather_state_name'],
            'icon_link': urls['icons'] + f'{each["weather_state_abbr"]}.svg',
            'min_temp': round(((float(each['min_temp']) * 9/5) + 32), 2), # F
            'max_temp': round(((float(each['max_temp']) * 9/5) + 32), 2), # F
            'humidity': each['humidity'], # %
            'wind_speed': each['wind_speed'],
            'predictability': each['predictability'],
            'woied': woied        
        }
        final_json.append(obj)
    return final_json 

def fix_today(result, woied):
    result = result[:-1]
    today = datetime.datetime.today().strftime('%Y/%m/%d')
    url = urls['date'] + f'{woied}/{today}'
    r = requests.get(url)
    todays_data = json.loads(r.text)[0]
    result.insert(0,todays_data)
    return return_object(result, woied)

def search_city(query):
    """
    returns obj of weather data
    input is str e.x 'Seattle', 
    finds id and querys api
    """
    url = urls['query_url'] + f'{query}'
    r = requests.get(url)
    if r.status_code == 200:
        woied = json.loads(r.text)#[0]['woied']
    else: 
        return "API down, (response status code != 200)"
    return woied #return_weather_data(woied) 
    # ex
    #[{'title': 'Seattle', 
    # 'location_type': 'City', 
    # 'woied': 2490383, 
    # 'latt_long': '47.603561,-122.329437'}]

def return_weather_data(woied):
    url = urls['location_url'] + f'{woied}'
    r = requests.get(url)
    result = json.loads(r.text)['consolidated_weather']
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')  
    first_date_returned = datetime.datetime.strptime(result[0]['applicable_date'], '%Y-%m-%d')
    if first_date_returned > datetime.datetime.today():
        return fix_today(result, woied)
    else:
        return return_object(result, woied)

## returns
#    [{'date': '2020-05-03',
#  'weather_state_name': 'Showers',
#  'icon_link': 'https://www.metaweather.com/static/img/weather/s.svg',
#  'min_temp': 49.87,
#  'max_temp': 57.61,
#  'humidity': 59,
#  'wind_speed': 2.492696945348498,
#  'predictability': 73},
#
## + 4 days in future