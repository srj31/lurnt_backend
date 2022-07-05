from distutils.log import debug
from flask import Flask

app = Flask(__name__)

# Members API Route


@app.route("/choices")
def choices():
    return {"choices": ["choice1", "choice2", "choice3"]}


if __name__ == "__main__":
    app.run(debug=True)
