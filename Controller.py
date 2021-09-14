""" This script contains the Controller class. This class controls the
objects which are in charge of handling the information broadcasted by Tracktor
and playing the clips in Abbleton. 

It also is responsible of reading the .txt files containing the info
of the next song to be played. 
"""

import pathlib
import logging

from Abbleton import Abbleton
from Tracktor import Tracktor

class Controller:
    """ 
    Controller class controls the objects which are in charge of handling the 
    information broadcasted by Tracktor and playing the clips in Abbleton. 

    It also is responsible of reading the .txt files containing the info
    of the next song to be played.  

    Attributes
    ----------
    filesPath : str
        path to .txt files

    abbleton : Abbleton
        Abbleton controller object. It finds and plays the recommended song.

    tracktor : Tracktor
        Tracktor broadcast listener object. It handles the data provided
        by the Tracktor broadcasting software.
    
    Methods
    -------
    getNextSongTitle(str : filePath)
        reads from the specified file the next song's title

    run()
        executes the main program
    """
    def __init__(self, filesPath):
        self.filesPath = pathlib.Path(filesPath)
        self.abbleton = Abbleton()
        self.tracktor = Tracktor()


    def getNextSongTitle(self, filename):
        """ Reads the corresponding file and return the title of the next song.

        Attributes
        ----------
        filename : str
            name of the file to be readen. It would be appended to the BASE_PATH

        Returns
        -------
        songName : str
            Title of the next song to be played
        """
        try:
            with self.filesPath.joinpath(filename).open(mode="r", encoding="utf-8") as file:
                songName =  file.readline()
                return songName
        except OSError:
            logging.error("\n[CONTROLLER]: Error while opening the song .txt file. The error log is: ")

    
    def run(self):
        pass
