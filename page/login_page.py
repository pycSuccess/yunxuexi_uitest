# coding:utf-8
class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_password_text(self):
        return self.driver.find_element_by_xpath('//*[contains(@text, "密码登录")]')

    def get_yan_text(self):
        return self.driver.find_element_by_xpath('//*[contains(@text, "验证码登录":)]')

    def get_editor_account(self):
        return self.driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_username')

    def get_editor_password(self):
        return self.driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_password')

    def get_login_button(self):
        return self.driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_button')
