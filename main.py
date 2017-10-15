from clarifai import *
from clarifai.rest import ClarifaiApp
from clarifai.rest import client
import json
app = ClarifaiApp(api_key='eabb3a40609c4b8096054351b85d68f5')
#img = ClImage(filename='/tmp/user/dog.jpg')

def getTags(imgurl)
	# get the general model
	model = app.models.get("bd367be194cf45149e75f01d59f77ba7")
	# predict with the model
	food=model.predict_by_url(url=imgurl)#"https://samples.clarifai.com/food.jpg")#imgurl
	tags=[]
	for each in food['outputs'][0]['data']['concepts']:
		if each['value']>0.95:
			tags.append(each['name'])
	if len(tags)==0:
		print("No Tags")
		sys.exit(-1)
	#for each in tags:
	#print(each)
	return tags


