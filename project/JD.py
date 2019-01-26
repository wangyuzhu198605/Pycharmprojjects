from selenium import webdriver
import xlwt
import time
driver = webdriver.Chrome()
driver.get("https://www.jd.com")
driver.find_element_by_xpath('//*[@type="text"]').clear()
driver.find_element_by_xpath('//*[@type="text"]').send_keys("手机")

driver.find_element_by_xpath('//*[contains(@class,"button")]').click()
time.sleep(5)
price = driver.find_elements_by_xpath('//*[@class="p-price"]//i')
print(price[0].text)
phone = driver.find_elements_by_xpath('//*[@class="p-name p-name-type-2"]//em')
a=driver.find_element_by_css_selector('.J_100002332162>em').text
print(type(a))
count=len(phone)
print(count)

exl=xlwt.Workbook()
sheet=exl.add_sheet("JD手机")
sheet.write(0,0,"手机")
sheet.write(0,1,"价格")
for i in range(count):
    sheet.write(i+1,0,phone[i].text)
    sheet.write(i+1,1,a+price[i].text)
exl.save("/Users/wangyuzhu/Downloads/test3.xlsx")