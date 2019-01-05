import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


import functions

class TC_1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("http://www.python.org")
        time.sleep(2)

    def test_TC_1(self):
        driver = self.driver
        #driver.get("http://www.python.org")
        lol=functions.findField(driver)
        lol.send_keys("lol")
        teksts = lol.get_attribute('value')
        assert "lol" in teksts
        go=functions.findSearchButton(driver)
        go.click()
        time.sleep(2)
        sr2=functions.search2(driver)
        sr2.clear()
        sr2.send_keys("Python")
        tekst=sr2.get_attribute('value')
        assert "Python" in tekst
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
