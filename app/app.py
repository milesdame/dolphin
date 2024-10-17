from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/finFacts")
def facts():
    with open('facts.json') as f:
        fin = json.load(f)
    return jsonify(fin)

@app.route("/anatomy")
def anatomy():
    with open('anatomy.json') as f:
        dolphin = json.load(f)