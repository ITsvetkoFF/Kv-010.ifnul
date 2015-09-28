__author__ = 'Evgen'
from page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class InternalPage(Page):
    INTERNAL_PAGE = (By.CSS_SELECTOR, "nav")
    USER_DROPDOWN = (By.XPATH, "//i[@class='fa fa-user fa-fw']")
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='dropdown open']//a[@ng-click='header.logout()']")
    PERSON_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.person.list']")
    ENROLLMENT_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.enrolment.list']")
    DICTIONARIES_PAGE_LINK = (By.XPATH, "//a[@ui-sref='root.dictionaries']")

    @property
    def user_dropdown(self):
        return self.driver.find_element(*self.USER_DROPDOWN)

    @property
    def logout_button(self):
        return self.driver.find_element(*self.LOGOUT_BUTTON)

    @property
    def is_this_page(self):
        return self.is_element_visible(self.INTERNAL_PAGE)

    @property
    def person_page_link(self):
        return self.driver.find_element(*self.PERSON_PAGE_LINK)

    @property
    def enrollment_page_link(self):
        return self.driver.find_element(*self.ENROLLMENT_PAGE_LINK)

    @property
    def dictionaries_page_link(self):
        return self.driver.find_element(*self.DICTIONARIES_PAGE_LINK)
