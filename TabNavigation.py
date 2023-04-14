from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')

    def test_opentab(self):
        driver = self.driver
        driver.get('http://www.google.com')
        time.sleep(4)
        driver.execute_script('window.open('');')
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://www.facebook.com/')
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(4)
if __name__ == '__main__':
    unittest.main()
