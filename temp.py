from selenium import webdriver
import time
import unittest
from selenium.common.exceptions import NoSuchElementException

class SeleniumTest(unittest.TestCase):

    # test data
    __website_path = "https://www.amazon.com/"

    @classmethod
    def setUpClass(cls):
        """initialize the browser and opens the page"""
        # paste the chromedriver in this location : C:\Program Files\Python37 (python installation folder)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

        # open the page and enter the keyword
        cls.driver.get(cls.__website_path)

    def test_search_keyword(self):
        search_field = self.driver.find_element_by_name('q')
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # close the browser
        cls.driver.minimize_window()


# this line makes the current file executable file, verbosity helps to display more details in execution result
if __name__ == '__main__':
    unittest.main(verbosity=2)
