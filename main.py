from clarifai import rest
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='f057c497d264409f8c50bcfa79666b94')

def getTags(imgurl)
	# get the general model
	model = app.models.get("bd367be194cf45149e75f01d59f77ba7")
	# predict with the model
	return model.predict_by_url(url=imgurl)#'https://samples.clarifai.com/metro-north.jpg')

