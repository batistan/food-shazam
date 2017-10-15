from clarifai import *
from clarifai.rest import ClarifaiApp, Image
from clarifai.rest import client
appc = ClarifaiApp(api_key='eabb3a40609c4b8096054351b85d68f5')
#img = ClImage(filename='/tmp/user/dog.jpg')

def getTags(ifile):

    # get the general model
    model = appc.models.get("bd367be194cf45149e75f01d59f77ba7")
    # predict with the model
    image = Image(file_obj=ifile)
    food=model.predict([image])

    #food=model.predict_by_url(url=imgurl)#"https://samples.clarifai.com/food.jpg")#imgurl
    tags=[]
    for each in food['outputs'][0]['data']['concepts']:
        if each['value']>0.95:
            tags.append(each['name'])
    if len(tags)==0:
        return 0

    return tags[0:2]

def getRestaurants(tags, location):

    query = ""
    for tag in tags:
        query.append(tag)
        query.append(' ')
    
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id = 'S2IQP1FPW11CICWUQYKB2OM0ITATD3HWLG3PN3OHVJW5TZCH',
        client_secret = 'GINNM23LCOMLMMBS5YIVGO242FYLWJLA3TGGN4X5OWH3C3V2',
        near=location,
        query=query,
        limit=50
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    print(data)
    return data
