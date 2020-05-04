from flask import Flask, jsonify
from flask import render_template
from flask import request
from lackey import get_root_path
import json

# actions folder supplies our API calls and local data
from lackey.actions import weather

app = Flask(__name__, static_folder=get_root_path('frontend/build/static'), template_folder=get_root_path('frontend/build'))

DATA = ["Data One", "Data Two"]

@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/', methods=['GET'])
def landing():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def data():
    """ An example endpoint """
    data = {
        'this': 'should',
        'be': 'a fat',
        'json': 'obj',
        'hopefully': 'one day'
    }
    if request.method == 'GET':
        return jsonify(status=200, text=data)



if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)
