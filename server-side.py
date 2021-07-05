import praw
import requests
import json
import os
import time

def jsondumper():
	clientSecret = os.environ.get('REDDIT_SECRET_KEY')
	password = os.environ.get('BOTT_PASSWORD')
	reddit = praw.Reddit(client_id='WvfB2YOqYcUlMg',client_secret=clientSecret,username='jsonbot',password=password,user_agent='prawtryv1')
	reddit.validate_on_submit=True
	with open('dump.json') as inp:
		dumpValue=json.load(inp)
	selftext = "{}".format(dumpValue)
	title = "-json-dump-"
	reddit.subreddit("jsondump").submit(title, selftext=json.dumps(dumpValue))


def getValue():
	api = os.environ.get('CRYPTO_API')
	Headers={
		'Accept': 'application/json'
	}
	parameters = {
		'CMC_PRO_API_KEY': api,
		'id' : '1,1839,4687,1831,2010,1975,4943,74,1027,2,6636,3890,5426,512,2416,825,3408,7083,3717,52'
	}
	list_id = [1,1839,4687,1831,2010,1975,4943,74,1027,2,6636,3890,5426,512,2416,825,3408,7083,3717,52]
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
	response = requests.get(url,params=parameters)
	recievedValue = response.json()
	with open('dump.json','r') as inp:
		dumpValue=json.load(inp)
	
	while(len(dumpValue['1'])>23):
		for i in list_id:
			dumpValue["{}".format(i)].pop(0)
	for i in list_id:
		dumpValue["{}".format(i)].append("{}".format(recievedValue['data'][str(i)]['quote']['USD']['price']))
	
	with open('dump.json','w') as out:
		json.dump(dumpValue,out,indent = 2)

if __name__ == "__main__":
	getValue()
	jsondumper()
	print('Done')
