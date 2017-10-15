from clarifai import *
from clarifai.rest import ClarifaiApp, Image
from clarifai.rest import client
import json,requests
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
        print("Tags: ",tags[0:2])
        return tags[0:2]

def getRestaurants(tags, location):

    url = 'https://api.foursquare.com/v2/venues/search'

    q = ''

    for t in tags:
        q += t
        q += '+'

    params = dict(
            client_id='S2IQP1FPW11CICWUQYKB2OM0ITATD3HWLG3PN3OHVJW5TZCH',
            client_secret='GINNM23LCOMLMMBS5YIVGO242FYLWJLA3TGGN4X5OWH3C3V2',
            near=location,
            v='20171015',
            query=q,
            limit=10
            )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    #print(data)
    return data


tags = getTags('food.jpg')
resp = getRestaurants(tags, 'New York, NY')
r = resp['response']['venues']

print('Venues serving food like this near New York, NY:')
for v in r:
    print(v['name'])
    print(v['location']['formattedAddress'])

#for each in resp['venue']:
#    print(each)
#   # print(venue['name'])
#   # print(venue['location']['formattedAddress'])
#   # print(venue['contact']['formattedPhone'])


