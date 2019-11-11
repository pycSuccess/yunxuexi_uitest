# coding:utf-8
from page import login_page


class LoginHandle:

    def __init__(self, driver):
        self.page = login_page.LoginPage(driver)

    def clear_password(self):
        self.page.get_editor_password().clear()

    def clear_account(self):
        self.page.get_editor_account().clear()

    def send_keys_password(self):
        self.page.get_editor_password().send_keys('18510913395')

    def send_keys_account(self):
        self.page.get_editor_account().send_keys('123456Ww')

    def click_login(self):
        self.page.get_login_button().click()
