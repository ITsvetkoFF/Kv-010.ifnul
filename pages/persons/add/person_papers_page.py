#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Deorditsa'

from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.common_methods import CommonMethods
from selenium.webdriver.support import expected_conditions as EC


class AddPersonPapersPage(AddPersonPage):

    ADD_DOCUMENT_BUTTON = (By.XPATH, "//div[@class='row']//div[@class='col-xs-2']//button")
    SAVE_DOCUMENT_BUTTON = (By.XPATH, "//button[@ng-click='addToTable()']")
    DOCUMENT_CATEGORY_SELECT = (By.XPATH, "//select[@ng-model='currentObj.abbrName']")
    DOCUMENT_NAME_SELECT = (By.XPATH, "//select[@ng-model='currentObj.paperTypeId']")
    ALL_DOCUMENT_NAMES_SELECT = (By.XPATH, "//select[@ng-model='currentObj.paperTypeId']//option")
    DOCUMENT_SERIES_INPUT = (By.XPATH, "//input[@ng-model='currentObj.docSeries']")
    DOCUMENT_NUMBER_INPUT = (By.XPATH, "//input[@ng-model='currentObj.docNum']")
    DOCUMENT_DAY_OF_ISSUE_CHOSER = (By.XPATH, "//input[@ng-model='currentObj.docDate']")
    DOCUMENT_ISSUED_BY = (By.XPATH, "//input[@ng-model='currentObj.docIssued']")
    DOCUMENT_IS_ORIGINAL = (By.XPATH, "//input[@ng-model='currentObj.isChecked']")
    DOCUMENT_IS_FOREIGN = (By.XPATH, "//input[@ng-model='currentObj.isForeign']")
    TABLE_DOCUMENTS_NUM_ROW = (By.XPATH, "//div[@class='col-xs-12']/table/tbody/tr/td[3]")
    DELETE_FIRST_DOCUMENT_BUTTON = (By.XPATH, "//div[@class='col-xs-12']/table/tbody/tr[1]/td[13]/button[2]")
    DELETE_DOCUMENT_BUTTONS = (By.XPATH, "//div[@class='col-xs-12']/table/tbody/tr/td[13]/button[2]")

    EDIT_DOCUMENT_FIELDS = (
        By.XPATH, ".//*[@id='person']//*[@ng-show='!personView']//*[@class='row']//div[@class='col-xs-4']")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_DOCUMENT_BUTTON)

    @property
    def number_of_fields(self):
        return len(self.driver.find_elements(*self.EDIT_DOCUMENT_FIELDS))

    @property
    def press_add_new_document_button(self):
        self.driver.find_element(*self.ADD_DOCUMENT_BUTTON).click()
        self.is_element_present(self.SPINNER_OFF)

    @property
    def press_save_new_document_button(self):
        self.is_element_visible(self.SAVE_DOCUMENT_BUTTON)
        self.driver.find_element(*self.SAVE_DOCUMENT_BUTTON).click()
        self.is_element_present(self.SPINNER_OFF)

    def list_with_all_visible_element_in_document(self):
        return self.driver.find_elements(
            *(By.XPATH, ".//*[@id='person']//*[@ng-show='!personView']//*[@class='row']//div[@class='col-xs-4']/*[2]"))

    def document_type_select(self, document_type):
        """
        Method select type of document in select menu
        :param document_type: String document type. If type exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_visible(self.DOCUMENT_CATEGORY_SELECT)
        Select(self.driver.find_element(*self.DOCUMENT_CATEGORY_SELECT)).select_by_visible_text(document_type)

    def document_name_select(self, document_name):
        """
        Method select name of document in select menu
        :param document_name: String document name. If name exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_visible(self.DOCUMENT_NAME_SELECT)
        Select(self.driver.find_element(*self.DOCUMENT_NAME_SELECT)).select_by_visible_text(document_name)

    def set_document_series(self, chars):
        """
        Method sets the documents series
        :param chars: String parametr.
        :return:
        """
        self.emulation_of_input(self.DOCUMENT_SERIES_INPUT, chars)

    def set_document_number(self, number):
        """
        Method sets the documents number
        :param number: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.DOCUMENT_NUMBER_INPUT, number)

    def set_day_of_issue(self, day_of_issue):
        """
        Method sets documents day of issue
        :param day_of_issue: Date, when document was issued in a datetime format
        :return:
        """
        self.set_date(self.DOCUMENT_DAY_OF_ISSUE_CHOSER, day_of_issue)

    def set_document_maker(self, maker):
        """
        Method sets the organization which document was issued by
        :param maker: String parametr.
        :return:
        """
        self.emulation_of_input(self.DOCUMENT_ISSUED_BY, maker)

    def check_is_original_document(self, is_original):
        """
        Method checks or unchecks "Is original document?" checkbox
        :param is_original: Boolean format. Must be True, if document was compared with original.
        :return:
        """
        common_methods = CommonMethods(self.driver)
        common_methods.checkbox_manager(self.driver.find_element(*self.DOCUMENT_IS_ORIGINAL), is_original)

    def check_is_foreign_document(self, is_foreign):
        """
        Method checks or unchecks "Is foreign document?" checkbox
        :param is_foreign: Boolean format. Must be True, if document is foreign.
        :return:
        """
        common_methods = CommonMethods(self.driver)
        common_methods.checkbox_manager(self.driver.find_element(*self.DOCUMENT_IS_FOREIGN), is_foreign)

    def try_get_searched_doc_num(self, given_num):
        if type(given_num) == int:
            given_num = str(given_num)
        self.wait.until(EC.text_to_be_present_in_element(self.TABLE_DOCUMENTS_NUM_ROW, given_num))
        return self.driver.find_element(*self.TABLE_DOCUMENTS_NUM_ROW)

    def delete_first_document_in_page(self):
        if self.is_element_visible(self.DELETE_FIRST_DOCUMENT_BUTTON):
            self.driver.find_element(*self.DELETE_FIRST_DOCUMENT_BUTTON).click()
            self.is_element_present(self.SPINNER_OFF)

    def get_number_of_person_documents(self):
        return len(self.driver.find_elements(*self.DELETE_DOCUMENT_BUTTONS))

    def delete_all_person_documents(self):
        """
        Method deletes all the person's documents
        :return:
        """
        elements = self.driver.find_elements(*self.DELETE_DOCUMENT_BUTTONS)
        if elements:
            for element in elements:
                element.click()
                self.is_element_present(self.SPINNER_OFF)

    def fill_in_document_page(self, person):
        """
        Method fill in data on the papers persons page
        :param person: persons model in Person format
        :return:
        """
        self.is_this_page
        self.press_add_new_document_button
        self.document_type_select(person.documents[0].category)
        self.document_name_select(person.documents[0].document_name)
        self.set_document_series(person.documents[0].document_case_char)
        self.set_document_number(person.documents[0].document_case_number)
        self.set_day_of_issue(person.documents[0].day_of_issue)
        self.set_document_maker(person.documents[0].issued_by)
        self.check_is_original_document(person.documents[0].document_is_original)
        self.check_is_foreign_document(person.documents[0].document_is_foreign)
        self.press_save_new_document_button

    def read_in_document_page(self, person_new):
        """
        Method read the data on the papers persons page
        :param person_new: persons model in Person format
        :return: person_new
        """
        common_methods = CommonMethods(self.driver)
        self.is_this_page
        self.wait_until_page_generate()
        for index in range(1, self.get_number_of_person_documents() + 1):
            self.click_on_edit_document(index)
            document = []
            self.wait_until_page_generate()
            for web_element in self.list_with_all_visible_element_in_document():
                if web_element.tag_name == "input":
                    value_of_webelement_by_js = common_methods.get_value_from_text_field(web_element)
                    document.append(value_of_webelement_by_js)
                elif web_element.tag_name == "select":
                    value_of_webelement_by_js = common_methods.get_value_from_select(web_element)
                    document.append(value_of_webelement_by_js)

            document.append(
                common_methods.is_checkbox_checked(self.driver.find_element(*self.DOCUMENT_IS_ORIGINAL)))
            document.append(
                common_methods.is_checkbox_checked(self.driver.find_element(*self.DOCUMENT_IS_FOREIGN)))
            person_new.documents.append(document)

        return person_new

    def click_on_edit_document(self, count):
        self.driver.find_element(By.XPATH, "//div[@class='col-xs-12']/table/tbody/tr[" + str(
            count) + "]/td[13]/button[1]").click()
