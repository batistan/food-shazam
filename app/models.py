from clarifai import *
from clarifai.rest import ClarifaiApp, Image
from clarifai.rest import client
import json
appc = ClarifaiApp(api_key='eabb3a40609c4b8096054351b85d68f5')

def getTags(filename):

    # get the general model
        model = appc.models.get("bd367be194cf45149e75f01d59f77ba7")
        # predict with the model
        image = Image(file_obj=open(filename, 'rb'))
        food=model.predict([image])

        tags=[]
        for each in food['outputs'][0]['data']['concepts']:
            if each['value']>0.95:
                tags.append(each['name'])
        if len(tags)==0:
            print("No Tags")
            sys.exit(-1)
        print(tags)
        return tags[0:2]

def getRestaurants(tags, location):

    url = 'https://api.foursquare.com/v2/venues/search'

    params = dict(
            client_id='S2IQP1FPW11CICWUQYKB2OM0ITATD3HWLG3PN3OHVJW5TZCH',
            client_secret='GINNM23LCOMLMMBS5YIVGO242FYLWJLA3TGGN4X5OWH3C3V2',
            near=location,
            query=tags,
            limit=50
            )

    resp = requests.get(url=url, params=params)
    print(resp)
    return resp

