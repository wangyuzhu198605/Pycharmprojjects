
import json
import traceback
import requests


url = "http://cpright.xinhua-news.cn/api/match/image/getjson"

querystring = {
    "category": "image",
    "offset": "0",
    "limit": "30",
    "sourceId": "0",
    "metaTitle": "",
    "metaId": "0",
    "classify": "unclassify",
    "startTime": "",
    "endTime": "",
    "createStart": "",
    "createEnd": "",
    "sourceType": "",
    "isTracking": "true",
    "metaGroup": "",
    "companyId": "0",
    "lastDays": "1",
    "author": ""
}

headers = {
    'cache-control': "no-cache",
    'postman-token': "e97a99b0-424b-b2a5-7602-22cd50223c15"
    }


try:
    #Post接口调用
    response = requests.request("POST", url, headers=headers, params=querystring)
    print(response.text)
    #对http返回值进行判断，对于200做基本校验
    if response.status_code == 200:
        results = json.loads(response.text)
        if results['total'] == 135:
            print("Success")
        else:
            print("Fail")
            print(results['total'])
    else:
        #对于http返回非200的code，输出相应的code
        raise Exception("http error info:%s" %response.status_code)
except:
    traceback.print_exc()

