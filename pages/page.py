import abc
from decorators.error_handling_dec import ErrorHandler

__author__ = 'Evgen'

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.expected_conditions import *


class Page(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_element_located(locator))
        except WebDriverException:
            return False

    def try_get_visible_element(self, locator):
        return self.wait.until(visibility_of_element_located(locator))

    @ErrorHandler("page generation is failed")
    def wait_until_page_generate(self):
        return self.wait.until(presence_of_element_located(self.SPINNER_OFF))

    @abc.abstractmethod
    def is_current_page(self):
        return
