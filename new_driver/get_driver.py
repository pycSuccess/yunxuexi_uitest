# coding:utf8
from appium import webdriver


class Driver:
    def __init__(self, flag):
        if flag == 'Android':
            self.caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'app': 'C:/Users/Administrator/Desktop/xes_test.apk',
                'automationName': 'UiAutomator2',
                'appActivity': 'com.xes.jazhanghui.activity.mvp.start.SafePolicyActivity'  # 如果是启动问题需要加入appActivity

            }
        else:
            self.caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'app': 'C:/Users/Administrator/Desktop/xes_test.apk',
                'automationName': 'UiAutomator2',
                'appActivity': 'com.xes.jazhanghui.activity.mvp.start.SafePolicyActivity'  # 如果是启动问题需要加入appActivity
            }

    def android_driver(self):
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.caps)

