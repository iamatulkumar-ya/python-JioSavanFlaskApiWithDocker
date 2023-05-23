from service.jioSavanService import getSearchedSong
from  utility.util import createResponse,validateRequestJsonData,getFormattedResponseResult
import logging

def callGetSearchedSong(reqJsonData):
     # validate the input json data
        logging.warning("calling validateRequestJsonData to validate the input.")
        isValidInput, songName= validateRequestJsonData(reqJsonData)

        logging.warning("validateRequestJsonData:  isValidInput:" + str(isValidInput))
        logging.warning("validateRequestJsonData:  songName:" + str(songName))

        if(isValidInput):
            #print(songName)
            logging.warning("calling getSearchedSong to get the result.")
            response = getSearchedSong(songName)
            # now calling the service to get the result for request song
            logging.warning("getSearchedSong: Status Code: " + str(response.status_code))

            logging.warning("calling getFormattedResponseResult to format the.")
            responseResult = getFormattedResponseResult(response.json())

            logging.warning("returning response from callGetSearchedSong.")
            return createResponse(False, "OK",responseResult,response.status_code) 

        
        else:
            logging.error("callGetSearchedSong: Issue with the input json.")
            return createResponse(True,'Json Input is not in proper format. Use this format: {"songName":"song name which you want to search"}')



