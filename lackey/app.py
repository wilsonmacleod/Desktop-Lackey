# Flask app that handles application logic

from flask import Flask
from flask import render_template
from flask import request
from lackey import get_root_path

app = Flask(__name__, static_folder=get_root_path('static'), template_folder=get_root_path('templates'))

@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True, use_reloader=True)
