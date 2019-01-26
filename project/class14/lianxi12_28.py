import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import HTMLReport
from HTMLTestRunner_PY3 import HTMLTestRunner
"""
测试账户:
用户名：user1  
密码：123456
"""

class Cnode(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000/'
        self.driver = webdriver.Chrome()
        driver=self.driver
        driver.get(self.Url)
        driver.maximize_window()
        # 登陆用户
        driver.find_element_by_css_selector('a[href="/signin"]').click()
        # 用户名
        driver.find_element_by_id('name').send_keys('user0')
        # 密码
        driver.find_element_by_id('pass').send_keys('123456')
        # 登陆
        driver.find_element_by_css_selector('input[type="submit"]').click()

    def tearDown(self):
        self.driver.save_screenshot('./posttopic.png')
        self.driver.close()

    def  test_post_topic(self):
        driver=self.driver
        driver.find_element_by_xpath('//*[text()="发布话题"]').click()
        driver.find_element_by_xpath('//*[text()="分享"]').click()
        driver.find_element_by_xpath('//*[@id="title"]').send_keys("1234567890")
        a = driver.find_element_by_xpath('//*[@class="CodeMirror-code"]/*[name()="pre"]')
        ActionChains(driver).click(a).send_keys("123456").perform()
        #driver.find_element_by_xpath('//*[@class="CodeMirror-code"]/pre').send_keys("123")
        driver.find_element_by_xpath('//*[@type="submit"]').click()
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(Cnode))


f = open('./log.html', 'wb')
runner = HTMLReport.TestRunner(
    title="UI自动化测试报告",
    description="用例测试情况",
    #stream=f,
    #verbosity=3,
    )



#
# if __name__ == "__main__":
#     unittest.main()

runner.run(suite)



