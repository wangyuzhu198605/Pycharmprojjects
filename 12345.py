
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://mail.163.com/")
time.sleep(5)
el=driver.find_elements_by_xpath("//*[@frameborder='0']")[0]
print(el)
#driver.switch_to.frame("")
driver.switch_to.frame(el)
time.sleep(3)
driver.find_element_by_xpath('//*[@name="email"]').send_keys("123456")