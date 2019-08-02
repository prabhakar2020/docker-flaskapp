#!/usr/bin/env python
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/isready")
def isready():
    return "Greetings engine is UP & Running"

@app.route('/')
def hello():
    # count = get_hit_count()
    return 'Hello World! Welcome to Flask application.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)