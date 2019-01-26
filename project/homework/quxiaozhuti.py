import requests
import xlrd
excel = xlrd.open_workbook(r'/Users/wangyuzhu/Downloads/test1.xlsx',"rb")
#新建主题接口
sheet = excel.sheets()[0]
print(sheet.nrows)

def response_url(url,**data):
    r=requests.post(url=url,data=data)
    return r.json()
#url=sheet.cell(0,1).value
for i in range(3,sheet.nrows):
    accesstoken = sheet.row_values(i)[0]
    print(accesstoken)
    topicid=sheet.row_values(i)[1]
    print(topicid)
    print(response_url(url="http://39.107.96.138:3000/api/v1/topic_collect/de_collect",accesstoken=accesstoken,topicid=topicid))