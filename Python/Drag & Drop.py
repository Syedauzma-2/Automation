import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\lts\\PycharmProjects\\Automation\\Drivers\\chromedriver.exe")

driver.get("http://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(4)

driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))
source = driver.find_element_by_xpath("//div[@id='draggable']")
time.sleep(4)
target = driver.find_element_by_xpath("//div[@id='droppable']")
time.sleep(3)
mouse = ActionChains(driver).drag_and_drop(source,target)
mouse.perform()

time.sleep(5)