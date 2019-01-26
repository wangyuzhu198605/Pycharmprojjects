import requests
import xlrd
def res_url(**param):

    r=requests.get('http://39.107.96.138:3000/api/v1/topics',params=param)
    print(r.json())
dict={"page":[1,2,3,4],"tab":["ask","share","job","good"],"limit":[1,2,3,4],"mdrender":["false","false","true","true"]}
print(len(dict))
for i in range(len(dict["page"])):

    page=dict["page"][i]
    print(page)
    tab=dict["tab"][i]
    limit=dict["limit"][i]
    mdrender=dict["mdrender"][i]


    res_url(url='http://39.107.96.138:3000/api/v1/topic/',page=page,tab=tab,limit=limit,mdrender=mdrender)