# coding: utf8
from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PersonsPage(InternalPage):
    #
    #TO SEARCH
    #
    ADD_PERSON_BUTTON               = (By.XPATH, "//button[contains(@class,'btn-success')]")
    CHOOSE_SURNAME_SEARCH           = (By.XPATH, "//div[@class='col-sm-12']//option[@value='0']")
    CHOOSE_PERSON_ID_SEARCH         = (By.XPATH, "//div[@class='col-sm-12']//option[@value='1']")
    CHOOSE_NUM_OS_SEARCH            = (By.XPATH, "//div[@class='col-sm-12']//option[@value='2']")
    CHOOSE_SERIES_OS_SEARCH         = (By.XPATH, "//div[@class='col-sm-12']//option[@value='3']")
    INPUT_GROUP_SEARCH_BUTTON       = (By.XPATH, "//div[@class='input-group']/input")
    OK_GROUP_SEARCH_BUTTON          = (By.XPATH, "//div[@class='input-group']/span/button")
    #in table
    SEARCHED_SURNAME                = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[2]")
    SEARCHED_PERSON_ID              = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[1]")
    SEARCHED_NUM_OS                 = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[11]")
    SEARCHED_SERIES_OS              = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[10]")
    #
    #TO FILTER
    #
    REFRESH_UPPER_BUTTON            = (By.XPATH, "//div[@class='container-fluid admissionSystemApp-container']//div[@class='col-md-2 col-lg-2 filter']/p[1]/button")
    REFRESH_BOTTOM_BUTTON           = (By.XPATH, "//div[@class='container-fluid admissionSystemApp-container']//div[@class='col-md-2 col-lg-2 filter']/p[2]/button")
    GENDER_MALE_CHECKBOX            = (By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[1]/label/input")
    GENDER_FEMALE_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[2]/label/input")
    GENDER_NOT_DEFINED_CHECKBOX     = (By.XPATH, "//div[@class='panel-group']/div[1]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_APPLICANT_CHECKBOX         = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[1]/label/input")
    TYPE_STUDENT_CHECKBOX           = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[2]/label/input")
    TYPE_SCIENTIST_CHECKBOX         = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[3]/label/input")
    TYPE_EMPLOYEE_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[4]/label/input")
    TYPE_GRADUATE_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[5]/label/input")
    TYPE_OUTSIDER_CHECKBOX          = (By.XPATH, "//div[@class='panel-group']/div[2]/div[2]/div[@class='panel-body']/div[6]/label/input")
    NEED_HOSTEL_CHECKBOX            = (By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[1]/label/input")
    DONT_NEED_HOSTEL_CHECKBOX       = (By.XPATH, "//div[@class='panel-group']/div[3]/div[2]/div[@class='panel-body']/div[2]/label/input")
    BOUND_TO_MILITARY_CHECKBOX      = (By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[1]/label/input")
    NOT_BOUND_TO_MILITARY_CHECKBOX  = (By.XPATH, "//div[@class='panel-group']/div[4]/div[2]/div[@class='panel-body']/div[2]/label/input")
    RESIDENT_FOREIGNER_CHECKBOX     = (By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[1]/label/input")
    RESIDENT_NOT_FOREIGNER_CHECKBOX = (By.XPATH, "//div[@class='panel-group']/div[5]/div[2]/div[@class='panel-body']/div[2]/label/input")
    #in table
    #the 1 value
    FILTERED_GENDER                 = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[7]")
    FILTERED_TYPE                   = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[6]")
    FILTERED_NEED_OF_HOSTEL         = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[16]")
    FILTERED_BOUND_TO_MILITARY      = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[15]")
    FILTERED_RESIDENT               = (By.XPATH, "//tbody[@class='pointer']/tr[@class='ng-scope'][1]/td[12]")

    SHOW_HIDE_FILTERS_BUTTON        = (By.XPATH, "//button[contains(@ng-click,'hideFilterFunc')]")
    ACTIVE_ITEMS_PER_PAGE_BUTTON    = (By.XPATH, "//button[contains(@class, 'active')]")
    PREVIOUS_PAGE                   = (By.XPATH, "//li[contains(@title, 'Previous Page')]")
    LAST_NUMBERED_PAGE              = (By.XPATH, "//li[contains(@title, 'Last Page')]/preceding-sibling::li[2]/span")
    LAST_PAGE                       = (By.XPATH, "//li[contains(@title, 'Last Page')]")
    FIELD_CHOOSER_BUTTON            = (By.XPATH, "//button[contains(@class, 'field-chooser-button')]")
    FIELD_CHOOSER_RED_CLOSE_BUTTON  = (By.XPATH, "//button[parent::div[contains(@class, 'modal-footer')]]")
    INACTIVE_COLUMNS_MODAL          = (By.XPATH, "//ul[@class='list-group']/li/label/input[not(@checked)]")
    # Columns dictionary binding number of column to it's name
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


    @property
    def is_this_page(self):
        return self.is_element_visible(self.ADD_PERSON_BUTTON)

    @property
    def add_person_link(self):
        return self.driver.find_element_by_xpath(*self.ADD_PERSON_BUTTON)

    #FILTER
    #to all filters
    def try_get_refresh_upper_button(self):
        return self.is_element_visible(self.REFRESH_UPPER_BUTTON)

    def try_get_refresh_bottom_button(self):
        return self.is_element_visible(self.REFRESH_BOTTOM_BUTTON)

    #gender (male, female, not defined)
    def try_get_gender_male_checkbox(self):
        return self.is_element_visible(self.GENDER_MALE_CHECKBOX)

    def try_get_gender_female_checkbox(self):
        return self.is_element_visible(self.GENDER_FEMALE_CHECKBOX)

    def try_get_gender_not_defined_checkbox(self):
        return self.is_element_visible(self.GENDER_NOT_DEFINED_CHECKBOX)
    #FILTERED
    def try_get_filtered_gender(self):
        return self.driver.find_element(*self.FILTERED_GENDER)


    #type (applicant, student, scientist, employee, graduate, outsider)
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
    #FILTERED



    #need for hostel (need, doesn`t need)
    def try_get_need_hostel_checkbox(self):
        return self.is_element_visible(self.NEED_HOSTEL_CHECKBOX)

    def try_get_dont_need_hostel_checkbox(self):
        return self.is_element_visible(self.DONT_NEED_HOSTEL_CHECKBOX)
    #FILTERED



    #bound to military service(bound, isn`t bound)
    def try_get_bound_to_military_checkbox(self):
        return self.is_element_visible(self.BOUND_TO_MILITARY_CHECKBOX)

    def try_get_not_bound_to_military_checkbox(self):
        return self.is_element_visible(self.NOT_BOUND_TO_MILITARY_CHECKBOX)
    #FILTERED


    #resident(foreigner, isn`t foreigner)
    def try_get_resident_foreigner_checkbox(self):
        return self.is_element_visible(self.RESIDENT_FOREIGNER_CHECKBOX)

    def try_get_resident_not_foreigner_checkbox(self):
        return self.is_element_visible(self.RESIDENT_NOT_FOREIGNER_CHECKBOX)
    #FILTERED





    #SEARCH
    #to all searches
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

    # persone_id search
    def try_get_choose_person_id(self):
        return self.is_element_visible(self.CHOOSE_PERSON_ID_SEARCH)

    def try_get_searched_person_id(self, given_person_id):
        self.wait.until(EC.text_to_be_present_in_element(self.SEARCHED_PERSON_ID, given_person_id))
        return self.driver.find_element(*self.SEARCHED_PERSON_ID)

    # num_os search
    def try_get_choose_num_os(self):
        return self.is_element_visible(self.CHOOSE_NUM_OS_SEARCH)

    def try_get_searched_num_os(self, given_num_os):
        self.wait.until(EC.text_to_be_present_in_element(self.SEARCHED_NUM_OS, given_num_os))
        return self.driver.find_element(*self.SEARCHED_NUM_OS)

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
            list_of_column_text.append(element.text)
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
                visible_columns_list.append(i+1)
        return visible_columns_list

    def show_all_columns(self):
        self.driver.find_element(*PersonsPage.FIELD_CHOOSER_BUTTON).click()
        not_selected_columns =\
            self.driver.find_elements(*PersonsPage.INACTIVE_COLUMNS_MODAL)
        for column_name in not_selected_columns:
            column_name.click()
        self.driver.find_element(*PersonsPage.FIELD_CHOOSER_RED_CLOSE_BUTTON).click()

    def get_number_from_selector(self, selector):
        return self.driver.find_element(*selector).text
