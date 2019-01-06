import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import functions

class TC_2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.python.org")
        time.sleep(2)

    def test_TC_2(self):
        driver = self.driver
        #driver.get("http://www.python.org")

        #first step'

        functions.about(driver).click()
        time.sleep(2)

        functions.downloads(driver).click()
        time.sleep(2)

        functions.doc(driver).click()
        time.sleep(2)


        time.sleep(2)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
