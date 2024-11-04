from flask import Flask, jsonify, json, render_template

app = Flask(__name__)

@app.route("/finFacts")
def facts():
    with open('facts.json') as f:
        fin = json.load(f)
    return jsonify(fin)

@app.route("/anatomy")
def anatomy():
    with open('anatomy.json') as f:
        dolphin_data = json.load(f)
    return jsonify(dolphin_data)

@app.route("/types/<type>")
def make_type_page(type):
    with open('types.json') as f:
        dolphin_type_data = json.load(f)

    info = dolphin_type_data[type]
    return render_template('types.html', info)
#                           title = info["common_name"],
#                           heading = info["common_name"],
#                           common_name = info["common_name"],
#                           sci_name = info["sci_name"],
#                           length = info["length"],
#                           weight = info["weight"],
#                           life_span = info["life_span"],
#                           desc = info["desc"]
#                           )