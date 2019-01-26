import requests
import xlrd
import xlwt
import json























import requests
import xlrd
excel = xlrd.open_workbook('/Users/wangyuzhu/PycharmProjects/untitled1/homework/test.xlsx')#打开sheet
sheet= excel.sheets()[0]
print(sheet.nrows)
# url = sheet.cell(1,0).value
# print(url)

def res_url(url,**parama):

    r = requests.get(url=url, params=parama)
    return r.json()
 #主题首页接口
for  i  in range(1,5) :
    page=int(sheet.row_values(i)[0])  #获取page
    print(page)    #打印page
    tab= (sheet.row_values(i)[1])  #获取tab
    print(tab)       #打印tab
    limit=int(sheet.row_values(i)[2])
    print(limit)
    mdrender = str(sheet.row_values(i)[3])
    print(mdrender)
    print(res_url(url='http://39.107.96.138:3000/api/v1/topics',page=page,tab=tab,limit=limit,mdrender=mdrender))  #打印参数的返回结果
    assert   res_url(url='http://39.107.96.138:3000/api/v1/topics' ,page=page,tab=tab,limit=limit,mdrender=mdrender)["success"]==True   #断言






