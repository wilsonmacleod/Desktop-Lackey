import os

APP_NAME = "Lackey"
APP_NAME_NO_SPACE = APP_NAME.replace(' ', '')
APP_VERSION = '1.00'
APP_DESCRIPTION = "Lower my Chrome tab count, Flask-based desktop application with React frontend"
COMPANY_NAME = "MacLeod"
WEBSITE = "https://wilsonmacleod.com/"


NBA_SEASON = "2019-20" ##
API_KEYS = {
    'finance_key': os.environ.get('LACKEY_FINANCE_KEY') ##
}
