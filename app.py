from flask import Flask , request
from http import HTTPStatus

from  util import createResponse, getEndpointInstructions,validateRequestJsonData,getFormattedResponseResult
from jioSavanService import getSearchedSong

app = Flask(__name__)


@app.route('/',methods=['GET'])
def welcomeToPortal():
    return createResponse(False,"Search Songs API is running.", getEndpointInstructions(),HTTPStatus.OK)


@app.route('/SearchSongs',methods=['GET'])
def SearchSongs():
    try: 
    # get request json data
        reqJsonData = request.get_json()

        # validate the input json data
        isValidInput, songName= validateRequestJsonData(reqJsonData)
        if(isValidInput):
            print(songName)
            response = getSearchedSong(songName)
            # now calling the service to get the result for request song
            responseResult = getFormattedResponseResult(response.json())
            return createResponse(False, "OK",responseResult,response.status_code) 

        
        else:
            return createResponse(True,'Json Input is not in proper format. Use this format: {"songName":"song name which you want to search"}')

    except Exception:
        return createResponse(True,"Internal Error Occurred. Please try after sometime.","",HTTPStatus.INTERNAL_SERVER_ERROR)

if __name__ == "__main__":

    # remove the debug=True while deploying into PROD
    app.run(port = 5000,debug=True)