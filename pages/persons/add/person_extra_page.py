#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Deorditsa'

from utils.web_elem_utils import checkbox_set_state
from utils.common_methods import CommonMethods
from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By


class AddPersonExtraPage(AddPersonPage):
    ACTIVATE_BIRTH_DAY_CHOOSER = (By.XPATH, "//input[@ng-model='person.begDate']")
    SEX_TYPES_SELECT = (By.XPATH, "//div[@id='genderTypeId']//div//span")
    ALL_SEX_TYPES_SELECT = (By.XPATH, "//div[@id='genderTypeId']//a//div")
    MARITAL_STATUS_SELECT = (By.XPATH, "//div[@id='marriedTypeId']//div[@class='ui-select-match']/span")
    # MARITAL_STATUS_SELECT = (By.ID, "marriedTypeId")
    ALL_MARITAL_STATUSES_SELECT = (By.XPATH, "//div[@id='marriedTypeId']//a//div")
    NATIONALITY_SELECT = (By.XPATH, "//div[@id='citizenCountryId']//div/span//span[@class='ng-binding ng-scope']")
    ALL_NATIONALITIES_SELECT = (By.XPATH, "//div[@id='citizenCountryId']//a//div")
    PRIVATE_CASE_CHARS_INPUT = (By.XPATH, "//input[@id='docSeries']")
    PRIVATE_CASE_NUMBER_INPUT = (By.XPATH, "//input[@id='docNum']")
    PRIVATE_CASE_NUMBER_INPUT_INCORRECT = (By.XPATH, "//input[@id='docNum'][contains (@class, 'ng-invalid-pattern')]")
    IS_A_OUTLANDER_CHECKER = (By.XPATH, "//input[@ng-checked='person.resident']")
    IS_A_MILITARY_CHECKER = (By.XPATH, "//input[@ng-checked='person.isMilitary']")
    NEED_HOSTEL_CHECKER = (By.XPATH, "//input[@ng-checked='person.isHostel']")

    def is_this_page(self):
        return self.is_element_visible(self.ACTIVATE_BIRTH_DAY_CHOOSER)

    def active_birth_day_chooser(self):
        return self.is_element_visible(self.ACTIVATE_BIRTH_DAY_CHOOSER)

    def sex_types_select(self):
        return self.is_element_visible(self.SEX_TYPES_SELECT)

    def marital_status_select(self):
        return self.is_element_visible(self.MARITAL_STATUS_SELECT)

    def nationality_select(self):
        return self.is_element_visible(self.NATIONALITY_SELECT)

    def private_case_chars_input(self):
        return self.is_element_visible(self.PRIVATE_CASE_CHARS_INPUT)

    def private_case_number_input(self):
        return self.is_element_visible(self.PRIVATE_CASE_NUMBER_INPUT)

    # web element
    @property
    def checkbox_is_outlander(self):
        return self.driver.find_element(*self.IS_A_OUTLANDER_CHECKER)

    @property
    def checkbox_is_hostel_need(self):
        return self.driver.find_element(*self.NEED_HOSTEL_CHECKER)

    @property
    def checkbox_is_military(self):
        return self.driver.find_element(*self.IS_A_MILITARY_CHECKER)

    @property
    def private_case_number_input_incorrect(self):
        return self.is_element_visible(self.PRIVATE_CASE_NUMBER_INPUT_INCORRECT)

    def set_persons_birth_day(self, date):
        """
        Method sets persons birth day
        :param date: Date, when person was burn in a datetime format
        :return:
        """
        self.set_date(self.ACTIVATE_BIRTH_DAY_CHOOSER, date)

    def choose_person_sex_type(self, person_sex_type):
        """
        Method performs choosing concrete person sex type
        :param person_sex_type: if person_sex_type exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.SEX_TYPES_SELECT)
        self.driver.find_element(*self.SEX_TYPES_SELECT).click()
        self.find_element_in_select(self.driver.find_elements(*self.ALL_SEX_TYPES_SELECT), person_sex_type).click()

    def choose_person_martial_status(self, person_martial_status):
        """
        Method performs choosing concrete person martial status
        :param person_martial_status: if person_martial_status exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.MARITAL_STATUS_SELECT)
        self.driver.find_element(*self.MARITAL_STATUS_SELECT).click()
        self.find_element_in_select(self.driver.find_elements(*self.ALL_MARITAL_STATUSES_SELECT),
                                    person_martial_status).click()

    def choose_person_nationality(self, person_nationality):
        """
        Method performs choosing concrete person sex type
        :param person_nationality: String format. If person_nationality exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.NATIONALITY_SELECT)
        self.driver.find_element(*self.NATIONALITY_SELECT).click()
        self.find_element_in_select(self.driver.find_elements(*self.ALL_NATIONALITIES_SELECT),
                                    person_nationality).click()

    def set_private_case_chars(self, chars):
        """
        Method sets the persons private case series
        :param chars: String format. Persons private case series
        :return:
        """
        self.emulation_of_input(self.PRIVATE_CASE_CHARS_INPUT, chars)

    def set_private_case_numbers(self, numbers):
        """
        Method sets the persons private case number
        :param numbers: String format. Persons private case number
        :return:
        """
        self.emulation_of_input(self.PRIVATE_CASE_NUMBER_INPUT, numbers)



    # web element function
    def check_resident_status(self, is_outlander):
        """
        Method checks or unchecks "Is person outlander?" checkbox
        :param is_outlander: Boolean format. Must be True, if person is outlander.
        :return:
        """
        checkbox_set_state(self.checkbox_is_outlander, is_outlander)

    def check_needed_hostel_status(self, is_need):
        """
        Method checks or unchecks "Is person need a hostel?" checkbox
        :param is_need: Boolean format. Must be True, if person need a hostel.
        :return:
        """
        checkbox_set_state(self.checkbox_is_hostel_need, is_need)

    def check_reservist_status(self, is_reservist):
        """
        Method checks or unchecks "Is person reservist?" checkbox
        :param is_reservist: Boolean format. Must be True, if person is reservist.
        :return:
        """
        checkbox_set_state(self.checkbox_is_military, is_reservist)

    # general functions
    def fill_in_extra_person_page(self, person):
        """
        Method fill in data on the extra persons page
        :param person: persons model in Person format
        :return:
        """
        self.is_this_page()
        self.set_persons_birth_day(person.birth_day)
        self.choose_person_sex_type(person.sex)
        self.choose_person_martial_status(person.marital_status)
        self.choose_person_nationality(person.nationality)
        self.set_private_case_chars(person.private_case_chars)
        self.set_private_case_numbers(person.private_case_number)
        self.check_resident_status(person.is_outlander)
        self.check_reservist_status(person.reservist)
        self.check_needed_hostel_status(person.hostel_need)

    def read_in_extra_person_page(self, person_new):
        """
        Method read the data on the extra persons page
        :param person_new: persons model in Person format
        :return:
        """
        common_methods = CommonMethods(self.driver)
        self.is_this_page
        person_new.birth_day = common_methods.get_value_from_text_field(
            self.driver.find_element(*self.ACTIVATE_BIRTH_DAY_CHOOSER))
        person_new.sex = self.sex_types_select().text
        person_new.marital_status = self.marital_status_select().text
        person_new.nationality = self.nationality_select().text
        person_new.private_case_chars = common_methods.get_value_from_text_field(
            self.driver.find_element(*self.PRIVATE_CASE_CHARS_INPUT)).encode('cp1251')
        person_new.private_case_number = common_methods.get_value_from_text_field(
            self.driver.find_element(*self.PRIVATE_CASE_NUMBER_INPUT))
        person_new.is_outlander = common_methods.is_checkbox_checked(
            self.driver.find_element(*self.IS_A_OUTLANDER_CHECKER))
        person_new.reservist = common_methods.is_checkbox_checked(
            self.driver.find_element(*self.IS_A_OUTLANDER_CHECKER))
        person_new.hostel_need = common_methods.is_checkbox_checked(
            self.driver.find_element(*self.IS_A_OUTLANDER_CHECKER))
        return person_new
