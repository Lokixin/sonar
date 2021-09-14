from Controller import Controller
from constants import BASE_DIR


if __name__ == "__main__":

    controller = Controller(BASE_DIR)
    controller.getNextSongTitle("sample.txt")