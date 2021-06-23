import requests
import json
import tkinter 

requestedValue = 0

def config():
	changeDisplayValue.set(str(requestedValue))

def getValue():
	global requestedValue
	with open('api.txt','r') as inp:
		api = inp.read(36) 

	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

	Headers={
		'Accept': 'application/json'
	}
	getRequestParam = {
		'CMC_PRO_API_KEY': api,
		'id':'1'
	}


	getRequest = requests.get(url,params=getRequestParam,headers=Headers)
	recievedDataInJson = getRequest.json()
	requestedValue = recievedDataInJson["data"]["1"]["quote"]["USD"]["percent_change_1h"]
	config()
#   This part of code saved the received data to a json file 

#	with open('cryptodata.json','w') as out:
#		json.dump(recievedDataInJson, out, indent= 4, sort_keys= True)

	

mainWindow = tkinter.Tk()
changeDisplayValue = tkinter.StringVar(mainWindow)
changeDisplayValue.set('0')
button = tkinter.Button(mainWindow, text ="Get Value", command = getValue ).pack()
display = tkinter.Label(mainWindow,textvariable = changeDisplayValue ).pack()
mainWindow.mainloop()