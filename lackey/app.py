import json
from flask import Flask, render_template
from flask_restful import Api

from lackey import get_root_path
# app
app = Flask(__name__, static_folder=get_root_path('frontend/build/static'), template_folder=get_root_path('frontend/build'))

from lackey import api_views # api (uses db/models)
from lackey.api_views import calendar, weather

api = Api(app)
api.add_resource(calendar.CALENDAR, '/Calendar/<action>') # calendar specifc api calls
api.add_resource(weather.WEATHER, '/Weather/<action>') # general api calls/actions

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/', methods=['GET'])
def landing():
    return render_template('index.html')
