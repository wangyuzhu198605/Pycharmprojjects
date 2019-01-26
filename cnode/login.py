import time
def login(driver):
    driver.find_element_by_xpath('//*[text()="登录"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("user1")
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys("123456")
    driver.find_element_by_xpath('//*[@value="登录"]').click()