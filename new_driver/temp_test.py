# # coding:utf-8
#
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions \
#     as EC
# import time
# print(driver.current_activity)
# element_path = ('xpath', "//*[@text='同意']")
# element = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(element_path))
# element.click()
# size = driver.get_window_size()
# print(size)
# time.sleep(1)
# # driver.find_element_by_xpath('//*[contains(@text,"看看")]').click()
# driver.find_element_by_xpath('//*[contains(@text,"学而思账号登录")]').click()
# '''
# 进入课堂页
# '''
# # classRoom_ele = driver.find_element_by_android_uiautomator('text(\"课堂\")')
# # classRoom_ele = driver.find_element_by_android_uiautomator('new UiSelector().text(\"课堂\")')
# # classRoom_ele.click()
# # time.sleep(1)
# # driver.find_element_by_id('com.xes.jazhanghui.activity:id/tv_empty_status_btn').click()
# pass_login_path = ('xpath', "//*[@text='验证码登录']")
# flag = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(pass_login_path))
# if flag:
#     flag.click()
# else:
#     driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_username').clear()
#     driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_username').send_keys('18510913395')
#     driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_password').clear()
#     driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_password').send_keys('123456Ww')
#     time.sleep(1)
#     driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_button').click()
#     toast_path = ('xpath', '//*[contains(@text, "系统开小差")]')
#     toast = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(toast_path))
#     if toast:
#         time.sleep(1)
#         driver.find_element_by_id('com.xes.jazhanghui.activity:id/xes_login_button').click()
#     time.sleep(5)
#     driver.quit()
