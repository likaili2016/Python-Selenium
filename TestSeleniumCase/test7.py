#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

input_ = driver.find_element_by_id("kw")
element = WebDriverWait(driver, 5, 0.5).until(lambda driver : input_.is_displayed())

input_.send_keys("selemiun")
driver.quit()