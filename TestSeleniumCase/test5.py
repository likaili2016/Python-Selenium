#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumm")
#删除多输入的一个m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#输入空格+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
#全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'A')
#剪切全中的内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'X')
#将剪切的内容复制到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'V')
#通过回车键来代替点击操作
driver.find_element_by_id("kw").send_keys(Keys.ENTER)

driver.quit()
print "运行成功！"