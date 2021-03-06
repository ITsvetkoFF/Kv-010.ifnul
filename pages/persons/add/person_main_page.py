from utils.common_methods import CommonMethods

__author__ = 'Evgen'

from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By


class AddPersonMainPage(AddPersonPage):

    PERSON_TYPE_SELECT = (By.XPATH, "//div[@id='personTypeId']//i[contains(@class, 'caret pull-right')]")
    PERSON_TYPE_TEXT = (By.XPATH, ".//*[@id='personTypeId']//span[@class='ng-binding ng-scope']")
    ALL_PERSON_TYPES_SELECT = (By.XPATH, "//a[@class='ui-select-choices-row-inner']//div[@class='ng-binding ng-scope']")
    PERSON_SURNAME_UKR_INPUT = (By.XPATH, "//input[@id='surname']")
    PERSON_SURNAME_ENG_INPUT = (By.XPATH, "//input[@id='surnameEng']")
    PERSON_FARTHER_NAME_UKR_INPUT = (By.XPATH, "//input[@id='fatherName']")
    PERSON_FIRST_NAME_UKR_INPUT = (By.XPATH, "//input[@id='firstName']")
    PERSON_FIRST_NAME_ENG_INPUT = (By.XPATH, "//input[@id='firstNameEng']")
    PERSON_SURNAME_UKR_INPUT_INCORRECT = (By.XPATH, "//input[@id='surname'][contains (@class, 'ng-invalid-pattern')]")
    PERSON_SURNAME_ENG_INPUT_INCORRECT = \
        (By.XPATH, "//input[@id='surnameEng'][contains (@class, 'ng-invalid-pattern')]")
    PERSON_FARTHER_NAME_UKR_INPUT_INCORRECT = \
        (By.XPATH, "//input[@id='fatherName'][contains (@class, 'ng-invalid-pattern')]")
    PERSON_FIRST_NAME_UKR_INPUT_INCORRECT = \
        (By.XPATH, "//input[@id='firstName'][contains (@class, 'ng-invalid-pattern')]")
    PERSON_FIRST_NAME_ENG_INPUT_INCORRECT = \
        (By.XPATH, "//input[@id='firstNameEng'][contains (@class, 'ng-invalid-pattern')]")

    # overriding functions
    def is_this_page(self):
        return self.is_element_visible(self.PERSON_TYPE_SELECT)

    # web elements

    # web element's functions

    # general functions

    # old

    def person_surname_ukr_input(self):
        return self.is_element_visible(self.PERSON_SURNAME_UKR_INPUT)

    def person_surname_eng_input(self):
        return self.is_element_visible(self.PERSON_SURNAME_ENG_INPUT)

    def person_farther_name_ukr_input(self):
        return self.is_element_visible(self.PERSON_FARTHER_NAME_UKR_INPUT)

    def person_first_name_ukr_input(self):
        return self.is_element_visible(self.PERSON_FIRST_NAME_UKR_INPUT)

    def person_first_name_eng_input(self):
        return self.is_element_visible(self.PERSON_FIRST_NAME_ENG_INPUT)

    @property
    def person_surname_ukr_input_incorrect(self):
        return self.is_element_visible(self.PERSON_SURNAME_UKR_INPUT_INCORRECT)

    @property
    def person_surname_eng_input_incorrect(self):
        return self.is_element_visible(self.PERSON_SURNAME_ENG_INPUT_INCORRECT)

    @property
    def person_father_name_input_incorrect(self):
        return self.is_element_visible(self.PERSON_FARTHER_NAME_UKR_INPUT_INCORRECT)

    @property
    def person_first_name_ukr_input_incorrect(self):
        return self.is_element_visible(self.PERSON_FIRST_NAME_UKR_INPUT_INCORRECT)

    @property
    def person_first_name_eng_input_incorrect(self):
        return self.is_element_visible(self.PERSON_FIRST_NAME_ENG_INPUT_INCORRECT)

    def person_type_select_click(self):
        """
        Method performs clicking on person type select field
        :return:
        """
        self.is_element_present(self.PERSON_TYPE_SELECT)
        self.driver.find_element(*self.PERSON_TYPE_SELECT).click()

    def person_type_text(self):
        """
        Method get text from person type select field
        :return:
        """
        self.is_element_present(self.PERSON_TYPE_TEXT)
        return self.driver.find_element(*self.PERSON_TYPE_TEXT)

    def choose_person_type(self, person_type):
        """
        Method performs choosing concrete person type
        :param person_type: if person_type exists in select menu,
                then method will click on it, else will leave default value
        :return:
        """
        self.is_element_present(self.ALL_PERSON_TYPES_SELECT)
        self.find_element_in_select(self.driver.find_elements(*self.ALL_PERSON_TYPES_SELECT), person_type).click()

    def set_first_ukr_name(self, first_ukr_name):
        """
        Method sets the first person name on Ukrainian language
        :param first_ukr_name: first person name on Ukrainian language
        :return:
        """
        self.is_element_present(self.PERSON_FIRST_NAME_UKR_INPUT)
        self.emulation_of_input(self.PERSON_FIRST_NAME_UKR_INPUT, first_ukr_name)

    def set_ukr_surname(self, ukr_surname):
        """
        Method sets the persons surname on Ukranian language
        :param ukr_surname: persons surname on Ukranian language
        :return:
        """
        self.emulation_of_input(self.PERSON_SURNAME_UKR_INPUT, ukr_surname)

    def set_father_ukr_name(self, father_ukr_name):
        """
        Method sets the fathers person name on Ukranian language
        :param father_ukr_name: fathers person name on Ukranian language
        :return:
        """
        self.emulation_of_input(self.PERSON_FARTHER_NAME_UKR_INPUT, father_ukr_name)

    def set_eng_surname(self, eng_surname):
        """
        Method sets the persons surname on English language
        :param ukr_surname: persons surname on English language
        :return:
        """
        self.emulation_of_input(self.PERSON_SURNAME_ENG_INPUT, eng_surname)

    def set_first_eng_name(self, first_eng_name):
        """
        Method sets the first person name on English language
        :param first_eng_name: first person name on English language
        :return:
        """
        self.emulation_of_input(self.PERSON_FIRST_NAME_ENG_INPUT, first_eng_name)

    def fill_in_main_person_page(self, person):
        """
        Method fill in data on the main persons page
        :param person: persons model in Person format
        :return:
        """
        self.is_this_page()
        self.person_type_select_click()
        self.choose_person_type(person.person_type)
        self.set_ukr_surname(person.surname_ukr)
        self.set_first_ukr_name(person.first_name_ukr)
        self.set_father_ukr_name(person.second_name_ukr)
        self.set_eng_surname(person.surname_eng)
        self.set_first_eng_name(person.first_name_eng)

    def read_in_main_person_page(self, person_new):
        """
        Method read the data on the main persons page
        :param person_new: is persons model in Person format
        :return: person_new
        """
        self.is_this_page
        common_methods = CommonMethods(self.driver)
        person_new.person_type = self.person_type_text().text
        person_new.surname_ukr = common_methods.get_value_from_text_field(self.driver.find_element(*self.PERSON_SURNAME_UKR_INPUT))
        person_new.first_name_ukr = common_methods.get_value_from_text_field(self.driver.find_element(*self.PERSON_FIRST_NAME_UKR_INPUT))
        person_new.second_name_ukr = common_methods.get_value_from_text_field(self.driver.find_element(*self.PERSON_FARTHER_NAME_UKR_INPUT))
        person_new.surname_eng = common_methods.get_value_from_text_field(self.driver.find_element(*self.PERSON_SURNAME_ENG_INPUT))
        person_new.first_name_eng = common_methods.get_value_from_text_field(self.driver.find_element(*self.PERSON_FIRST_NAME_ENG_INPUT))
        return person_new
