""" This script contains the Abbleton class. 

The Abbleton class is responsible of reading the tracks
and the clips of the Abbleton project being used and playing
the corresponding song of the playlist.
"""

from live import Set
from constants import TEMPO, TRACK_NAME


class Abbleton(Set):
    """
    The Abbleton class is responsible of reading the tracks
    and the clips of the Abbleton project being used and playing
    the corresponding song of the playlist.

    Attributes
    ----------
    #TODO

    Methods
    -------
    #TODO
    """
    
    def __init__(self):
        super().__init__()
        self.scan(scan_clip_names = True, scan_devices = True)
        self.tempo = TEMPO
        self.currentTrack = self.getTrack(TRACK_NAME)


    def getTrack(self, trackname):
        """ Gets the track named as TRACK_NAME

        If no track is found the program would exit
        Attributes
        ----------
        trackname : str
            Name of the track where the playlist is stored

        Returns
        -------
        track : Track
            A track named trackname
        """
        for track in self.tracks:
            if track.name == TRACK_NAME:
                return track
        else:
            print(f"[ABBLETON]: No track {TRACK_NAME} found. Exiting the program ...")
            exit()
            
            
    def playSong(self, songName):
        """ Plays the song which title's matches the songName

        Attributes
        ----------
        songName : str
            Name of the song to be played
        """
        for clip in self.currentTrack:
            if clip is not None:
                if songName in clip.name:
                    clip.play()
                    print(f"[ABBLETON]: Clip being played: {songName}")
                    break
        else:
            #TODO Deal with no clip found scenario. Now it only prints an error message.
            print(f"[ABBLETON]: Clip {songName} not found. We're screwed.")
                

        
