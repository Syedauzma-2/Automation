import time
import os
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\lts\\PycharmProjects\\Automation\\Drivers\\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(5)

driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("D:\ST market  Trends.pdf")
time.sleep(3)

driver.find_element_by_id("file-submit").click()
time.sleep(3)