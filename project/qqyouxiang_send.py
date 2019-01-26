count =0
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://mail.qq.com')
browser.switch_to.frame("login_frame")
browser.find_element_by_id('switcher_plogin').click()
browser.find_element_by_class_name('inputstyle').send_keys('970257785@qq.com')
browser.find_element_by_id('p').send_keys('wyzceshi198605')
browser.find_element_by_id('login_button').click()
time.sleep(10)
useraddr=browser.find_element_by_id('useraddr').text
if useraddr=='970257785@qq.com':
    browser.find_element_by_id('composebtn').click()
    time.sleep(5)
    browser.switch_to.frame(browser.find_element_by_id('mainFrame'))
    browser.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input").send_keys('970257785@qq.com')
    browser.find_element_by_id('subject').send_keys('i send this message by PythonScript ! HAHA')
    try:
        zhegnwen=browser.find_element_by_xpath("//*[@id='QMEditorArea']/table/tbody/tr/td/iframe")
        browser.switch_to.frame(zhegnwen)
        browser.find_element_by_xpath("/html/body").send_keys('ceshijieguo')
        browser.switch_to.default_content()
        browser.switch_to.frame(browser.find_element_by_id('mainFrame'))
        time.sleep(2)
        browser.find_element_by_css_selector("#toolbar > div > a:nth-child(1)").click()
        time.sleep(5)
    finally:
        browser.switch_to.default_content()
        browser.find_element_by_link_text('退出').click()
        time.sleep(5)
        browser.quit()