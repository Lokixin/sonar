from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route("/")
def home():
    print(request.data)
    return jsonify({"msg": "ok"}), 200


@app.route("/updateChannel/<channel>")
def updateChannel(channel):
    print(request.data)
    return jsonify({"msg": "ok"}), 200


@app.route("/deckLoaded/<deck>")
def deckLoaded(deck):
    print(request.data)
    return jsonify({"msg": "ok"}), 200


@app.route("/updateDeck/<deck>")
def updateDeckdeck(deck):
    print(request.data)
    return jsonify({"msg": "ok"}), 200


@app.route("/updateMasterClock")
def updateMasterClock():
    print(request.data)
    return jsonify({"msg": "ok"}), 200


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)