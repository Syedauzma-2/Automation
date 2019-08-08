from selenium import webdriver
from selenium.webdriver import ActionChains
driver=webdriver.Chrome("C:\\Users\\lts\\PycharmProjects\\Automation\\Drivers\\chromedriver.exe")

driver.get("http://www.amazon.in")
driver.maximize_window()
driver.implicitly_wait(10)

element=driver.find_element_by_xpath("//a[@id='nav-link-accountList']")
hover = ActionChains(driver).move_to_element(element)
hover.perform()
driver.implicitly_wait(20)

