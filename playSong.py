from Abbleton import Abbleton
import sys



if __name__ == "__main__":
    try:
        print("[PLAYSONG]: Starting process...")    
        abbleton = Abbleton()
        abbleton.playSong(sys.argv[1])
        print("0")
    except Exception:
        sys.stderr.write("-1")