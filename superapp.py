""" Flask API listening to events catchted in the Traktor API. 

It listens to the events send by app.py and communicates with
Abbleton depending on the information provided by Traktor.
"""
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    print(request.data)
    return jsonify({"msg": "ok"}), 200


@app.route("/deckLoaded/<deck>", metods=["POST", "GET"])
def deckLoaded(deck):
    try:
        print(request.data)

        received_data = request.get_json()

        bpm = None
        title = None
        trackLength = None
        elapsedTime = None

        if received_data: 
            if 'bpm' in received_data:
                bpm = received_data["bpm"]
            if 'title' in received_data:
                title = received_data["title"]
            if 'trackLength' in received_data:
                trackLength = received_data["trackLength"]
            if "elapsedTime" in received_data: 
                elapsedTime = received_data["elapsedTime"]

        print(f"BPM: {bpm}. TITLE: {title}. TRACK LENGTH: {trackLength}. ELAPSED TIME: {elapsedTime}")
        return jsonify({"msg": "ok"}), 200

    except Exception:
        print("[SERVER SUPERAPP]: Error in /deckLoaded route.\n")
        logging.exception("The error log is: ")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/updateDeck/<deck>", metods=["POST", "GET"])
def updateDeck(deck):
    try:
        print(request.data)

        received_data = request.get_json()

        bpm = None
        title = None
        trackLength = None
        elapsedTime = None

        if received_data: 
            if 'bpm' in received_data:
                bpm = received_data["bpm"]
            if 'title' in received_data:
                title = received_data["title"]
            if 'trackLength' in received_data:
                trackLength = received_data["trackLength"]
            if "elapsedTime" in received_data: 
                elapsedTime = received_data["elapsedTime"]

        print(f"BPM: {bpm}. TITLE: {title}. TRACK LENGTH: {trackLength}. ELAPSED TIME: {elapsedTime}")
        return jsonify({"msg": "ok"}), 200

    except Exception:
        print("[SERVER SUPERAPP]: Error in /updateDeck route.\n")
        logging.exception("The error log is: ")
        return jsonify({"error": "Internal server error"}), 500



if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True)