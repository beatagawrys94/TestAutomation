import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import functions

class TC_1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_TC_1(self):
        driver = self.driver
        driver.get("http://www.python.org")
        lol=functions.findField(driver)
        lol.send_keys("lol")
        go=functions.findSearchButton(driver)
        go.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
