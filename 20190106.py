from selenium import webdriver
import time
driver = webdriver.Chrome()
print(driver)
print(type(driver))
#driver.get("https://www.baidu.com")
"""
> 上下级关系（子元素）
# id属性的值
. class属性的值
:ntl-child(index) 第index子元素


"""
driver.get("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=1c47d7931fce428882100d0a5621b86a")
#l=driver.find_elements_by_css_selector(".gl-item>div>div.p-img>a:nth-child(1)")
l=driver.find_elements_by_xpath('//*[@class="gl-item"]//*[@class="p-img"]//img')
#l=driver.find_elements_by_css_selector(".gl-i-wrap")
for i in range(len(l)):

    #l = driver.find_elements_by_css_selector(".gl-item>div>div.p-img>a:nth-child(1)")
    #print(len(l))
    l[i].click()
    win_list=driver.window_handles
    driver.switch_to.window(win_list[1])
    time.sleep(5)
    text=driver.find_element_by_xpath('//*[@class="p-price"]/span[2]').text
    #text = driver.find_element_by_css_selector('.p-price>span:nth-child(2)').text
    print(text)
    driver.close()
    driver.switch_to.window(win_list[0])

#driver.find_element_by_name("tj_trnews").click()
# navs=driver.find_elements_by_xpath('//*[@class="mnav"]')
# print(navs)
# print(len(navs))
# for i in range(len(navs)):
#     navs = driver.find_elements_by_xpath('//*[@class="mnav"]')
#     print(navs)
#     navs[i].click()
#     time.sleep(3)
#     driver.back()
#     time.sleep(3)

def search():

    baidu_input=driver.find_element_by_xpath('//*[@id="kw"]')
    baidu_input.send_keys("helloword")
    driver.find_element_by_id("su").click()
    baidu_input.clear()
    baidu_input.send_keys("凡猫")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    result = driver.find_element_by_xpath('//*[@id="content_left"]')
    print(result.text)
    str=result.text
    with open('data.txt','w') as f:    #设置文件对象
        f.write(str)


