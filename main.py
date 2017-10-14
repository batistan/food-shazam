from clarifai import rest
from clarifai.rest import ClarifaiApp
from flask import flask

app = ClarifaiApp(api_key='f057c497d264409f8c50bcfa79666b94')
###
# get the general model
model = app.models.get("general-v1.3")

# predict with the model
model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
####
# before search, first need to upload a few images
app.inputs.create_image_from_url("https://samples.clarifai.com/puppy.jpeg")

# search by public concept
app.inputs.search_by_predicted_concepts(concept='dog')
###
# import a few labelled images
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog2.jpeg", concepts=["cute dog"], not_concepts=["cute cat"])

app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat1.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])
app.inputs.create_image_from_url(url="https://samples.clarifai.com/cat2.jpeg", concepts=["cute cat"], not_concepts=["cute dog"])

model = app.models.create(model_id="pets", concepts=["cute cat", "cute dog"])

model = model.train()

# predict with samples
print model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg")
print model.predict_by_url(url="https://samples.clarifai.com/cat3.jpeg")