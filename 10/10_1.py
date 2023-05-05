import urllib
import json


def getGeoCode( addr) :
    q= urllib.parse.quote(addr)
    data = urllib.request.urlopen(" ") #key 필요
    result = json.loads(data.read())
    if (result['response']['status'] =='OK') :
        x=float(result['response']['result']['point']['x'])
        y=float(result['response']['result']['point']['y'])
    else :
        x,y=0,0
    return x, y


print (  getGeoCode("")) #자신의 위치