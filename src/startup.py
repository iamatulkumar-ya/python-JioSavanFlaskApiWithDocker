from flask import Flask , request
from http import HTTPStatus

from utility.util import createResponse, getEndpointInstructions
from app.searchSongsHandler import callGetSearchedSong

import logging

app = Flask(__name__)


@app.route('/',methods=['GET'])
def welcomeToPortal():
    logging.warning("Welcome to the portal.")
    return createResponse(False,"Search Songs API is running.", getEndpointInstructions(),HTTPStatus.OK)


@app.route('/SearchSongs',methods=['GET'])
def SearchSongs(): 
    try: 
        logging.warning("Inside /SearchSongs")
        logging.warning("Calling callGetSearchedSong method to get the result.")
    # get callGetSearchedSong
        return  callGetSearchedSong(request.get_json())

       
    except:
        logging.error("Inside Exception of /SearchSongs.")
        return createResponse(True,"Internal Error Occurred. Please try after sometime.","",HTTPStatus.INTERNAL_SERVER_ERROR)

if __name__ == "__main__":

    # remove the debug=True while deploying into PROD
    app.run(port = 5000,debug=True)