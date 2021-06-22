import json
import requests

with open('api.txt','r') as inp:
    api = inp.read(36) 
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

Headers={
	'Accept': 'application/json'
}
getRequestParam = {
	'CMC_PRO_API_KEY': api
}


getRequest = requests.get(url,params=getRequestParam,headers=Headers)
recievedDataInJson = getRequest.json()


with open('cryptodata.json','w') as out:
	json.dump(recievedDataInJson, out, indent= 4, sort_keys= True)

