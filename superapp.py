""" Flask API listening to events catchted in the Traktor API. 

It listens to the events send by app.py and communicates with
Abbleton depending on the information provided by Traktor.
"""
import logging
import subprocess
from pathlib import Path
from flask import Flask, request, jsonify
from src.ai_dj import AiDj


TIME_TH = 15
trackLength = None
title = None

app = Flask(__name__)
# CREATION OF THE AiDj OBJECT



data_dir = Path("./data")
aidj = AiDj(data_dir.joinpath("main_clean_tracklist.csv"),
            data_dir.joinpath("similarity_matrix", "paraphrase-multilingual-mpnet-base-v2_weighted_mean_100.csv"),
            num_prev_rel_tracks=5
            )



@app.route("/deckLoaded/<deck>", methods=["POST", "GET"])
def deckLoaded(deck):
    try:
        received_data = request.get_json()
        print("\n[SUPERAPP]: <------- JSON DATA -------> in deckLoaded\n")
        print(received_data)

        global trackLength
        global title
        elapsedTime = None

        bpm = None
        elapsedTime = None

        if received_data: 
            if 'bpm' in received_data and received_data["bpm"]:
                bpm = received_data["bpm"]

            if 'title' in received_data and received_data["title"]:
                title = received_data["title"]

            if 'trackLength' in received_data and str(received_data["trackLength"]).isnumeric():
                trackLength = received_data["trackLength"]

            if "elapsedTime" in received_data and received_data["elapsedTime"] != None: 
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
        received_data = request.get_json()
        print("\n[SUPERAPP]: <------- JSON DATA -------> in updateDeck\n")
        print(received_data)

        global trackLength
        global title

        elapsedTime = None


        if received_data: 

            if "elapsedTime" in received_data and received_data["elapsedTime"] != None: 
                elapsedTime = received_data["elapsedTime"]

            print(f"Track Length: {trackLength}. Elapsed Time: {elapsedTime}")
        
        if trackLength != None and elapsedTime != None:

            if (trackLength - elapsedTime) < TIME_TH:
                print("[SUPERAPP]: STARTING THE AI ...")
                aidj.add_track(track_name = title, dj = "human")
                next_track_name = aidj.select_and_add_next_track()
                proc = subprocess.Popen(["py", "playSong.py", next_track_name])
                stdout, stderr = proc.communicate()
                if stdout == "0" and stderr != "-1":
                    print("Subprocess executed successfuly")

        print(f"BPM: esto me da igual. TITLE: {title}. TRACK LENGTH: {trackLength}. ELAPSED TIME: {elapsedTime}")
        return jsonify({"msg": "ok"}), 200

    except Exception:
        print("[SERVER SUPERAPP]: Error in /updateDeck route.\n")
        logging.exception("The error log is: ")
        return jsonify({"error": "Internal server error"}), 500



if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True)