import time
from multiprocessing import Process


def worker():
    while True:
        print("First process executing...")
        time.sleep(2)


def secondworker():
    while True:
        print("Second process executing")
        time.sleep(3)


if __name__ == "__main__":
    p = Process(target=worker)
    p2 = Process(target=secondworker)
    p.start()
    p2.start()
    print("Processes have started")
    print("Process is working")