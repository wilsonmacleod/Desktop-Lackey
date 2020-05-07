import json
from flask import Flask, render_template
from flask_restful import Api

from lackey import get_root_path
# app
app = Flask(__name__, static_folder=get_root_path('frontend/build/static'), template_folder=get_root_path('frontend/build'))

#from lackey.models import db, WeatherConfig # db/models
from lackey import api_views # api (uses db/models)

api = Api(app)
api.add_resource(api_views.API_ROUTER, '/api/<view>')


@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/', methods=['GET'])
def landing():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)
