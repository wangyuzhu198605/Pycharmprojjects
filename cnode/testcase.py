import unittest
from selenium import webdriver
from cnode.login import login
from cnode.shouye import first_page
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):

        self.driver = webdriver.Chrome()
        driver=self.driver
        driver.get("http://39.107.96.138:3000/")

    @classmethod
    def tearDownClass(self):
        driver = self.driver
        driver.close()
    def test_1case(self):

        login(self.driver)
        time.sleep(2)
    def test_2case(self):
        first_page(self.driver)
        time.sleep(2)
if __name__=="__main__" :
    unittest.main()












