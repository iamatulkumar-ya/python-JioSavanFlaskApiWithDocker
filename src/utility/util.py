from http import HTTPStatus
import logging

def createResponse(_isError=False,_message="", _data="", _statusCode=HTTPStatus.BAD_REQUEST):
    if(_isError): 
        return {
            "data":_data,
            "message": "An error occured while processing the request. Please find the cause here: " + str(_message),           
            "statusCode":_statusCode}

    else:
     return {
            "data": _data,
            "message": str(_message),
            "statusCode":_statusCode}


def getEndpointInstructions():
   return 'To search a song use below endpoint: {{hostName}}/SearchSongs  Body: json type {"songName":"song name which you want to search"}'


"""
This method is ise to validatet the input json
"""
def validateRequestJsonData(reqJsonData):
    reqDataDict = {k.lower(): items for k, items in reqJsonData.items()}
    logging.warning("Inside validateRequestJsonData")

    if  'songname' in reqDataDict:
       logging.warning("Input Json is having required key.")
       return True , reqDataDict.get('songname')
    
    else:
       logging.warning("Input Json is not having required key.")
       return False , 'None'
    

"""
Method is used to get the json input of response result and format it into required fields

"""
def getFormattedResponseResult(resDataDict):

   logging.warning("Inside getFormattedResponseResult")

   searchedResultsList = []
   if(resDataDict["data"]["total"]==0):
         logging.warning("No data in result")
         #print(resDataDict["data"]["total"])

   else:
         logging.warning("Result is having data, formatting all.")
         searchResult = resDataDict["data"]["results"]

         for i in range(len(searchResult)):
               singleRecord = {}
               singleRecord.update({"Thumbnail": 'No Data' if len(searchResult[i]["image"]) == 0 else searchResult[i]["image"][len(searchResult[i]["image"])-1]["link"]})
               singleRecord.update({"SongName":'No Data' if len(str(searchResult[i]["name"])) == 0 else str(searchResult[i]["name"])})
               singleRecord.update({"AlbumName": 'No Data' if len(str(searchResult[i]["album"]["name"])) == 0 else str(searchResult[i]["album"]["name"])})
               singleRecord.update({"Year": 'No Data' if len(str(searchResult[i]["year"])) == 0 else str(searchResult[i]["year"])})
               singleRecord.update({"PrimaryArtists": 'No Data' if len(str(searchResult[i]["primaryArtists"])) == 0 else str(searchResult[i]["primaryArtists"])})
               singleRecord.update({"Language": 'No Data' if len(str(searchResult[i]["language"])) == 0 else str(searchResult[i]["language"])})
               singleRecord.update({"PlayOnline": 'No Data' if len(str(searchResult[i]["url"])) == 0 else str(searchResult[i]["url"])})
               singleRecord.update({"DownloadUrl": 'No Data' if len(searchResult[i]["downloadUrl"]) == 0 else searchResult[i]["downloadUrl"][len(searchResult[i]["downloadUrl"])-1]["link"]})
               
               searchedResultsList.append(singleRecord)

         
   logging.warning("Returning from getFormattedResponseResult.")      
   return searchedResultsList
            