""" Flask API listening to events catchted in the Traktor API. 

It listens to the events send by app.py and communicates with
Abbleton depending on the information provided by Traktor.
"""
import logging
import os
import sys
from pathlib import Path
from flask import Flask, request, jsonify
from Abbleton import Abbleton
from src.ai_dj import AiDj


TIME_TH = 15

app = Flask(__name__)
# CREATION OF THE AiDj OBJECT

abbletonController = Abbleton()

data_dir = Path("./data")
aidj = AiDj(data_dir.joinpath("main_clean_tracklist.csv"),
            data_dir.joinpath("similarity_matrix", "paraphrase-multilingual-mpnet-base-v2_weighted_mean_100.csv"),
            num_prev_rel_tracks=5
            )


@app.route("/", methods=["POST", "GET"])
def home():
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

        print(f"BPM: {bpm}. TITLE: {title}. TRACK LENGTH: {trackLength}. ELAPSED TIME: {elapsedTime}")
        return jsonify({"msg": "ok"}), 200

    except Exception:
        print("[SERVER SUPERAPP]: Error in /deckLoaded route.\n")
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
        if (trackLength - elapsedTime) < TIME_TH:
            aidj.add_track(track_name = title, dj = "human")
            next_track_name = aidj.select_and_add_next_track()
            abbletonController.playSong(next_track_name)

        print(f"BPM: {bpm}. TITLE: {title}. TRACK LENGTH: {trackLength}. ELAPSED TIME: {elapsedTime}")
        return jsonify({"msg": "ok"}), 200

    except Exception:
        print("[SERVER SUPERAPP]: Error in /updateDeck route.\n")
        logging.exception("The error log is: ")
        return jsonify({"error": "Internal server error"}), 500



if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True)