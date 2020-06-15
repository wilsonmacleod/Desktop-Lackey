import json
from flask import Flask, render_template
from flask_restful import Api

from lackey import get_root_path
# app
app = Flask(__name__, static_folder=get_root_path('frontend/build/static'), template_folder=get_root_path('frontend/build/'))

from lackey.models import db

db.create_all()

from lackey import api_views # api (uses db/models)
from lackey.api_views import calendar, notes, weather, finance, sports

api = Api(app)
api.add_resource(calendar.CALENDAR, '/Calendar/<arg>')
api.add_resource(notes.NOTES, '/Notes/<arg>')
api.add_resource(weather.WEATHER, '/Weather/<arg>')
api.add_resource(finance.FINANCE, '/Finance/<arg>')
api.add_resource(sports.SPORTS, '/Sports/<arg>')

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/', methods=['GET'])
def landing():
    return render_template('index.html')
