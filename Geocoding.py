###########################
######## maps API ########
###########################

import urllib.request, urllib.parse, urllib.error
import json
import ssl
from geopy.distance import geodesic

servicesurl = "https://py4e-data.dr-chuck.net/json?"
api_key = 42
# ----------------------------------------
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# ----------------------------------------
def ctl(city):
    address = city
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = servicesurl + urllib.parse.urlencode(parms)
    url_handler = urllib.request.urlopen(url, context=ctx)
    data = url_handler.read().decode()
    try:
        js = json.loads(data)
        # print(js,"\n\n")

    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        return False
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    # return dict[('lat',lat),('lng',lng)]
    return lat, lng


def clc_d(x, y):
    if (x == False or y == False):
        return None
    return geodesic(x, y).km

