import abc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from decorators.error_handling_dec import ErrorHandlerPO

__author__ = 'Evgen'


class Page(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 15)

    # locators
    SPINNER_OFF = (By.XPATH, "//div[@id='spinnerDiv' and @style='display: none;']")

    # abstracting functions
    @abc.abstractmethod
    def is_this_page(self):
        return

    # general functions
    def is_element_visible(self, locator):
        try:
            return self.wait.until(visibility_of_element_located(locator))
        except WebDriverException:
            return False

    def try_get_visible_element(self, locator):
        return self.wait.until(visibility_of_element_located(locator))

    @ErrorHandlerPO("page generation is failed")
    def wait_until_page_generate(self):
        return self.wait.until(presence_of_element_located(self.SPINNER_OFF))
