# coding:utf-8
from handle import login_handle


class LoginBusiness:

    def __init__(self, driver):
        self.handle = login_handle.LoginHandle(driver)

    def right_login(self):
        self.handle.clear_account()
        self.handle.send_keys_account()
        self.handle.clear_password()
        self.handle.send_keys_password()
        self.handle.click_login()
