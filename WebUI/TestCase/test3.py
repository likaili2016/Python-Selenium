#coding=utf-8

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 获得输入框的尺寸
size = driver.find_element_by_id("kw").size
print size
#返回百度底部备案的文案信息
text = driver.find_element_by_id("jgwab").text
print text
#返回输入框元素的属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print attribute
#返回输入框元素是否可见
status = driver.find_element_by_id("kw").is_displayed()
print status

driver.quit()
