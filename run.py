from flask import Flask
from controller.defaultController import DefaultController

# Initialize the flask app
app = Flask(__name__)


@app.route("/")
def default():
    return DefaultController()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
