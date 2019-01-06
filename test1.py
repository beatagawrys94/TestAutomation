import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import functions

class TC_1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.python.org")
        time.sleep(2)

    def test_TC_1(self):
        driver = self.driver
        # driver.get("http://www.python.org")

        # first step
        lol = functions.findField(driver)
        lol.send_keys("lol")
        teksts = lol.get_attribute('value')
        self.assertEqual("lol", teksts, "Text is successfully inputed")

        # second step
        go = functions.findSearchButton(driver)
        go.click()
        time.sleep(2)

        #---
        sr2 = functions.search2(driver)
        sr2.clear()
        sr2.send_keys("Python")
        tekst = sr2.get_attribute('value')
        self.assertEqual("Python", tekst, "Text is successfully inputed")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
