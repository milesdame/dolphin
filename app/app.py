from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
cors = CORS(app)

@app.route("/csc342groups")
def csc_342_groups():
    groups = {1: {'Content Specialist': ['Julia Hogg'],
        'Designer': ['Sage DeVore'],
        'Programmer(s)': ['Miles Dame', 'Hanna King']},
        2: {'Content Specialist': ['Brady Fleuette'],
        'Designer': ['David Lash'],
        'Programmer(s)': ['Kyler Bailey', 'Brodee Clontz']},
        3: {'Content Specialist': ['AJ Leary'],
        'Designer': ['Khalid Ismail'],
        'Programmer(s)': ['Matt Keller', 'Moultrie Dangerfield']},
        4: {'Content Specialist': ['Collin Riddle'],
        'Designer': ['Case Riddle'],
        'Programmer(s)': ['Ellie Johnson', 'Jack Roberts']},
        5: {'Content Specialist': ['Olivia Longsworth'],
        'Designer': ['Flynn Nisbet'],
        'Programmer(s)': ['Mengsrun Nit']},
        6: {'Content Specialist': ['Jack Patterson'],
        'Designer': ['Charlie Fink'],
        'Programmer(s)': ['Emirhan Gencer']}}
    return jsonify(groups)

@app.route("/anatomy")
def anatomy():
    with open('anatomy.json') as f:
        dolphin = json.load(f)