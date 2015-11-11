# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pages.internal_page import InternalPage
from utils.fill_enrollment import FillEnrollment
from utils.web_elem_utils import checkbox_set_state

__author__ = 'Stako'


class EnrollmentsMainPage(InternalPage):
    TEXT_CORRECT_PAGE_ENROLLMENT_ADD = (By.XPATH, "//h2[@class='content-header-title top-buffer bottom-buffer']")
    OK_FOR_INPUT_FIELD = (By.CSS_SELECTOR, "div[class='input-group'] * button[class='btn btn-primary']")
    SEARCH_NAME_FIELD = (By.XPATH, "//div[@class='modal-body ng-scope']//input[contains (@type, 'search')]")
    FIRST_PERSON = (By.XPATH, "//*[@class='table-responsive']//tbody[@class='pointer']//tr[1]/td[2]")
    PERSON_FIO_ALREADY_ADDED_VIEW = (By.XPATH, "//div[@search='personSearch']//table[@class='table table-bordered table-hover ']/tbody/tr[1]/td[2]")
    SERIES_OF_STATEMENTS = (By.ID, "inputDocSeries")
    NUMBER_STATEMENTS = (By.ID, "inputdocNum")
    NUMBER_WRONG_STATMENTS = (By.XPATH, "//input[contains(@class, 'ng-invalid-pattern')]")
    NUMBER_RIGHT_STATMENTS = (By.XPATH, "//input[contains(@class, 'ng-valid-pattern')]")
    CHECKBOX_IS_STATE = (By.XPATH, ".//input[@ng-model='enrolment.isState']")
    CHECKBOX_IS_CONTRACT = (By.XPATH, ".//input[@ng-model='enrolment.isContract']")
    CHECKBOX_IS_PRIVILEGE = (By.XPATH, ".//input[@ng-model='enrolment.isPrivilege']")
    RADIOBUTTON_DONT_GETTING_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='0']")
    RADIOBUTTON_GETTING_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='1']")
    RADIOBUTTON_IS_EDUCATION = (By.CSS_SELECTOR, "input[name='isedustate'][value='11']")
    RADIOBUTTON_NOT_PASSED_INTERVIEW = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='-1']")
    RADIOBUTTON_DONT_NEED_INTERVIEW = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='0']")
    RADIOBUTTON_NEED_INTERVIEW = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='1']")
    RADIOBUTTON_INTERVIEW_PASSED = (By.CSS_SELECTOR, "input[ng-model='enrolment.isInterview'][value='11']")
    CHECKBOX_IS_HOSTEL = (By.XPATH, ".//*[@ng-init='enrolment.isHostel = 0']")
    SEARCH_OFFERS_FIELD = (By.XPATH, "//*[@ng-model='searchBy.departmentId']//*[@class='caret pull-right']")
    CHOOSE_FORM_OF_EDUCATION = (By.XPATH, "//*[@ng-model='searchBy.specOfferTypeId']//*[@class='caret pull-right']")
    LIST_FROM_UI_SELECT = (By.XPATH, "//div[contains(@id, 'ui-select-choices-row')]/a/div")
    BUTTON_CHOOSE_SPECIALTIES = (By.CSS_SELECTOR, "button[class='btn btn-primary'] >i")
    CHOOSE_FIRST_SPECIALTIES = (By.XPATH, "//div[@class='table-responsive']//tbody[@class='pointer']/tr[1]/td[2]")
    FIRST_SPECIALTIES_ID = (By.XPATH, "//div[@class='table-responsive']//tbody[@class='pointer']/tr[1]/td[1]")
    FIRST_SPECIALTIES_ID_IN_VIEW_TABLE = (By.XPATH, "//div[@ng-model='enrolment.specOfferId']//tbody[@class='pointer']/tr[1]//td[1]")
    FIRST_SPECIALTIES_FIO_IN_VIEW_TABLE = (By.XPATH, "//div[@ng-model='enrolment.specOfferId']//tbody[@class='pointer']/tr[1]//td[2]")
    BUTTON_CLOSE_CHOOSE_OFFER = (By.XPATH, "//button[@class='close']")
    COUNT_SPECIALISTS = (By.XPATH, "//div[@class='table-responsive']//tbody[@class='pointer']/tr")
    DOCUMENT = (By.XPATH, ".//*[@class='col-xs-5']/*[@id='inputStructure']//i[@class='caret pull-right']")
    DOCUMENT_TITLE = (By.XPATH, "//*[@class='col-xs-5']/*[@id='inputStructure']//span[@class='ng-binding ng-scope']")
    TOTAL_SCORE = (By.ID, "inputMark")
    GRADING_SCALE = (By.XPATH, ".//*[@id='markScale']//i[@class='caret pull-right']")
    TEXT_FROM_GRADING_SCALE = (By.XPATH, ".//*[@id='markScale']//span[@class='ng-binding ng-scope']")
    CHECKBOX_DOCUMENT_IS_ORIGINAL = (By.XPATH, ".//*[@ng-init='enrolment.isOriginal = 0']")
    PRIORITY = (By.ID, "inputPriority")
    PRIORITY_WRONG_UP   = (By.XPATH, "//input[contains(@class, 'ng-invalid-max')]")
    PRIORITY_WRONG_DOWN   = (By.XPATH, "//input[contains(@class, 'ng-invalid-min')]")
    PRIORITY_RIGHT   = (By.XPATH, "//input[contains(@class, 'ng-valid')]")
    STRUCTURAL_UNIT = (By.XPATH, ".//*[@class='col-xs-3']/*[@id='inputStructure']//i[@class='caret pull-right']")
    STRUCTURAL_UNIT_TEXT = (By.XPATH, ".//*[@class='col-xs-3']/*[@id='inputStructure']//span[@class='ng-binding ng-scope']")
    DATE_OF_CREATION_STATEMENTS = (By.ID, "evDate")
    DATE_OF_ENTRY_STATEMENTS = (By.ID, "begDate")
    DATE_CLOSING_STATEMENTS = (By.ID, "endDate")
    BUTTON_SAVE = (By.XPATH, ".//*[@class='btn btn-primary'][@ng-click='sendToServer()']")
    ID_DETAILING_START_MENU = (By.ID, "inputEnrolmentTypeId")
    ID_TYPE_OF_ENTRY_MENU = (By.ID, "inputChiefEnrolTypes")
    SEARCH_PERSON_BY_SELECT = (By.XPATH, "//select[@ng-model='fieldSearchBy']")
    SEARCH_PERSON_BY_INPUT = (By.XPATH, "//input[@ng-model='querySearchBy']")
    ALL_FOUND_PERSONS_PIB = (By.XPATH, "//div[@search='personSearch']//tbody[@class='pointer']//tr//td[2]")
    ALL_FOUND_PERSONS_ID = (By.XPATH, "//div[@search='personSearch']//tbody[@class='pointer']//tr//td[1]")
    CANCEL_BUTTON = (By.XPATH, "//div[@class='modal-footer ng-scope']//button[@ng-click='cancel()']")
    IS_ENROLLMENT_IN_PERSON = (By.XPATH, "//div[@search='personSearch']//*[@class='pointer']/tr/td[1]")

    # overriding functions
    def is_this_page(self):
        return self.is_element_visible(self.SEARCH_PERSON_BY_SELECT)

    # web elements
    @property
    def checkbox_is_state(self):
        return self.driver.find_element(*self.CHECKBOX_IS_STATE)

    @property
    def checkbox_is_contract(self):
        return self.driver.find_element(*self.CHECKBOX_IS_CONTRACT)

    @property
    def checkbox_is_privilege(self):
        return self.driver.find_element(*self.CHECKBOX_IS_PRIVILEGE)

    @property
    def checkbox_is_hostel(self):
        return self.driver.find_element(*self.CHECKBOX_IS_HOSTEL)

    @property
    def checkbox_document_is_original(self):
        return self.driver.find_element(*self.CHECKBOX_DOCUMENT_IS_ORIGINAL)

    @property
    def cancel_button(self):
        return self.driver.find_element(*self.CANCEL_BUTTON).click()

    @property
    def is_enrollment_in_person(self):
        return self.is_element_visible(self.IS_ENROLLMENT_IN_PERSON)

    @property
    def search_offers_field(self):
        return self.is_element_visible(self.SEARCH_OFFERS_FIELD)

    @property
    def choose_first_specialties(self):
        return self.is_element_visible(self.CHOOSE_FIRST_SPECIALTIES)

    @property
    def button_close_choose_offer(self):
        return self.is_element_visible(self.BUTTON_CLOSE_CHOOSE_OFFER)

    @property
    def search_name_field(self):
        return self.is_element_visible(self.SEARCH_NAME_FIELD)

    @property
    def radiobutton_getting_education(self):
        return self.is_element_visible(self.RADIOBUTTON_GETTING_EDUCATION)

    @property
    def radiobutton_dont_getting_education(self):
        return self.is_element_visible(self.RADIOBUTTON_DONT_GETTING_EDUCATION)

    @property
    def radiobutton_is_education(self):
        return self.is_element_visible(self.RADIOBUTTON_IS_EDUCATION)

    @property
    def radiobutton_not_passed_interview(self):
        return self.is_element_visible(self.RADIOBUTTON_NOT_PASSED_INTERVIEW)

    @property
    def radiobutton_dont_need_interview(self):
        return self.is_element_visible(self.RADIOBUTTON_DONT_NEED_INTERVIEW)

    @property
    def radiobutton_need_interview(self):
        return self.is_element_visible(self.RADIOBUTTON_NEED_INTERVIEW)

    @property
    def radiobutton_interview_passed(self):
        return self.is_element_visible(self.RADIOBUTTON_INTERVIEW_PASSED)

    @property
    def button_choose_specialties(self):
        return self.is_element_visible(self.BUTTON_CHOOSE_SPECIALTIES)

    @property
    def document(self):
        return self.is_element_visible(self.DOCUMENT)

    @property
    def total_score(self):
        return self.is_element_visible(self.TOTAL_SCORE)

    @property
    def grading_scale(self):
        return self.is_element_visible(self.GRADING_SCALE)

    @property
    def priority(self):
        return self.is_element_visible(self.PRIORITY)

    @property
    def choose_form_of_education(self):
        return self.is_element_visible(self.CHOOSE_FORM_OF_EDUCATION)

    @property
    def first_person(self):
        return self.is_element_visible(self.FIRST_PERSON)

    @property
    def ok_for_input_field(self):
        return self.driver.find_element(*self.OK_FOR_INPUT_FIELD)

    @property
    def certain_negative_number_statements(self):
        return self.is_element_visible(self.NUMBER_WRONG_STATMENTS)

    @property
    def certain_positive_number_statements(self):
        return self.is_element_visible(self.NUMBER_RIGHT_STATMENTS)

    @property
    def number_statements(self):
        return self.is_element_present(self.NUMBER_STATEMENTS)

    @property
    def structural_unit(self):
        return self.is_element_visible(self.STRUCTURAL_UNIT)

    @property
    def button_save(self):
        return self.driver.find_element(*self.BUTTON_SAVE)


    # web element's functions
    def button_save_click(self):
        self.button_save.click()
        self.wait_until_page_generate()

    def set_state_status(self, boolean):
        checkbox_set_state(self.checkbox_is_state, boolean)

    def set_contract_status(self, boolean):
        checkbox_set_state(self.checkbox_is_contract, boolean)

    def set_privilege_status(self, boolean):
        checkbox_set_state(self.checkbox_is_privilege, boolean)

    def set_hostel_status(self, boolean):
        checkbox_set_state(self.checkbox_is_hostel, boolean)

    def set_document_original_status(self, is_outlander):
        checkbox_set_state(self.checkbox_document_is_original, is_outlander)

    def list_form_ui_select(self):
        self.is_element_visible(self.LIST_FROM_UI_SELECT)
        return self.driver.find_elements(*self.LIST_FROM_UI_SELECT)

    def ok_for_input_field_click(self):
        self.is_element_visible(self.OK_FOR_INPUT_FIELD).click()
        self.wait_until_page_generate()

    def cancel_click(self):
        self.cancel_button.click()
        self.wait_until_page_generate()

    def find_first_specialities_id(self):
        return self.driver.find_element(*self.FIRST_SPECIALTIES_ID)

    def find_first_specialities_id_in_view_table(self):
        return self.driver.find_element(*self.FIRST_SPECIALTIES_ID_IN_VIEW_TABLE)

    def find_first_specialities_fio_in_view_table(self):
        return self.driver.find_elements(*self.FIRST_SPECIALTIES_FIO_IN_VIEW_TABLE)[1]

    def person_fio_already_added_view(self):
        return self.driver.find_element(*self.PERSON_FIO_ALREADY_ADDED_VIEW)

    def search_person_by(self, index):
        self.wait_until_page_generate()
        Select(self.driver.find_element(*self.SEARCH_PERSON_BY_SELECT)).select_by_index(index)

    def get_all_found_persons_pib(self):
        """
        Method find all elements with persons PIB
        :return: list of elements with persons PIB
        """
        return self.driver.find_elements(*self.ALL_FOUND_PERSONS_PIB)

    def get_all_found_persons_id(self):
        """
        Method find all elements with persons ID
        :return: list of elements with persons ID
        """
        return self.driver.find_elements(*self.ALL_FOUND_PERSONS_ID)

    def find_date_of_creation(self):
        """
        Method find date of creation input field
        :return: element of date of creation input field
        """
        self.is_element_visible(self.DATE_OF_CREATION_STATEMENTS)
        return self.driver.find_element(*self.DATE_OF_CREATION_STATEMENTS)

    def find_series_of_statements(self):
        self.is_element_visible(self.SERIES_OF_STATEMENTS)
        return self.driver.find_element(*self.SERIES_OF_STATEMENTS)

    def find_number_statements(self):
        self.is_element_visible(self.NUMBER_STATEMENTS)
        return self.driver.find_element(*self.NUMBER_STATEMENTS)

    def find_checkbox_is_state(self):
        self.is_element_visible(self.CHECKBOX_IS_STATE)
        return self.driver.find_element(*self.CHECKBOX_IS_STATE)

    def find_checkbox_is_contract(self):
        self.is_element_visible(self.CHECKBOX_IS_CONTRACT)
        return self.driver.find_element(*self.CHECKBOX_IS_CONTRACT)

    def find_checkbox_is_privilege(self):
        self.is_element_visible(self.CHECKBOX_IS_PRIVILEGE)
        return self.driver.find_element(*self.CHECKBOX_IS_PRIVILEGE)

    def find_checkbox_document_is_original(self):
        self.is_element_visible(self.CHECKBOX_DOCUMENT_IS_ORIGINAL)
        return self.driver.find_element(*self.CHECKBOX_DOCUMENT_IS_ORIGINAL)

    def find_radiobutton_getting_education(self):
        self.is_element_visible(self.RADIOBUTTON_GETTING_EDUCATION)
        return self.driver.find_element(*self.RADIOBUTTON_GETTING_EDUCATION)

    def find_radiobutton_is_education(self):
        self.is_element_visible(self.RADIOBUTTON_IS_EDUCATION)
        return self.driver.find_element(*self.RADIOBUTTON_IS_EDUCATION)

    def find_checkbox_is_hostel(self):
        self.is_element_visible(self.CHECKBOX_IS_HOSTEL)
        return self.driver.find_element(*self.CHECKBOX_IS_HOSTEL)

    def find_total_score(self):
        self.is_element_visible(self.TOTAL_SCORE)
        return self.driver.find_element(*self.TOTAL_SCORE)

    def find_grading_scale(self):
        self.is_element_visible(self.GRADING_SCALE)
        return self.driver.find_element(*self.GRADING_SCALE)

    def get_document_title(self):
        return self.driver.find_element(*self.DOCUMENT_TITLE)

    def get_structural_unit_text(self):
        return self.driver.find_element(*self.STRUCTURAL_UNIT_TEXT)

    def get_detailing_start_menu(self):
        return self.driver.find_element(*self.ID_DETAILING_START_MENU)

    def get_type_of_entry(self):
        return self.driver.find_element(*self.ID_TYPE_OF_ENTRY_MENU)

    def get_text_add_enrollment(self):
        return self.driver.find_element(*self.TEXT_CORRECT_PAGE_ENROLLMENT_ADD)

    def get_form_input_total_score(self):
        return self.driver.find_element(*self.TOTAL_SCORE)

    def get_priority(self):
        return self.driver.find_element(*self.PRIORITY)


    # general functions
    def set_search_person_by(self, searched_value):
        """
        Method sets the searched value
        :param searched_value: String parametr.
        :return:
        """
        self.emulation_of_input(self.SEARCH_PERSON_BY_INPUT, searched_value)

    # def click_all_checkbox(self, state, contract, privilege, hostel, document):
    #     """
    #     This method sets value in all checkbox.
    #     :param state: is value of checkbox "budget".
    #     :param contract: is value of checkbox "contract".
    #     :param privilege: is value of checkbox "privilege".
    #     :param hostel: is value of checkbox "need hostel".
    #     :param document: is value of checkbox "document is original".
    #     """
    #     self.set_state_status(state)
    #     self.set_contract_status(contract)
    #     self.set_privilege_status(privilege)
    #     self.set_hostel_status(hostel)
    #     self.set_document_original_status(document)

    def certain_number_statements(self, c_number_statements):
        try:
            val = int(c_number_statements)
            if val <= 0:
                raise ValueError
        except ValueError:
            return self.is_element_visible(self.NUMBER_WRONG_STATMENTS)
        else:
            return self.is_element_visible(self.NUMBER_RIGHT_STATMENTS)

    def certain_priority(self, c_priority):
        if 0 < c_priority < 16:
            return self.is_element_visible(self.PRIORITY_RIGHT)
        return self.is_element_visible(self.PRIORITY_WRONG_DOWN) or self.is_element_visible(self.PRIORITY_WRONG_UP)

    def clear_form_input_total_score(self):
        toClear = self.driver.find_element(*self.TOTAL_SCORE)
        toClear.send_keys(Keys.CONTROL + "a")
        toClear.send_keys(Keys.DELETE)


    def find_element_in_ui_select(self, elements, string):
        """
        This method looks for WebElement in ui-select by name.
        :param elements: is list of WebElements in ui-select.
        :param string: is name of elements.
        :return: looked for WebElement.
        """
        for el in elements:
            # if el.text.encode('utf8') == string:
            if el.text == string:
                return el

    def find_element_in_select(self, elements, string):
        """
        This method looks for options in select by name and click one.
        :param elements: is list of options in select.
        :param string: is name of elements.
        """
        for sel in elements:
            # if sel.text.encode('utf8') == string:
            if sel.text == string:
                sel.click()
                break

    def get_enrollment(self, json_file, name_of_dict):
        """
        This method return dictionary from json by name.
        :param json_file: is name of json file.
        :param name_of_dict: is name of dictionary in json file.
        :return: dictionary.
        """
        fill_enrollment = FillEnrollment()
        return fill_enrollment.create_enrollment_from_json(json_file, name_of_dict)

    def fill_enrollment(self, json_file, name_of_dictionary):
        """
        This method fill enrollment and save one.
        """
        enrollment = self.get_enrollment(json_file, name_of_dictionary)
        if not self.is_enrollment_in_person:
            self.add_person_in_enrollment(enrollment.person_name)
        self.emulation_of_input(self.SERIES_OF_STATEMENTS, enrollment.series_of_statements)
        self.emulation_of_input(self.NUMBER_STATEMENTS, enrollment.number_statements)
        checkbox_set_state(self.enrollments_main_page.find_checkbox_is_state(), enrollment.checkbox_is_state)
        checkbox_set_state(self.enrollments_main_page.find_checkbox_is_contract(), enrollment.checkbox_is_contract)
        checkbox_set_state(self.enrollments_main_page.find_checkbox_is_privilege(), enrollment.checkbox_is_privilege)
        checkbox_set_state(self.enrollments_main_page.find_checkbox_is_hostel(), enrollment.checkbox_is_hostel)
        checkbox_set_state(self.enrollments_main_page.find_checkbox_document_is_original(), enrollment.checkbox_document_is_original)
        self.radiobutton_higher_education(enrollment.radiobutton_higher_education)
        self.radiobutton_evaluation_of_the_interview(enrollment.radiobutton_evaluation_of_the_interview)
        self.search_offers(enrollment.offers, enrollment.form_of_education)
        self.choose_first_specialties.click()
        self.choose_document(enrollment.document)
        self.choose_grading_scale(enrollment.grading_scale)
        self.add_total_score(self.TOTAL_SCORE, enrollment.total_score)
        self.add_priority(self.PRIORITY, enrollment.priority)
        self.choose_structural_unit(enrollment.structural_unit)
        self.type_of_entry(enrollment.type_of_entry)
        self.specification_of_entry(enrollment.detailing_start)
        self.set_date(self.DATE_OF_ENTRY_STATEMENTS, enrollment.date_of_entry)
        self.set_date(self.DATE_CLOSING_STATEMENTS, enrollment.date_closing)
        self.wait_until_page_generate()
        self.button_save_click()
        return enrollment

    def add_person_in_enrollment(self, name):
        """
        This method adds person in enrollments.
        :param name: is name of person.
        """
        self.wait_until_page_generate()
        self.ok_for_input_field.click()
        self.wait_until_page_generate()
        self.emulation_of_input(self.SEARCH_NAME_FIELD, name)
        self.first_person.click()
        self.wait_until_page_generate()

    def radiobutton_higher_education(self, education):
        """
        This method is to select the radiobutton "Вища освіта" on its value.
        :param education: is value for radiobutton select.
        """
        if education == u"Не отримую освіти":
            self.radiobutton_dont_getting_education.click()
        elif education == u"Отримую освіту":
            self.radiobutton_getting_education.click()
        elif education == u"Є вища освіта":
            self.radiobutton_is_education.click()

    def radiobutton_evaluation_of_the_interview(self, evaluation):
        """
        This method is to select the radiobutton "Відмітка про співбесіду" on its value.
        :param evaluation: is value for radiobutton select.
        """
        if evaluation == u"Не пройшов співбесіду":
            self.radiobutton_not_passed_interview.click()
        elif evaluation == u"Не потрібно співбесіди":
            self.radiobutton_dont_need_interview.click()
        elif evaluation == u"Потрібна співбесіда":
            self.radiobutton_need_interview.click()
        elif evaluation == u"Співпебісда пройдена":
            self.radiobutton_interview_passed.click()

    def search_offers(self, offer, form_of_education):
        """
        This method searches and selects offers and form of education.
        :param offer: is offer what need to select.
        :param form_of_education: is form of education what need to select.
        """
        self.search_offers_field.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), offer).click()
        self.choose_form_of_education.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), form_of_education).click()
        self.button_choose_specialties.click()
        self.wait_until_page_generate()

    def choose_document(self, document):
        """
        This method selects the document in UI select by name.
        :param document: is name of document.
        """
        self.document.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), document).click()

    def choose_grading_scale(self, scale):
        """
        This method selects the grading scale in UI select by name.
        :param scale: is name of grading scale.
        """
        self.grading_scale.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), scale).click()


    def add_total_score(self, locator, score):
        """
        This method establishes a total score character by character.
        :param locator: is locator of field for total score.
        :param score: is value of total score.
        """
        self.emulation_of_input(locator, score)

    def add_priority(self, locator, priority):
        """
        This method establishes a priority character by character.
        :param locator: is locator of field for priority.
        :param priority: is value of priority.
        """
        self.emulation_of_input(locator, priority)

    def choose_structural_unit(self, unit):
        """
        This method selects the structural unit in UI select by name.
        :param unit: is name of structural unit.
        """
        self.structural_unit.click()
        self.find_element_in_ui_select(self.list_form_ui_select(), unit).click()

    def type_of_entry(self, type_of_entry):
        """
        This method selects the type of entry in select menu by name.
        :param type_of_entry: is name of entry type.
        """
        self.find_element_in_select(
            Select(self.driver.find_element(*self.ID_TYPE_OF_ENTRY_MENU)).options, type_of_entry)

    def specification_of_entry(self, specification):
        """
        This method selects the specification of entry in select menu by name.
        :param specification: is name of specification.
        """
        self.find_element_in_select(
            Select(self.driver.find_element(*self.ID_DETAILING_START_MENU)).options, specification)

    def select_person_by(self, index):
        """
        Method select searching type by index
        :param index: Searching type in Integer. 0 - by PIB, 1 - by surname, 2 - by person id, 3 - by documents number
        :return:
        """
        self.wait_until_page_generate()
        Select(self.driver.find_element(*self.SEARCH_PERSON_BY_SELECT)).select_by_index(index)

    def set_begin_date(self, date):
        """
        Method sets date in the date of beginning input field
        :return: element of date of creation input field
        """
        self.set_date(self.DATE_OF_ENTRY_STATEMENTS, date)

    def set_end_date(self, date):
        """
        Method sets date in the date of closing input field
        :return: element of date of closing input field
        """
        self.set_date(self.DATE_CLOSING_STATEMENTS, date)

    def find_date_of_begining(self):
        """
        Method find date of beginning input field
        :return: element of date of beginning input field
        """
        self.is_element_visible(self.DATE_OF_ENTRY_STATEMENTS)
        return self.driver.find_element(*self.DATE_OF_ENTRY_STATEMENTS)

    def find_date_of_ending(self):
        """
        Method find date of closing input field
        :return: element of date of closing input field
        """
        self.is_element_visible(self.DATE_CLOSING_STATEMENTS)
        return self.driver.find_element(*self.DATE_CLOSING_STATEMENTS)

    def get_arr_structural_subdivision_from_choose_offer(self):
        count_specialists = len(self.driver.find_elements(*self.COUNT_SPECIALISTS))
        structural_subdivisions = []
        for number in range(count_specialists):
            locator = self.__get_structural_subdivision_specialist_by_number_in_table(number)
            structural_subdivisions.append(self.driver.find_element(*locator).text)
        return structural_subdivisions

    def get_arr_type_offer_from_choose_offer(self):
        count_specialists = len(self.driver.find_elements(*self.COUNT_SPECIALISTS))
        type_offers = []
        for number in range(count_specialists):
            locator = self.__get_type_offer_specialist_by_number_in_table(number)
            type_offers.append(self.driver.find_element(*locator).text)
        return type_offers

    def __get_structural_subdivision_specialist_by_number_in_table(self, number):
        return (By.XPATH, "//div[@class='table-responsive']//tbody[@class='pointer']/tr[" + str(number + 1) + "]/td[4]")

    def __get_type_offer_specialist_by_number_in_table(self, number):
        return (By.XPATH, "//div[@class='table-responsive']//tbody[@class='pointer']/tr[" + str(number + 1) + "]/td[6]")

    def get_atrribute_of_element_by(self, element, value):
        return element.get_attribute(value)

    def get_text_choose_grading_scale(self):
        return self.driver.find_element(*self.TEXT_FROM_GRADING_SCALE)

