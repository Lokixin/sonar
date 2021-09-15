""" This script contains the Tracktor class. It would read tracktor boradcasted messages.

This class is mainly a TCP Server listening to the tracktor broadcast. It would read
the song information provided by the Tracktor software ( hopefully :D ). 
"""

from traktor_nowplaying import Listener
from constants import BASE_DIR


class Tracktor():
    """
    The Traktor class is responsible of listening to the Traktor software
    broadcast. From that broadcast, it shall extract the song's title, duration
    and elapsed time. Also it must write it into a file, so the Ableton class 
    knwo which song has to play next.

    Attributes
    ----------
    listener : Listener
        Http server socket listening to Traktor broadcast data.

    Methods
    -------
    start() -> None
        Starts the server
    """
    
    def __init__(self):

        self.listener = Listener(
            port=8000, 
            quiet=False, 
            outfile='/files/sample.txt', 
            output_format='{{title}}'
        )

    
    def start(self):
        self.listener.start()