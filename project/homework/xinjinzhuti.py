import requests
import xlrd
filepath='/Users/wangyuzhu/PycharmProjects/project/homework/test.xlsx'
excel = xlrd.open_workbook(filepath,"rb")
#新建主题接口
sheet= excel.sheets()[1]
print(sheet.nrows)
def test_xinjianzhuti(url,**data):


    r=requests.post(url,data=data)
    return r.json()
def read_excel_from_file(filepath):
    return filepath
def runa_case():
    data=read_excel_from_file(filepath)
    print("data",data.json())
    for  i  in range(3,sheet.nrows):
        accesstoken=sheet.row_values(i)[0]
        print(accesstoken)
        title=sheet.row_values(i)[1]
        print(title)
        tab=sheet.row_values(i)[2]
        print(tab)
        content=sheet.row_values(i)[3]
        print(content)

        test_xinjianzhuti(url='http://39.107.96.138:3000/api/v1/topics',accesstoken=accesstoken,title=title,tab=tab,content=content)
runa_case()