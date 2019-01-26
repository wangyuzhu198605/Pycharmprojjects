import requests

r = requests.get('http://39.107.96.138:3000/api/v1/topics',params={"page":2,"tab":"ask"})
print(r.json())
import json
a = {'a':1,'b':2,'c':3}
b='{"a":1,"b":2,"c":3}'
print(json.loads(b))
#json.load()
print(json.dumps(a))
#json.dump()
def response_url(id,**param):
    url='http://39.107.96.138:3000/api/v1/topic/'
    if  param=={}:
        response_url=requests.get(url+id)
        return response_url.json()
    else :
        response_url=requests.get(url+id,params=param )
        return response_url.json()
list=["5c1e5c1b9a1b06054f50a728","5c1e5c1b9a1b06054f50a727","5c1e5c1b9a1b06054f50a726","5c1e5c1b9a1b06054f50a723","5c1e5c1b9a1b06054f50a721"]
for id in list:

#res=requests.get('http://39.107.96.138:3000/api/v1/topics/5c1e5c1b9a1b06054f50a728',params={"mdrender":"false","accesstoken":"3333a0fb-6dd8-439e-813b-2c3a5213a154"}


    #print(response_url(id=id,mdrender="false",accesstoken="3333a0fb-6dd8-439e-813b-2c3a5213a154"))
    print(response_url(id=id,param={"mdrender":"false","accesstoken":"3333a0fb-6dd8-439e-813b-2c3a5213a154"}))


