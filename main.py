from Controller import Controller

from constants import BASE_DIR


if __name__ == "__main__":

    controller = Controller(BASE_DIR)
    #   Posar aquí el nom del txt amb el títol de la cançó
    songName = controller.getNextSongTitle("sample.txt")
    controller.abbleton.playSong(songName)
