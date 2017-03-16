#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element = WebDriverWait(driver, 5, 0.5, None).until(EC.presence_of_element_located(By.ID, 'kw'), u'元素可见')

element.send_keys('selenium')
driver.quit()


'''expected_conditions提供了其他的预期条件实现的方法：
   title_is 判断标题是否**
   title_contains 判断标题是否包含**
   presence_of_element_located 判断元素是否存在
   visible_of_element_located 判断元素是否可见
   visible_of 是否可见
   presence_of_all_element_located 判断一组元素是否可见
   text_to_be_present_in_element 判断元素是否有xx文本信息
   '''