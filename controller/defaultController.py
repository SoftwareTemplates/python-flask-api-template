from flask import jsonify


def DefaultController():
    return jsonify({
        "message": "Hello World"
    })
