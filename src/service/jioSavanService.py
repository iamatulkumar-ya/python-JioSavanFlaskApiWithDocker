import requests
import os
import logging


# format the song
def formatQuery(songName):
    return str(songName).strip().replace("\w+",'').replace(" ","+")

# get the searched songs
def getSearchedSong(songName):
    logging.warning("Inside getSearchedSong")

    logging.warning("Calling formatQuery")
    formattedSongName=formatQuery(songName)

    logging.warning("Calling URL to get the result with this song: "+ str(formattedSongName))
    response = requests.get(os.getenv("JIO_SAVAN_SEARCH_SONG_URL")+formattedSongName)
    return response 

