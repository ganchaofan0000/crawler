import json
from urllib.request import urlopen
import requests

def getCountry(ipAddress):
    response = urlopen('http://ip-api.com/json/'+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country")


#print(getCountry('121.97.110.145'))
