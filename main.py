from Controller import Controller
from constants import BASE_DIR
from multiprocessing import Process


if __name__ == "__main__":

    controller = Controller(BASE_DIR)
    controller.tracktor.start()

    #   Posar aquí el nom del txt amb el títol de la cançó
    songName = controller.getNextSongTitle("sample.txt")
    controller.abbleton.playSong(songName)

