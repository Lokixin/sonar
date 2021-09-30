""" Tracktor event listener API. 

It listens to the Traktor events generated by the 
QML plugin.
Also, it resends data from Traktor to superapp.py
"""

import requests
import logging
from flask import Flask, request, jsonify


app = Flask(__name__)
EXTERNAL_API = "http://localhost:5555"


@app.route("/", methods=["POST", "GET"])
def home():
    print(request.data)
    requests.post("http://localhost:5555")
    return jsonify({"msg": "ok"}), 200


@app.route("/updateChannel/<channel>", methods=["POST", "GET"])
def updateChannel(channel):
    print(request.data)
    return jsonify({"msg": "ok"}), 200


@app.route("/deckLoaded/<deck>", methods=["POST", "GET"])
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

        song_data = {
            "bpm": bpm,
            "title": title,
            "trackLength": trackLength,
            "elapsedTime": elapsedTime
        }
    
        requests.post(
            f"{EXTERNAL_API}/deckLoaded/{deck}",
            json=song_data
        )

        return jsonify({"msg": "ok"}), 200

    except Exception:
        print("[SERVER APP]: Error in /deckLoaded route.\n")
        logging.exception("The error log is: ")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/updateDeck/<deck>", methods=["POST", "GET"])
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

        song_data = {
            "bpm": bpm,
            "title": title,
            "trackLength": trackLength,
            "elapsedTime": elapsedTime
        }
    
        requests.post(
            f"{EXTERNAL_API}/updateDeck/{deck}",
            json=song_data
        )

        return jsonify({"msg": "ok"}), 200

    except Exception:
        print("[SERVER APP]: Error in /updateDeck route.\n")
        logging.exception("The error log is: ")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/updateMasterClock", methods=["POST", "GET"])
def updateMasterClock():
    print(request.data)
    return jsonify({"msg": "ok"}), 200


if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)