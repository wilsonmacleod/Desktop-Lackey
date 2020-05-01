import datetime

def today():
    now = datetime.datetime.now()
    return now.strftime("%a, %b %d, %Y")