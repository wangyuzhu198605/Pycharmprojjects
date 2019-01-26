from selenium import webdriver
import re
import requests
import time
driver=webdriver.Chrome()
driver.get("https://movie.douban.com/subject/3168101/reviews")
driver.find_element_by_xpath('//*[text()="登录"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="email"]').send_keys("970257785@qq.com")
driver.find_element_by_xpath('//*[@name="form_password"]').send_keys("wyz198605")
driver.find_element_by_xpath('//*[@value="登录"]').click()
for i in range(63):

    html=requests.get("https://movie.douban.com/subject/3168101/reviews")
    html=html.text
    pattern=re.compile(r'<div class="short-content">(.*?)</div>',re.S)
    result=pattern.findall(html)
    print((result))
#driver.find_element_by_xpath('//*[text()="后页>"]').click()

# a="'http://www.24234.com,https://www.svdg5h454.com'"
# # pattern=re.compile(r'https{0,1}://w+.*.com',re.S)
# # result=pattern.findall(a)
# # print(result)
