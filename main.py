import json
import requests
import pprint

api = '858c01a1-651c-4343-8e01-89c39143b544' 
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

Headers={
	'Accept': 'application/json'
}
getRequestParam = {
	'CMC_PRO_API_KEY': api
}


getRequest = requests.get(url,params=getRequestParam,headers=Headers)
recievedDataInJson = getRequest.json()
prettyRecievedDataInJson = pprint.pformat(recievedDataInJson)

with open('cryptodata.json','w') as out:
	out.write(prettyRecievedDataInJson)

#print(recievedDataInJson['data'])