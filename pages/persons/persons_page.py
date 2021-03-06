# coding: utf8
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


from decorators.error_handling_dec import ErrorHandlerPO
from pages.internal_page import InternalPage


class PersonsPage(InternalPage):
    #
    # TO SEARCH
    #
    MODAL_HEADER_CHOOSER = (By.XPATH,"//div[@id='modalHeaderChooser']")
    ADD_PERSON_BUTTON = (By.XPATH, "//button[contains(@class,'btn-success')]")
    CHOOSE_SURNAME_SEARCH = (By.XPATH, "//div[@class='col-sm-12']//option[@value='0']")
    CHOOSE_PERSON_ID_SEARCH = (By.XPATH, "//div[@class='col-sm-12']//option[@value='1']")
    CHOOSE_NUM_OS_SEARCH = (By.XPATH, "//div[@class='col-sm-12']//option[@value='2']")
    CHOOSE_SERIES_OS_SEARCH = (By.XPATH, "//div[@class='col-sm-12']//option[@value='3']")
    INPUT_GROUP_SEARCH_BUTTON = (By.XPATH, "//div[@class='input-group']/input")
    OK_GROUP_SEARCH_BUTTON = (By.XPATH, "//div[@class='input-group']/span/button")
    # in table
    SEARCHED_SURNAME = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[2]")
    SEARCHED_PERSON_ID = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[1]")
    PERSON_ID_FOR_SEARCH = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][2]/td[1]")
    SEARCHED_NUM_OS = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[11]")
    SEARCHED_SERIES_OS = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[10]")
    ROWS_IN_RABLE = (By.XPATH, "//tbody[@class='pointer']/tr")
    #
    # TO FILTER
    #
    BURGER_BUTTON = (By.XPATH, "//button[@class='field-chooser-button pull-right btn btn-primary']")
    ADD_TO_TABLE_MILITARY_CHECKBOX = (By.XPATH, "//li[15]/label/input[@id='showHideHeader']")
    ADD_TO_TABLE_RESIDENT_CHECKBOX = (By.XPATH, "//li[12]/label/input[@id='showHideHeader']")
    CLOSE_AFTER_ADDITION_BUTTON = (By.XPATH, "//div[@class='modal-footer']/button[@class='btn btn-danger']")

    REFRESH_UPPER_BUTTON = (
        By.XPATH, "//p[1]/*[contains(@class, 'personFilterUpdateButton')]")
    REFRESH_BOTTOM_BUTTON = (
        By.XPATH, "//p[2]/*[contains(@class, 'personFilterUpdateButton')]")
    GENDER_MALE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[1]/label/input")
    GENDER_FEMALE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[2]/label/input")
    GENDER_NOT_DEFINED_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_APPLICANT_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[1]/label/input")
    TYPE_STUDENT_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[2]/label/input")
    TYPE_SCIENTIST_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_EMPLOYEE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[4]/label/input")
    TYPE_GRADUATE_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[5]/label/input")
    TYPE_OUTSIDER_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[6]/label/input")
    NEED_HOSTEL_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[1]/label/input")
    DONT_NEED_HOSTEL_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[2]/label/input")
    BOUND_TO_MILITARY_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[1]/label/input")
    NOT_BOUND_TO_MILITARY_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[2]/label/input")
    RESIDENT_FOREIGNER_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[1]/label/input")
    RESIDENT_NOT_FOREIGNER_CHECKBOX = (
        By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[2]/label/input")
    # in table
    # the 1 value
    FILTERED_GENDER = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[7]")
    FILTERED_TYPE = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[6]")
    FILTERED_NEED_OF_HOSTEL = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[16]")
    FILTERED_BOUND_TO_MILITARY = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[15]")
    FILTERED_RESIDENT = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[12]")

    FILTERED_TYPE_COLUMN = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[6]")
    FILTERED_GENDER_COLUMN = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[7]")
    FILTERED_HOSTEL_COLUMN = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[16]")
    FILTERED_MILITARY_COLUMN = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[15]")
    FILTERED_RESIDENT_COLUMN = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope']/td[12]")

    RID_OUT_OF_FILTER_BUTTON = (By.XPATH, "//div[@class='col-md-2 col-lg-2 filter']//button[@class='close']")

    TO_NEXT_TABLE_PAGE_BUTTON = (By.XPATH, "//ul[@class='pagination']/li[8]/span")

    ADD_PERSON_BUTTON = (By.XPATH, "//a[@ui-sref='root.person.new.main']")
    SHOW_HIDE_FILTERS_BUTTON = (By.XPATH, "//button[contains(@ng-click,'hideFilterFunc')]")
    ACTIVE_ITEMS_PER_PAGE_BUTTON = (By.XPATH, "//button[contains(@class, 'active')]")
    PREVIOUS_PAGE = (By.XPATH, "//li[contains(@title, 'Previous Page')]")
    LAST_NUMBERED_PAGE = (By.XPATH, "//li[contains(@title, 'Last Page')]/preceding-sibling::li[2]/span")
    LAST_PAGE = (By.XPATH, "//li/span[contains(.,'>>')]")
    FIELD_CHOOSER_BUTTON = (By.XPATH, "//button[contains(@class, 'field-chooser-button')]")
    FIELD_CHOOSER_RED_CLOSE_BUTTON = (By.XPATH, "//button[parent::div[contains(@class, 'modal-footer')]]")
    INACTIVE_COLUMNS_MODAL = (By.XPATH, "//ul[@class='list-group']/li/label/input[not(@checked)]")
    # Columns dictionary binding number of column to it's name
    DELETE_FIRST_PERSON_IN_TABLE = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[18]//button[3]")
    VIEW_FIRST_PERSON_IN_TABLE = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[18]//button[2]")
    EDIT_FIRST_PERSON_IN_TABLE = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[18]//button[1]")

    COLUMN_NUMBER_ADD = (By.XPATH, "//li[1]//*[@id='showHideHeader']")
    COLUMN_FIO_ADD = (By.XPATH, "//li[2]//*[@id='showHideHeader']")
    COLUMN_NAME_ADD = (By.XPATH, "//li[3]//*[@id='showHideHeader']")
    COLUMN_FATHER_NAME_ADD = (By.XPATH, "//li[4]//*[@id='showHideHeader']")
    COLUMN_SURNAME_ADD = (By.XPATH, "//li[5]//*[@id='showHideHeader']")
    COLUMN_PERSON_TYPE_ADD = (By.XPATH, "//li[6]//*[@id='showHideHeader']")
    COLUMN_SEX_ADD = (By.XPATH, "//li[7]//*[@id='showHideHeader']")
    COLUMN_MARITAL_STATUS_ADD = (By.XPATH, "//li[8]//*[@id='showHideHeader']")
    COLUMN_CITIZENSHIP_ADD = (By.XPATH, "//li[9]//*[@id='showHideHeader']")
    COLUMN_PB_SERIES_ADD = (By.XPATH, "//li[10]//*[@id='showHideHeader']")
    COLUMN_PB_NUMBER_ADD = (By.XPATH, "//li[11]//*[@id='showHideHeader']")
    COLUMN_RESIDENT_ADD = (By.XPATH, "//li[12]//*[@id='showHideHeader']")
    COLUMN_PLACE_OF_BIRTH_ADD = (By.XPATH, "//li[13]//*[@id='showHideHeader']")
    COLUMN_DATE_OF_BIRTH_ADD = (By.XPATH, "//li[14]//*[@id='showHideHeader']")
    COLUMN_VZ_ADD = (By.XPATH, "//li[15]//*[@id='showHideHeader']")
    COLUMN_HOSTEL_ADD = (By.XPATH, "//li[16]//*[@id='showHideHeader']")
    COLUMN_MATERIAL_LIABILITY_ADD = (By.XPATH, "//li[17]//*[@id='showHideHeader']")
    ID_OF_PERSON_IN_FIRST_ROW = (By.XPATH, "//*[@class='pointer']/tr[1]/td[1]")

    COLUMNS_DICT = {
        1: '№',
        2: 'ПІБ',
        3: 'Ім’я',
        4: 'По-батькові',
        5: 'Прізвище',
        6: 'Тип персони',
        7: 'Стать',
        8: 'Сімейний стан',
        9: 'Громад-во',
        10: 'Серія ОС',
        11: 'Номер ОС',
        12: 'Резидент',
        13: 'Місце народж.',
        14: 'Дата народж.',
        15: 'ВЗ',
        16: 'Гуртожиток',
        17: 'Мат. відп'
    }
    #
    # !!! Important
    #
    # To get selectors on table headers (sorting after click on it)
    # or modal window column selection (which columns display)
    # use methods get_table_selector(N) and get_modal_selector(N)
    # where N is the key of COLUMN_DICT

    def get_modal_selector(self, column_number):
        return By.XPATH, "//span[contains(., '" + PersonsPage.COLUMNS_DICT.get(column_number) + "')]"

    def get_table_selector(self, column_number):
        return By.XPATH, "//a[contains(., '" + PersonsPage.COLUMNS_DICT.get(column_number) + "')]"

    #
    # END OF SELECTORS SECTION
    #

    @ErrorHandlerPO("current page is not Persons page")
    def is_current_page(self):
        return self.wait.until(visibility_of_element_located(self.ADD_PERSON_BUTTON))

    def id_of_person_in_first_row(self):
        return self.driver.find_element(*self.ID_OF_PERSON_IN_FIRST_ROW)


    def is_this_page(self):
        self.is_element_visible(self.ADD_PERSON_BUTTON)
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def rows_in_body(self):
        return self.driver.find_elements(*self.ROWS_IN_RABLE)

    @property
    def add_person_link(self):
        return self.driver.find_element(*self.ADD_PERSON_BUTTON).click()

    @property
    def delete_first_person_in_page(self):
        if self.is_element_visible(self.DELETE_FIRST_PERSON_IN_TABLE):
            self.driver.find_element(*self.DELETE_FIRST_PERSON_IN_TABLE).click()
            self.wait_until_page_generate()

    @property
    def view_first_person_in_page(self):
        if self.is_element_visible(self.VIEW_FIRST_PERSON_IN_TABLE):
            self.driver.find_element(*self.VIEW_FIRST_PERSON_IN_TABLE).click()
            self.wait_until_page_generate()

    @property
    def edit_first_person_in_page(self):
        self.is_element_visible(self.EDIT_FIRST_PERSON_IN_TABLE)
        return self.driver.find_element(*self.EDIT_FIRST_PERSON_IN_TABLE)

    def searching_person_by_surname(self, given_surname):
        """
        Method needs for "test_add_person". It checks that the added person doesn't exist in the system.
        :param given_surname: String parameter. Added persons surname.
        :return:
        """
        self.wait_until_page_generate()
        if len(self.rows_in_body) == 0:
            return None
        if self.is_element_present(self.SEARCHED_SURNAME):
            elem = self.driver.find_element(*self.SEARCHED_SURNAME)
            if elem.text.__contains__(given_surname):
                return elem
        else:
            return None

    # FILTER
    # to all filters
    @ErrorHandlerPO(message='in person page last page ref is not found')
    def try_get_last_page_ref(self):
        return self.try_get_visible_element(self.LAST_PAGE)

    @ErrorHandlerPO(message='Red button is not found in field chooser')
    def try_field_chooser_red_close_button(self):
        return self.driver.find_element(*self.FIELD_CHOOSER_RED_CLOSE_BUTTON)

    def try_get_refresh_upper_button(self):
        return self.is_element_visible(self.REFRESH_UPPER_BUTTON)

    def try_get_refresh_bottom_button(self):
        return self.is_element_visible(self.REFRESH_BOTTOM_BUTTON)

    def try_get_burger_button(self):
        return self.is_element_visible(self.BURGER_BUTTON)

    def try_get_add_to_table_military_checkbox(self):
        return self.is_element_visible(self.ADD_TO_TABLE_MILITARY_CHECKBOX)

    def try_get_add_to_table_resident_checkbox(self):
        return self.is_element_visible(self.ADD_TO_TABLE_RESIDENT_CHECKBOX)

    def try_get_close_after_addition_button(self):
        return self.is_element_visible(self.CLOSE_AFTER_ADDITION_BUTTON)

    def try_get_close_filter(self):
        return self.is_element_visible(self.RID_OUT_OF_FILTER_BUTTON)

    # gender (male, female, not defined)
    def try_get_gender_male_checkbox(self):
        return self.is_element_visible(self.GENDER_MALE_CHECKBOX)

    def try_get_gender_female_checkbox(self):
        return self.is_element_visible(self.GENDER_FEMALE_CHECKBOX)

    def try_get_gender_not_defined_checkbox(self):
        return self.is_element_visible(self.GENDER_NOT_DEFINED_CHECKBOX)

    # FILTERED
    def try_get_filtered_gender(self, given_person_gender):
        self.wait.until(EC.text_to_be_present_in_element(self.FILTERED_GENDER, given_person_gender))
        return self.driver.find_element(*self.FILTERED_GENDER)

    def try_get_filtered_gender_column(self, given_person_gender):

        cells_texts = []

        for i in range(1, len(self.FILTERED_GENDER_COLUMN), 1):
            cell_path = "//tbody[@class='pointer']/tr[@class='ng-scope'][%d]/td[7]" % i
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, cell_path), given_person_gender))
            cells_texts.append((self.driver.find_element(*(By.XPATH, cell_path))).text)

        return cells_texts

    # type (applicant, student, scientist, employee, graduate, outsider)
    def try_get_type_applicant_checkbox(self):
        return self.is_element_visible(self.TYPE_APPLICANT_CHECKBOX)

    def try_get_type_student_checkbox(self):
        return self.is_element_visible(self.TYPE_STUDENT_CHECKBOX)

    def try_get_type_scientist_checkbox(self):
        return self.is_element_visible(self.TYPE_SCIENTIST_CHECKBOX)

    def try_get_type_employee_checkbox(self):
        return self.is_element_visible(self.TYPE_EMPLOYEE_CHECKBOX)

    def try_get_type_graduate_checkbox(self):
        return self.is_element_visible(self.TYPE_GRADUATE_CHECKBOX)

    def try_get_type_outsider_checkbox(self):
        return self.is_element_visible(self.TYPE_OUTSIDER_CHECKBOX)

    # FILTERED
    def try_get_one_filtered_type(self, given_person_type):
        self.wait.until(EC.text_to_be_present_in_element(self.FILTERED_TYPE, given_person_type))
        return self.driver.find_element(*self.FILTERED_TYPE)

    def try_get_filtered_type_column(self, given_person_type):

        cells_texts = []

        for i in range(1, len(self.FILTERED_TYPE_COLUMN), 1):
            cell_path = "//tbody[@class='pointer']/tr[@class='ng-scope'][%d]/td[6]" % i
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, cell_path), given_person_type))
            cells_texts.append((self.driver.find_element(*(By.XPATH, cell_path))).text)

        return cells_texts

    # need for hostel (need, doesn`t need)
    def try_get_need_hostel_checkbox(self):
        return self.is_element_visible(self.NEED_HOSTEL_CHECKBOX)

    def try_get_dont_need_hostel_checkbox(self):
        return self.is_element_visible(self.DONT_NEED_HOSTEL_CHECKBOX)

    # FILTERED
    def try_get_filtered_need_of_hostel(self, given_need_of_hostel):
        self.wait.until(EC.text_to_be_present_in_element(self.FILTERED_NEED_OF_HOSTEL, given_need_of_hostel))
        return self.driver.find_element(*self.FILTERED_NEED_OF_HOSTEL)

    def try_get_filtered_need_hostel_column(self, given_need_of_hostel):
        cells_texts = []

        for i in range(1, len(self.FILTERED_HOSTEL_COLUMN), 1):
            cell_path = "//tbody[@class='pointer']/tr[@class='ng-scope'][%d]/td[16]" % i
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, cell_path), given_need_of_hostel))
            cells_texts.append((self.driver.find_element(*(By.XPATH, cell_path))).text)

        return cells_texts

    # bound to military service(bound, isn`t bound)
    def try_get_bound_to_military_checkbox(self):
        return self.is_element_visible(self.BOUND_TO_MILITARY_CHECKBOX)

    def try_get_not_bound_to_military_checkbox(self):
        return self.is_element_visible(self.NOT_BOUND_TO_MILITARY_CHECKBOX)

    # FILTERED
    def try_get_filtered_bound_to_military(self, given_bound_to_military):
        self.wait.until(EC.text_to_be_present_in_element(self.FILTERED_BOUND_TO_MILITARY, given_bound_to_military))
        return self.driver.find_element(*self.FILTERED_BOUND_TO_MILITARY)

    def try_get_filtered_military_column(self, given_bound_to_military):

        cells_texts = []

        for i in range(1, len(self.FILTERED_MILITARY_COLUMN), 1):
            cell_path = "//tbody[@class='pointer']/tr[@class='ng-scope'][%d]/td[15]" % i
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, cell_path), given_bound_to_military))
            cells_texts.append((self.driver.find_element(*(By.XPATH, cell_path))).text)

        return cells_texts

    # resident(foreigner, isn`t foreigner)
    def try_get_resident_foreigner_checkbox(self):
        return self.is_element_visible(self.RESIDENT_FOREIGNER_CHECKBOX)

    def try_get_resident_not_foreigner_checkbox(self):
        return self.is_element_visible(self.RESIDENT_NOT_FOREIGNER_CHECKBOX)

    # FILTERED
    def try_get_filtered_resident(self, given_resident):
        self.wait.until(EC.text_to_be_present_in_element(self.FILTERED_RESIDENT, given_resident))
        return self.driver.find_element(*self.FILTERED_RESIDENT)

    def try_get_filtered_resident_column(self, given_resident):
        cells_texts = []

        for i in range(1, len(self.FILTERED_RESIDENT_COLUMN), 1):
            cell_path = "//tbody[@class='pointer']/tr[@class='ng-scope'][%d]/td[12]" % i
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, cell_path), given_resident))
            cells_texts.append((self.driver.find_element(*(By.XPATH, cell_path))).text)

        return cells_texts

    # SEARCH
    # to all searches
    def try_get_input_group(self):
        return self.is_element_visible(self.INPUT_GROUP_SEARCH_BUTTON)

    def try_get_ok_button(self):
        return self.is_element_visible(self.OK_GROUP_SEARCH_BUTTON)

    # surname search
    def try_get_choose_surname(self):
        return self.is_element_visible(self.CHOOSE_SURNAME_SEARCH)

    def try_get_searched_surname(self, given_surname):
        self.wait.until(EC.text_to_be_present_in_element(self.SEARCHED_SURNAME, given_surname))
        return self.is_element_visible(self.SEARCHED_SURNAME)

    # person_id search
    def try_get_choose_person_id(self):
        return self.is_element_visible(self.CHOOSE_PERSON_ID_SEARCH)

    def try_get_id_for_search(self):
        return self.is_element_visible(self.PERSON_ID_FOR_SEARCH)

    def try_get_searched_person_id(self, given_person_id):
        self.wait.until(EC.text_to_be_present_in_element(self.SEARCHED_PERSON_ID, given_person_id))
        return self.driver.find_element(*self.SEARCHED_PERSON_ID)

    # num_os search
    def try_get_choose_num_os(self):
        return self.is_element_visible(self.CHOOSE_NUM_OS_SEARCH)

    def try_get_searched_num_os(self, given_num_os):
        self.wait.until(EC.text_to_be_present_in_element(self.SEARCHED_NUM_OS, given_num_os))
        return self.is_element_visible(self.SEARCHED_NUM_OS)

    # series_os search
    def try_get_choose_series_os(self):
        return self.is_element_visible(self.CHOOSE_SERIES_OS_SEARCH)

    def try_get_searched_series_os(self, given_series_os):
        self.wait.until(EC.text_to_be_present_in_element(self.SEARCHED_SERIES_OS, given_series_os))
        return self.driver.find_element(*self.SEARCHED_SERIES_OS)

    def column_as_list(self, column_number):
        """
        Method get column number as input
        :return: list of text data in column
        """
        list_of_column_text = []
        list_of_column_elements = self.driver.find_elements_by_xpath("//tbody/tr/td[" + str(column_number) + "]")
        for element in list_of_column_elements:
            list_of_column_text.append(int(element.text))
        return list_of_column_text

    def get_all_hidden_columns(self):
        """
        Method get all columns with class attribute "ng-scope ng-hide"
        :return: list of visible columns number according to COLUMNS_DICT
        """
        visible_columns_list = []
        column_headers = self.driver.find_elements_by_xpath('//thead/tr/th')
        for i in range(len(column_headers)):
            if column_headers[i].get_attribute('class') == 'ng-scope ng-hide':
                visible_columns_list.append(i + 1)
        return visible_columns_list

    def search_person_by_id(self, person_id):
        """
        This method searches person by id.
        :param person_id: is person id.
        """
        self.is_this_page()
        self.try_get_choose_person_id().click()
        self.try_get_input_group().clear()
        self.try_get_input_group().send_keys(person_id)
        self.try_get_ok_button().click()

    def get_number_from_selector(self, selector):
        return self.driver.find_element(*selector).text

    def show_all_columns(self):
        list_all_unchecked_checkboxes = (self.COLUMN_SURNAME_ADD,
                                         self.COLUMN_NAME_ADD,
                                         self.COLUMN_FATHER_NAME_ADD,
                                         self.COLUMN_MARITAL_STATUS_ADD,
                                         self.COLUMN_CITIZENSHIP_ADD,
                                         self.COLUMN_RESIDENT_ADD,
                                         self.COLUMN_PLACE_OF_BIRTH_ADD,
                                         self.COLUMN_VZ_ADD,
                                         self.COLUMN_MATERIAL_LIABILITY_ADD)
        assert self.is_element_visible(PersonsPage.FIELD_CHOOSER_BUTTON)
        self.driver.find_element(*PersonsPage.FIELD_CHOOSER_BUTTON).click()
        self.wait_until_page_generate()
        self.is_element_visible(self.MODAL_HEADER_CHOOSER)
        for checkbox in list_all_unchecked_checkboxes:

            self.driver.find_element(*checkbox).click()

        self.try_field_chooser_red_close_button().click()

        self.is_element_present(self.MODAL_HEADER_CHOOSER)
        self.wait_until_page_generate()




    def return_added_person_surname(self, person):
        """
        Method searches new added person
        :param person: persons model in Person format
        :return: finded person's surname
        """
        self.is_this_page()
        self.try_get_choose_surname().click()
        self.try_get_input_group().clear()
        self.try_get_input_group().send_keys(person.surname_ukr)
        self.try_get_ok_button().click()
        return self.try_get_searched_surname(person.surname_ukr).text.partition(' ')[0]

    def del_newly_created_person(self, person):
        self.is_this_page()
        expected_person = self.try_get_searched_surname(person.surname_ukr).text.partition(' ')[0]
        if expected_person:
            self.delete_first_person_in_page

    def return_to_persons_main_page(self, app):
        app.internal_page.persons_page_link.click()
        self.wait_until_page_generate()
        self.try_get_refresh_upper_button().click()

    def search_person_by_surname(self, given_surname):
        """
        Method performs search by surname
        :param given_surname: wanted surname
        :return:
        """
        self.is_this_page()
        self.try_get_choose_surname().click()
        self.try_get_input_group().clear()
        self.try_get_input_group().send_keys(given_surname)
        self.try_get_ok_button().click()
        self.wait_until_page_generate()