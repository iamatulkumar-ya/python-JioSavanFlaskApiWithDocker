import requests
import os
# format the song
def formatQuery(songName):
    return str(songName).strip().replace("\w+",'').replace(" ","+")

# get the searched songs
def getSearchedSong(songName):
    formattedSongName=formatQuery(songName)

    response = requests.get(os.getenv("JIO_SAVAN_SEARCH_SONG_URL")+formattedSongName)
    return response 

