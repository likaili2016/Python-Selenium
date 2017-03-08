#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http:www.baidu.com")
driver.find_element_by_id("kww")
driver.find_element_by_id("kw").send_keys("selenium")
sleep(10)
driver.quit()

'''implicitly_wait()与sleep的区别：前者设置的是一个超时时间，不影响脚本的执行速度，
   如果元素定位到了继续执行，定位不到则会轮询一直到设置的时间之后会抛出异常。
   sleep则是固定的等待
'''