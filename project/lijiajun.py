from selenium import webdriver
import unittest
import time
import xlrd

class Testnode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://39.107.96.138:3000/')
        cls.driver.maximize_window()


    def testlogin(self):

        driver = self.driver

        driver.find_element_by_xpath("/html/body/div[1]/div/div/ul/li[6]/a").click()
        # excel = xlrd.open_workbook('E:\login.xls')
        # sheet = excel.sheet_by_index(0)
        # for i in range(sheet.nrows):
        #     name = sheet.row_values(i)[0]
        #     word = int(sheet.row_values(i)[1])
        #     print(word)
        driver.find_element_by_xpath('//*[@id="name"]').send_keys("user0")
        driver.find_element_by_id("pass").send_keys("123456")
        driver.find_element_by_xpath('//*[@id="signin_form"]/div[3]/input').click()
        if driver.find_element_by_xpath('//*[text()="个人信息"]').is_displayed():
            print('登陆成功')
        else:
            print('登录失败')

    def testview(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@class="topic_title_wrapper"]/a[1]').click()
        driver.execute_script('window.scrollTo(0,300)')
        driver.find_element_by_xpath('//*[@id="reply_form"]/div/div/div[2]/div[6]').send_keys('大四狗过来打个酱油')
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="reply_form"]/div/div/div[3]/input').click()
        time.sleep(5)
        if driver.find_element_by_xpath('//*[text()="大四狗过来打个酱油"').is_displayed():
            print("发帖成功")
        else:
            print("发帖失败")



if __name__ == '__main__':
    unittest.main()
