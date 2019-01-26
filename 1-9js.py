from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://news.baidu.com/')
driver.execute_script("document.querySelector(\"[id='city_name']>a\").scrollIntoView()")
# aa='python'
# bb='hello'
# print(f"{'python'} ,{'tab'}{'.com'}")
# # print('{}{}'.format('python','heelo'))