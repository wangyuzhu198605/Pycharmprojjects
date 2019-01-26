import xlrd
import requests
excel=xlrd.open_workbook("../zhutixiangqing.xlsx")
sheet=excel.sheets()[0]
#print(sheet.nrows)
url=sheet.row_values(1)[0]
# print(type(url))
# id=sheet.row_values(2)[1]
# a=sheet.row_values(2)[0]
# print("a:",a)
# print(id)
parama=(sheet.row_values(1)[3])
# num_id=sheet.col_values(1)
# print(len(num_id))
num_parama=sheet.col_values(3)
#print(num_parama)

# print(url)


num_id=sheet.col_values(1)
print(num_id)
#前四条测试用例

for i in range(1,7):
    num_id=sheet.col_values(1)[i]
    print(num_id)
    parama=sheet.col_values(3)[i]
    if isinstance(num_id,float):
        url = url + str(int(num_id))
    else:
        url = url + (num_id)
    r=requests.get(url=url,params=parama)

    print(i,r)
    if r.status_code != 404:
        print(r.json())
    print(url)
    url = sheet.row_values(1)[0]
    if i in range(1,5) :
        assert (r.json()['success'])==True
    elif i ==5  :
        assert r.status_code==404
    else: assert (r.json()['success'])==False
