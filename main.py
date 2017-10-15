from clarifai import *
from clarifai.rest import ClarifaiApp
from clarifai.rest import client
import json
app = ClarifaiApp(api_key='f057c497d264409f8c50bcfa79666b94')
#img = ClImage(filename='/tmp/user/dog.jpg')

#def getTags(imgurl)
# get the general model
model = app.models.get("bd367be194cf45149e75f01d59f77ba7")
# predict with the model
food=model.predict_by_url(url="https://samples.clarifai.com/food.jpg")#imgurl
print(str(food))
parsed=json.loads(str(food).replace("'", '"'))
for each in parsed:
    print(each)

