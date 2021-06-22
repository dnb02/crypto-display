import json
import requests

with open('api.txt','r') as inp:
    api = inp.read(36) 

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=1'

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

print(recievedDataInJson["data"]["1"]["quote"]["USD"]["percent_change_1h"])

