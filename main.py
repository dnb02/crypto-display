import json
import requests

api = '858c01a1-651c-4343-8e01-89c39143b544' 
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

apiInfo = {
	'CMC_PRO_API_KEY': api
}


r = requests.get(url, params = apiInfo)
print(r)