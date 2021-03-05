import os
from dotenv import load_dotenv
load_dotenv()

def get_env_value(env_variable):
    try:
        return os.getenv(env_variable)
    except Exception as e:
        error_msg = f'Set the {var_name} environment variable in .env!'
        logger.info(error_msg)

APP_NAME = "Lackey"
APP_NAME_NO_SPACE = APP_NAME.replace(' ', '')
APP_VERSION = '1.00'
APP_DESCRIPTION = "Lower my Chrome tab count, Flask-based desktop application with React frontend"
COMPANY_NAME = "MacLeod"
WEBSITE = "https://wilsonmacleod.com/"


NBA_SEASON = "2019-20" ##
API_KEYS = {
    'finance_key': get_env_value('FINANCE_KEY') ##
    'soccer_key': get_env_value('SOCCER_KEY')
}
