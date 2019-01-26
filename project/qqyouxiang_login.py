from selenium import webdriver
import traceback
import time
import datetime
import traceback
import logging
import os
import time
import datetime
import traceback
import logging
import os
# 测试用来执行函数
def login(browser):
    url = "https://mail.qq.com/"

    browser.get(url)

    # 输入账号和密码
    try:
        browser.switch_to_frame("login_frame")
        browser.find_element_by_css_selector('#u').send_keys("970257785@qq.com") # 输入用户名
        time.sleep(1) # 睡眠1秒钟
        browser.find_element_by_css_selector('#p').send_keys("wyzceshi198605") # 输入密码
        # 点击按钮提交登录表单
        browser.find_element_by_css_selector("#login_button").click() # 点击登录按钮

        browser.switch_to_default_content()
# 验证登录成功的URL
        time.sleep(5)

        #print(len(browser.find_elements_by_css_selector('[initlized="true"]')))
        if len(browser.find_elements_by_xpath("//*[text()='邮箱首页']")) ==0:

            #currUrl == "https://mail.qq.com/cgi-bin/frame_html?sid=XCVJv0oXo3dPDjdr&r=d6b891a71183d9f38617f49b05ac794a":
            traceback.print_exc(u"success")
        else:
            traceback.print_exc(u"failure")
        login_Log()
    except:
        print(u"failure")
        login_Log() # 跟踪日志
# 写错误日志并截图
def login_Log():
# 组合日志文件名（当前文件名+当前时间）.比如：case_login_success-20150817192533
    basename = os.path.splitext(os.path.basename(__file__))[0]
    print(basename)
    logFile = basename+"-"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".log"
    logging.basicConfig(filename=logFile) # 将日志记录到文件中
    s = traceback.format_exc()
    logging.error(s) # 记录错误的日志
    browser.get_screenshot_as_file("./"+logFile+"-error.png") # 截取登录的图片
if __name__ == "__main__":
    browser = webdriver.Chrome() # 启动chrome浏览器
    login(browser) # 登录qq邮箱
    #rowser.quit() # 退出浏览器