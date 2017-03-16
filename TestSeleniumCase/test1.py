#coding=utf-8

from selenium import webdriver

'''demo1 介绍了简单的使用百度搜索，
   这个case中包括的api有：
   1.driver.get() 打开网址；
   2.driver.send_keys() 向文本框中输入内容；
   3.driver.click() 单击；
   4.driver.set_window_size(a,b) 设置浏览器的宽为a，高为b；
   5.driver.maximize_window() 浏览器最大化；
   6.driver.quit() 关闭浏览器
   '''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")  # 打开到百度搜索页面
driver.find_element_by_id("kw").send_keys("selenium")  # 输入搜索内容
driver.find_element_by_id("su").click()  # 点击搜索按钮
driver.set_window_size(480, 800)   # 设置浏览器页面的大小为宽为480，高为800
driver.maximize_window()  # 浏览器自动化
driver.quit()  # 停止
print ("运行成功！")