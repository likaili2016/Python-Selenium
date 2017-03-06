#coding=utf-8

from selenium import webdriver

''''''

driver = webdriver.Chrome()
driver.get("http://mail.126.com/")
driver.find_element_by_id("auto-id-1488716345873").clear()  # 清空文本框内容
driver.find_element_by_id("auto-id-1488716345873").send_keys("test2")  # 输入账号信息
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("aaa111")  # 输入密码
driver.find_element_by_id("dologin").click()  # 点击登录按钮

driver.quit()