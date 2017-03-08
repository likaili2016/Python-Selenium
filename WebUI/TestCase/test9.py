#coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
#设置超时时间为10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#获得百度搜索窗口句柄
search_windows = driver.current_window_handle

driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_link_text(u'立即注册').click()

#获得当前浏览器打开的所有窗口的句柄

all_handles = driver.window_handles

#进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to_window(handle)
        print "now is register window !"
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_name("password").send_keys("password")

#进入搜索窗口
for handle in all_handles:
    if handle == search_windows:
        driver.switch_to_window(handle)
        print "now search window!"


driver.quit()
