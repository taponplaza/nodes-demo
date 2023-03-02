import os
from flask import Flask, render_template, make_response, json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/get-graph", methods=["POST"])
def get_graph():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "resources", "data_30.json")
    data = json.load(open(json_url))

    response = make_response(data, 200)
    return response