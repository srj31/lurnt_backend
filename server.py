from flask import request, jsonify, Flask
import requests
import json
import random

from helper import get_page, store_info_in_csv

app = Flask(__name__)

API_KEY = "AIzaSyC5FUhXQK-HirDBHAPE5kiG6g20FRLF4Z4"
SEARCH_ENGINE_ID = 'edfc0e73a51df8fbd'
GOOGLE_API = ' https://www.googleapis.com/customsearch/v1?key=' + \
    API_KEY+'&cx='+SEARCH_ENGINE_ID

# Members API Route


@app.route("/all_pages")
def all_pages():
    if 'choice' in request.args:
        choice = str(request.args['choice'])

    if 'lvl' in request.args:
        lvl = str(request.args['lvl'])

    url = GOOGLE_API+'&q='+lvl+"%20"+choice
    response = requests.get(url).json()
    items = response['items']

    # store_info_in_csv(items)

    result = {"result": items}
    return jsonify(result)


@app.route("/lurn", methods=["GET"])
def lurn():

    if 'choice' in request.args:
        choice = str(request.args['choice'])

    if 'lvl' in request.args:
        lvl = str(request.args['lvl'])

    start_idx = str(random.randint(1, 50))

    url = GOOGLE_API+'&q='+lvl+"%20"+choice+"&start="+start_idx
    response = requests.get(url).json()
    items = response['items']

    random_page = get_page(items)

    result = {"result": random_page}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
