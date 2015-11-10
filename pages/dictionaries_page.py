from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

from decorators.error_handling_dec import ErrorHandlerPO
from pages.internal_page import InternalPage
from utils.web_elem_utils import dropdown_select_by_text, dropdown_select_by_index

__author__ = 'Denys'


class DictionariesPage(InternalPage):
    # locators
    DICTIONARIES_PAGE_ID = (By.XPATH, "//i[@class ='fa fa-book text-danger']")
    DICTIONARIES_DROPDOWN = (By.XPATH, "//select[@ng-click ='pickDictionary()']")
    DICTIONARIES_PAGE_TABLE = (By.XPATH, "//table")
    BUTTON_DISPLAY_BY_10 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[1]")
    BUTTON_DISPLAY_BY_25 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[2]")
    BUTTON_DISPLAY_BY_50 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[3]")
    BUTTON_DISPLAY_BY_100 = (By.XPATH, "//div[contains(@class,'ng-table-counts')]/button[4]")
    PAGE_BUTTON_NEXT = (By.XPATH, "//ul[@class='pagination ng-table-pagination']/li/a[@ng-switch-when='next']")
    PAGE_BUTTON_PREV = (By.XPATH, "//ul[@class='pagination ng-table-pagination']/li/a[@ng-switch-when='prev']")

    # TABLE_HEAD_CELL = "//table/thead/tr/td[%d]"
    # TABLE_HEAD_LAST_CELL = "//table/thead/tr/td[last()]"
    #
    # TABLE_BODY_CELL = ("//table/tbody/tr[%d]/td[%d]")
    # TABLE_BODY_LAST_CELL_IN_I_ROW = ("//table/tbody/tr[%d]/td[last()]")
    # TABLE_BODY_LAST_CELL_IN_LAST_ROW = ("//table/tbody/tr[last()]/td[last()]")

    def is_this_page(self):
        return self.driver.find_element(*self.DICTIONARIES_PAGE_ID)

    @property
    def table(self):
        return self.driver.find_element(*self.DICTIONARIES_PAGE_TABLE)

    @property
    def dictionaries_select_elem(self):
        return self.driver.find_element(*self.DICTIONARIES_DROPDOWN)

    @property
    def button_10(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_10)

    @property
    def button_25(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_25)

    @property
    def button_50(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_50)

    @property
    def button_100(self):
        return self.driver.find_element(*self.BUTTON_DISPLAY_BY_100)

    @property
    def button_next(self):
        return self.is_element_visible(self.PAGE_BUTTON_NEXT)

    @property
    def button_prev(self):
        return self.is_element_visible(self.PAGE_BUTTON_PREV)

    # web elem function
    def select_dictionary_by_name(self, text):
        dropdown_select_by_text(self.dictionaries_select_elem, text)
        self.wait_until_page_generate()

    def select_dictionary_by_option_value(self, index):
        dropdown_select_by_index(self.dictionaries_select_elem, index)
        self.wait_until_page_generate()



        # def try_get_table_head_cell_i(self, i):
        #     return self.is_element_visible((By.XPATH, self.TABLE_HEAD_CELL % i))
        #
        # def try_get_table_head_cell_last(self):
        #     return self.is_element_visible((By.XPATH, self.TABLE_HEAD_LAST_CELL))
        #
        # def try_get_table_body_cell_i_j(self, i, j):
        #     return self.is_element_visible((By.XPATH, self.TABLE_BODY_CELL % (i, j)))
        #
        # def try_get_table_body_last_cell_in_i_row(self, i):
        #     return self.is_element_visible((By.XPATH, self.TABLE_BODY_LAST_CELL_IN_I_ROW % i))
        #
        # def try_get_table_body_last_cell_in_last_row(self):
        #     return self.is_element_visible((By.XPATH, self.TABLE_BODY_LAST_CELL_IN_LAST_ROW))
