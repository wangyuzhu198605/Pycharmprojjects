import unittest
import logging
#FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
FORMAT = '%(asctime)-15s-%(action)s-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'user0'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem:s%', 'connection reset', extra=d)
from selenium import webdriver
import time

from time import gmtime,strftime
import HTMLReport

logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')
class Test(unittest.TestCase):
    def setUp(self):
        pass
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        driver=cls.driver
    @unittest.skip("demonstrating skipping")
    def test_login(self):
        d = {'clientip': '192.168.0.1', 'user': 'user0','action':"Test"}
        logging.warning('testupper:',extra=d)

        driver=self.driver
        driver.get("http://39.107.96.138:3000/")
        driver.find_element_by_css_selector('li>a[href="/signin"]')
        time.sleep(5)
        driver.find_element_by_css_selector('[id="name"]').send_keys('user0')
        driver.find_element_by_css_selector('[id="pass"]').send_keys('123456')

    def test_first_page(self):
        # 用例：发布话题
        driver=self.driver
        driver.get("http://39.107.96.138:3000/")
        driver.find_element_by_xpath('//*[text()="首页"]').click()
        #driver.find_element_by_xpath('//li//*[@href="/topic/5c31d8439a1b06054f50c8df"]').click()
    def tearDown(self):
        driver=self.driver
        pngname=strftime("%Y_%b_%d_%H_%M_%S", gmtime())
        driver.save_screenshot(pngname+".png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
# if __name__=="__main__":test_first_pagetest_first_page
#     unittest.main(verbosity=3)test_login
#suite = unittest.TestSuite()
#suite.addTest(Test('test_login'))
#suite.addTests(Test('test_first_page'))
suite = unittest.TestLoader().loadTestsFromTestCase(Test)
# def suite2():
#     suite = unittest.TestSuite()
#     loader = unittest.TestLoader().discover('./',pattern='test_*')
#     loader2=unittest.TestLoader().discover('./',pattern='test_*')
#     suite.addTests(loader)
#     return suite
# runer=unittest.TextTestRunner(verbosity=3)
# runer.run(suite2())
#loader  = unittest.TestLoader()
runner  = HTMLReport.TestRunner(report_file_name = 'test',
                               output_path = 'report',
                               title = '测试报告',
                               description = '无测试描述',
                               thread_count = 1,
                               thread_start_wait = 3 )
runner.run(suite)
