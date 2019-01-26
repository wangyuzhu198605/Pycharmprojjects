# import re
# a="转发 1"
# b=a.split("转发")[1]
# print(b)
#print(a[3:])
# if len(re.findall("\d+",a))>=1:
#     s = re.findall("\d+",a)[0]
#
# print()
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://s.weibo.com/')

driver.find_element_by_css_selector('div[class="search-input"] > input[type="text"]').send_keys('web自动化')
driver.find_element_by_css_selector('.s-btn-b').click()


driver.find_element_by_link_text('高级搜索').click()
driver.find_element_by_css_selector('label[for="radio03"]').click()

driver.find_element_by_link_text('搜索微博').click()
#driver.find_element_by_css_selector('[node-type="loginBtn"]').click()
sleep(10)
# driver.switch_to.alert()
# driver.find_element_by_css_selector('[class="item username input_wrap "]>input').send_keys('970257785@qq.com')
# driver.find_element_by_css_selector('.item.password.input_wrap ').send_keys('wyzceshi198605')
# driver.find_element_by_css_selector('.W_btn_a.btn_34px').click()
eles = driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')
elesx=driver.find_elements_by_xpath('//*[@action-type="feed_list_item"]')
print(eles)
for ele in elesx:
    #text_content = ele.find_element_by_css_selector('a[class="name"]').text
    text_content = ele.find_element_by_xpath('.//*[@node-type="feed_list_content"]').text
    print(text_content)
    coll = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(1)').text
    coll_num = coll.split('收藏')[1]
    print(coll_num)
    forward = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(2)').text
    forward_num = forward.split('转发')[1]
    print(forward_num)