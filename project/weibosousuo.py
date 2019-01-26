from selenium import webdriver
import time
import re
import xlwt
import xlrd
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome()
driver.get("https://s.weibo.com/")
driver.find_element_by_css_selector('[node-type="text"]').send_keys("web自动化")
driver.find_element_by_css_selector('.s-btn-b').click()
driver.find_element_by_css_selector('a[node-type="advsearch"]').click()
driver.find_element_by_css_selector('[id="radio03"]').click()
driver.find_element_by_css_selector('.s-btn-a').click()
WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector('.ctips').is_displayed())
num_biaoti=driver.find_elements_by_xpath('//*[@class="name"]')
print(len(num_biaoti))
L_fabuzhe=["发布者"]
L_biaoti=["标题"]
L_time=["时间"]
L_from=["来源"]
num_dianzan=["点赞"]
num_shoucang=["收藏"]
num_zhuanfa=["转发"]
num_pinglun=["评论"]
for i in range(len(num_biaoti)):
    text_发布者=num_biaoti[i].text
    L_fabuzhe.append(text_发布者)

    text_content=driver.find_elements_by_xpath('//*[@node-type="feed_list_content"]')[i].text
    L_biaoti.append(text_content)
    text_time=driver.find_elements_by_xpath('//*[@class="from"]//*[@target="_blank"]')[i].text
    L_time.append(text_time)
    text_from=driver.find_elements_by_xpath('//*[@class="from"]//*[@rel="nofollow"]')[i].text
    L_from.append(text_from)
    text_dianzan=driver.find_elements_by_xpath('//a[@title="赞"]/em')[i].text
    if text_dianzan=="":
        num_dianzan.append(0)
    else:
        num_dianzan.append(int(text_dianzan))





    if len(driver.find_elements_by_xpath('//*[@class="card-act"][i]//li[1]/*[text()="取消收藏"]'))==1:
        num_shoucang.append(1)
    else:num_shoucang.append(0)

    #print(num_shoucang)
    text_zhuanfa=driver.find_elements_by_xpath('//*[@class="card-act"][1]//li[2]/a')[i].text
    #print(text_zhuanfa)

    if len(re.findall("\d+",text_zhuanfa))>=1:
        s = re.findall("\d+",text_zhuanfa)[0]
        num_zhuanfa.append(int(s))
    else:  num_zhuanfa.append(0)
    text_pinglun=driver.find_elements_by_xpath('//*[@class="card-act"][1]//li[3]/a')[i].text



    if len(re.findall("\d+",text_pinglun))>=1:
        s = re.findall("\d+",text_pinglun)[0]
        num_pinglun.append(int(s))
    else:  num_pinglun.append(0)
    # print(s)# a=text_zhuanfa[2:]

    # print(a)
    # if (a.isdigit()):
    #     num_zhuanfa.append(int(a))
    # else:
    #     num_zhuanfa.append(0)
print(L_fabuzhe)
print(L_biaoti)
print(L_time)
print(L_from)
print(num_shoucang)
print(num_zhuanfa)
print(num_dianzan)
print(num_pinglun)

excel=xlwt.Workbook()
sheet=excel.add_sheet("test")




for i in range(len(L_biaoti)):
     sheet.write(i,0,L_biaoti[i])
     sheet.write(i,1,L_fabuzhe[i])
     sheet.write(i,2,L_time[i])
     sheet.write(i,3,L_from[i])

     sheet.write(i,4,num_shoucang[i])
     sheet.write(i,5,num_zhuanfa[i])
     sheet.write(i,6,num_pinglun[i])
     sheet.write(i,7,num_dianzan[i])
excel.save("16.22.xlsx")
driver.close()