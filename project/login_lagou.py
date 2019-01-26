from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import HTMLReport
import time
import unittest
driver = webdriver.Chrome()
class  Test(unittest.TestCase) :
    driver = webdriver.Chrome()
    def test_login(self):
        

        driver=self.driver
        driver.get('https://www.lagou.com/') #打开拉勾网
        driver.find_element_by_xpath('//*[text()="上海站"]').click() #选中上海站
        driver.find_element_by_xpath('//*[text()="登录"]').click()  #点击登录按钮
        locator=(By.XPATH,'//*[contains(text(),"密码登录")]')
    #WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located(locator))#等待元素出现
    #WebDriverWait(driver,5).until(lambda x : x.find_element_by_xpath('//*[contains(text(),"密码登录")]'))

        WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath('//*[contains(text(),"密码登录")]').is_displayed)
        driver.find_element_by_xpath('//*[@placeholder="请输入常用手机号/邮箱"]').send_keys('970257785@qq.com')
        driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys("wyz34508")
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        time.sleep(20)
        a=driver.find_element_by_xpath('//*[@class="unick bl"]').text
        print(a)
        self.assertEqual(a,"王玉柱")
        #WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@class="unick bl"]'))
unittest.main()


