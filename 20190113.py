from selenium import webdriver
import time
# import base64
# import requests
#
# driver = webdriver.Chrome()
# driver.get('https://persons.shgjj.com/')
#
#
# image = driver.find_element_by_id('img1')
#
# image.screenshot('./01.png')
#
# f = open(r'./01.png', 'rb')
# # 参数image：图像base64编码
# print(f.read())
# img = base64.b64encode(f.read())
#
#
#
# url = "https://aip.baidubce.com/oauth/2.0/token"
#
# querystring = {"grant_type":"client_credentials","client_id":"1RQYVnqvNBIPoxFtzr68mWzz","client_secret":"NcQfFTMwmNyayuQiLsugfyiP05nPmnKT"}
#
# payload = ""
# headers = {
#     'cache-control': "no-cache",
#     'Postman-Token': "53654ba8-1fa5-419f-9cf5-d585dd302b5d"
#     }
#
# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
#
# # print(response.json())
#
# data = response.json()
# print (data['access_token'])
#
# access_token = data['access_token']
#
# url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
#
# querystring = {"access_token":access_token}
#
# payload = {"image": img}
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'cache-control': "no-cache"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#
# print(response.json())
#
# checkData = response.json()
#
# num = checkData['words_result'][0]['words']
#
# driver.find_element_by_id('imagecode1').send_keys(num)
#ifarme.
# driver=webdriver.Chrome()
# driver.get("https://shanghai.anjuke.com/?pi=PZ-baidu-pc-all-biaoti")
# driver.find_element_by_xpath("//*[text()='登录']").click()
# driver.switch_to.frame("iframeLoginIfm")
# driver.find_element_by_css_selector('#pwdTab').click()
#
# driver.find_element_by_css_selector('#pwdUserNameIpt').send_keys("123456")
# driver=webdriver.Chrome()
# driver.get("http://39.107.96.138:3000/")
# driver.find_element_by_xpath('//*[text()="登录"]').click()
# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="name"]').send_keys("user1")
# driver.find_element_by_xpath('//*[@id="pass"]').send_keys("123456")
# driver.find_element_by_xpath('//*[@value="登录"]').click()
# driver=webdriver.Chrome()
# driver.get("http://www.ctrip.com/?utm_source=baidu&utm_medium=cpc&utm_campaign=baidu81&campaign=CHNbaidu81&adid=index&gclid=&isctrip=T")
# start_time="2019-01-01"
#
# driver.execute_script('''document.querySelector('#HD_CheckIn').value="f'{start_name}'" ''')

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
mobileEmulatio = {"deviceName":'iPad'}
chrome_options.add_experimental_option('mobileEmulation',mobileEmulatio)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.baidu.com')