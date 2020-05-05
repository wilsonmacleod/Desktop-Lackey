from flask import Flask
from flask import render_template
from flask import request
from flask_restful import Api

import json

from lackey import get_root_path, api_views
# actions folder supplies our API calls and local data

app = Flask(__name__, static_folder=get_root_path('frontend/build/static'), template_folder=get_root_path('frontend/build'))
"""
add API VIEWS
"""
api = Api(app)
api.add_resource(api_views.API_ROUTER, '/api/<view>')

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/', methods=['GET'])s
def landing():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)
