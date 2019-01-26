from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  #浏览器的实例
driver.get("http://39.107.96.138:3000/")  #打开网页
driver.find_element_by_xpath('//li/*[@href="/signin"]').click()  #点击登录按钮
driver.find_element_by_css_selector('#name').send_keys("user1")
driver.find_element_by_css_selector('#pass').send_keys("123456")
driver.find_element_by_css_selector('.span-primary').click()
driver.find_element_by_css_selector('.span-success').click()
sleep(3)
driver.find_element_by_css_selector('[value="share"]').click()
driver.find_element_by_css_selector('.span9').send_keys(1234567890123)
tag = driver.find_element_by_css_selector(".CodeMirror-code")

# driver.find_element_by_css_selector(".span-primary.submit_btn").click()
# driver.find_element_by_css_selector(".span-common").click()
# driver.back()
sleep(5)


action=ActionChains(driver)
action.click(tag).send_keys("123")
action.key_down(Keys.COMMAND)
action.send_keys("a")
action.key_up(Keys.COMMAND)
action.key_down(Keys.COMMAND)
action.send_keys("b")
action.key_up(Keys.COMMAND)

action.perform()

