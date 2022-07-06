from flask import request, jsonify, Flask
import requests

app = Flask(__name__)

API_KEY = "AIzaSyC5FUhXQK-HirDBHAPE5kiG6g20FRLF4Z4"
SEARCH_ENGINE_ID = 'edfc0e73a51df8fbd'
GOOGLE_API = ' https://www.googleapis.com/customsearch/v1?key=' + \
    API_KEY+'&cx='+SEARCH_ENGINE_ID

# Members API Route


@app.route("/choices")
def choices():
    return {"choices": ["choice1", "choice2", "choice3"]}


@app.route("/pages", methods=["GET"])
def pages():

    if 'choice' in request.args:
        choice = str(request.args['choice'])

    if 'lvl' in request.args:
        lvl = str(request.args['lvl'])

    results = []

    url = GOOGLE_API+'&q='+lvl+"%20"+choice
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)
