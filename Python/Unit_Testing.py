from selenium import webdriver
import time
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    #set up class method is used because only once we want to open the browser
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\lts\\PycharmProjects\\Automation\\Drivers\\chromedriver.exe")

    def test_login(self):
        self.driver.get("http://opensource-demo.orangehrmlive.com/")

        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")

        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")

        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()