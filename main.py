import requests
import json
import tkinter 

class application:

	def getValue(self):
		
		with open('mapping.json') as inp:
			trackableCrypto=json.load(inp)
		strackableCryptoNames = list(trackableCrypto.keys())
		

		with open('api.txt','r') as inp:
			api = inp.read(36) 
		url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
		Headers={
			'Accept': 'application/json'
		}
		getRequestParam = {
			'CMC_PRO_API_KEY': api,
			'id':trackableCrypto[self.clicked.get()]
			#'id':'1'
		}
		getRequest = requests.get(url,params=getRequestParam,headers=Headers)
		recievedDataInJson = getRequest.json()
		#requestedValue = recievedDataInJson["data"]["1"]["quote"]["USD"]["percent_change_1h"]
		requestedValue = recievedDataInJson["data"][trackableCrypto[self.clicked.get()]]["quote"]["USD"]["percent_change_1h"]
		self.changeDisplayValue.set(str(requestedValue))
		
	def gui(self):
		with open('mapping.json') as inp:
			trackableCrypto=json.load(inp)
		trackableCryptoNames = list(trackableCrypto.keys())
		
		mainWindow = tkinter.Tk()
		
		self.changeDisplayValue = tkinter.StringVar(mainWindow)
		self.changeDisplayValue.set('0')
		
		self.clicked= tkinter.StringVar()
		self.clicked.set(trackableCryptoNames[0])
		

		dropDownBox = tkinter.OptionMenu(mainWindow,self.clicked,*trackableCryptoNames).pack()
		
		button = tkinter.Button(mainWindow, text ="Get Value", command = self.getValue ).pack()
		display = tkinter.Label(mainWindow,textvariable = self.changeDisplayValue ).pack()
		mainWindow.mainloop()

app = application()
app.gui()


