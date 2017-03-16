#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#定位到要悬停的元素,百度搜索页面的设置元素
above = driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_settingicon']")
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(above).perform()
driver.quit()
print "ok!"

'''其他的鼠标操作有右击ActionChains(driver).context_click(element).perform;
    双击ActionChains(driver).double_click(element).perform();
    拖拽ActionChains(driver).drag_and_drop(element,target).perform()
    '''