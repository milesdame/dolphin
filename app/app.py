from flask import Flask, jsonify, 

app = Flask(__name__)
<<<<<<< Updated upstream
cors = CORS(app)

@app.route("/finFacts")
def facts():
    with open('facts.json') as f:
        fin = json.load(f)
    return jsonify(fin)
=======
>>>>>>> Stashed changes

@app.route("/anatomy")
def anatomy():
    with open('anatomy.json') as f:
        dolphin_data = json.load(f)
    return jsonify
# consulted AI for JS only