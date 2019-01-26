class LoginPage(object):

    def __init__(self,driver, username,password):
        self.driver = driver
        self.username = username
        self.password = password
    
    
    def login(self):
        """
        用户登陆的操作
        """
        self.driver.get('http://39.107.96.138:3000/signin')
        self.driver.find_element_by_id('name').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.password)
        self.driver.find_element_by_css_selector('[type="submit"]').click()
    

    def get_login_name(self):

        """
        登陆成功后 获取用户名
        return  str
        """

        username = self.driver.find_element_by_css_selector('.user_name > a.dark').text
        return username
