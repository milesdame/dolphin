from flask import Flask, jsonify, json, render_template

app = Flask(__name__)

@app.route("/facts")
def facts():
    with open('facts.json') as f:
        fin = json.load(f)
    return jsonify(fin)

@app.route("/anatomyData")
def anatomy():
    with open('anatomy.json') as f:
        dolphin_data = json.load(f)
    return jsonify(dolphin_data)

@app.route("/types/<type>")
def make_type_page(type):
    with open('types.json') as f:
        dolphin_type_data = json.load(f)

    info = dolphin_type_data[type]
    return render_template('types.html', info=info, type=type)