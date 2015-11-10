#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Deorditsa'

from utils.common_methods import CommonMethods
from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddPersonAddressesPage(AddPersonPage):

    BIRTH_PLACE_SELECTOR = "div[ng-model='person.birthPlace']>div:nth-child(%s) ul a div"
    BIRTH_PLACE_LEVEL_SELECTOR = "div[ng-model='person.birthPlace']>div:nth-child(%s) label+div span"
    REG_ADDRESS_PLACE_SELECTOR = "div[ng-model='addresses.regAddresses.adminUnitId']>div:nth-child(%s) ul a div"
    REG_ADDRESS_LEVEL_SELECTOR = "div[ng-model='addresses.regAddresses.adminUnitId']>div:nth-child(%s) label+div span"
    REG_POST_ADDRESS_PLACE_SELECTOR = "div[ng-model='addresses.postAddresses.adminUnitId']>div:nth-child(%s) ul a div"
    REG_POST_ADDRESS_LEVEL_SELECTOR = "div[ng-model='addresses.postAddresses.adminUnitId']>div:nth-child(%s) label+div span"
    POST_PLACE_LABEL = "РњiСЃС†Рµ РїСЂРѕР¶РёРІР°РЅРЅСЏ"
    ALL_REGISTRATION_PLACES_SELECT = (By.XPATH, "//a[@class='ui-select-choices-row-inner']//div[@class='ng-binding ng-scope']")
    INDEX_INPUT = (By.ID, "inputZipCodeReg")
    ADDRESS_TYPE_CHOOSER = (By.ID, "inputStreetTypeReg")
    ALL_ADDRESS_TYPE_SELECT = (By.XPATH, "//select[@id='inputStreetTypeReg']//option")
    STREET_INPUT = (By.XPATH, "//input[@id='inputStreetReg']")
    HOUSE_INPUT = (By.XPATH, "//input[@id='inputHouseReg']")
    APARTMENT_INPUT = (By.XPATH, "//input[@id='inputApartmentReg']")
    IS_ADDRESSES_MATCH = (By.XPATH, "//input[@ng-model='addresses.isAdressesMatch']")
    ALL_POST_PLACES_SELECT = (By.XPATH, "//a[@class='ui-select-choices-row-inner']//div[@class='ng-binding ng-scope']")
    INDEX_POST_INPUT = (By.XPATH, "//input[@id='inputZipCodePost']")
    ADDRESS_TYPE_POST_CHOOSER = (By.XPATH, "//select[@id='inputStreetTypePost']")
    ALL_ADDRESS_TYPE_POST_SELECT = (By.XPATH, "//select[@id='inputStreetTypePost']//option")
    STREET_POST_INPUT = (By.XPATH, "//input[@id='inputStreetPost']")
    HOUSE_POST_INPUT = (By.XPATH, "//input[@id='inputHousePost']")
    APARTMENT_POST_INPUT = (By.XPATH, "//input[@id='inputApartmentPost']")

    FULL_BIRTH_PLACE_TEXT = (By.XPATH, ".//*[@id='person']//div[@ng-model='person.birthPlace']//span[@class='ng-binding ng-scope']")
    FULL_BIRTH_REGISTRATION_TEXT = (By.XPATH, ".//*[@id='person']//div[@ng-model='addresses.regAddresses.adminUnitId']//span[@class='ng-binding ng-scope']")
    FULL_BIRTH_POST_REGISTRATION_TEXT = (By.XPATH, ".//*[@id='person']//div[@ng-model='addresses.postAddresses.adminUnitId']//span[@class='ng-binding ng-scope']")

    ARRAY_BIRTH_PLACE_SELECTOR = (By.XPATH, ".//*[@name='birthPlaceInput']//span[@class='ng-binding ng-scope']")
    ARRAY_REGISTRATION_PLACE_SELECTOR = (By.XPATH, ".//*[@name='regAddressesInput']//span[@class='ng-binding ng-scope']")
    ARRAY_POST_PLACE_SELECTOR = (By.XPATH, ".//*[@label='Мiсце проживання']//span[@class='ng-binding ng-scope']")
    SELECTED_ADDRESS_TYPE = (By.XPATH, ".//*[@id='inputStreetTypeReg']/option[@selected='selected']")
    SELECTED_ADDRESS_TYPE_POST = (By.XPATH, ".//*[@id='inputStreetTypePost']/option[@selected='selected']")

    @property
    def is_this_page(self):
        return self.is_element_visible(self.INDEX_INPUT)

    def array_birth_place_selector(self):
        return self.driver.find_elements(*self.ARRAY_BIRTH_PLACE_SELECTOR)

    def array_post_place_selector(self):
        return self.driver.find_elements(*self.ARRAY_POST_PLACE_SELECTOR)

    def array_registration_place_selector(self):
        return self.driver.find_elements(*self.ARRAY_REGISTRATION_PLACE_SELECTOR)

    def index_input(self):
        return self.is_element_visible(self.INDEX_INPUT)

    def address_type_chooser(self):
        return self.is_element_visible(self.SELECTED_ADDRESS_TYPE)

    def street_input(self):
        return self.is_element_visible(self.STREET_INPUT)

    def house_input(self):
        return self.is_element_visible(self.HOUSE_INPUT)

    def apartment_input(self):
        return self.is_element_visible(self.APARTMENT_INPUT)

    def index_post_input(self):
        return self.is_element_visible(self.INDEX_POST_INPUT)

    def address_type_post_chooser(self):
        return self.is_element_visible(self.SELECTED_ADDRESS_TYPE_POST)

    def street_post_input(self):
        return self.is_element_visible(self.STREET_POST_INPUT)

    def house_post_input(self):
        return self.is_element_visible(self.HOUSE_POST_INPUT)

    def apartment_post_input(self):
        return self.is_element_visible(self.APARTMENT_POST_INPUT)

    def get_selector_for_current_block_and_level(self, selector, level):
        """
        Method makes selector for current block and drop-down current level
        :param selector: Selector which points to current block
        :param level: Integer number which means level in current block
        :return:
        """
        return (By.CSS_SELECTOR, selector % str(level))

    def select_birth_place(self, address, address_level):
        """
        Method select address in drop-down menu in birth place block on the current level
        :param address: String address. If address exists in select menu, then method will click on it, else will leave default value
        :param address_level: Integer number which means level in current block
        :return:
        """
        self.is_element_visible(
            self.get_selector_for_current_block_and_level(self.BIRTH_PLACE_LEVEL_SELECTOR, address_level + 1))
        self.driver.find_element(
            *self.get_selector_for_current_block_and_level(self.BIRTH_PLACE_LEVEL_SELECTOR, address_level + 1)).click()
        all_level_addresses = self.driver.find_elements(
            *self.get_selector_for_current_block_and_level(self.BIRTH_PLACE_SELECTOR, address_level + 1))
        self.find_element_in_select(all_level_addresses, address).click()
        self.is_element_present(self.SPINNER_OFF)

    def select_registration_address(self, address, address_level):
        """
        Method select address in drop-down menu in registration adress block on the current level
        :param address: String address. If address exists in select menu, then method will click on it, else will leave default value
        :param address_level: Integer number which means level in current block
        :return:
        """
        self.is_element_visible(
            self.get_selector_for_current_block_and_level(self.REG_ADDRESS_LEVEL_SELECTOR, address_level + 1))
        self.driver.find_element(
            *self.get_selector_for_current_block_and_level(self.REG_ADDRESS_LEVEL_SELECTOR, address_level + 1)).click()
        all_level_addresses = self.driver.find_elements(
            *self.get_selector_for_current_block_and_level(self.REG_ADDRESS_PLACE_SELECTOR, address_level + 1))
        self.find_element_in_select(all_level_addresses, address).click()
        self.is_element_present(self.SPINNER_OFF)

    def select_post_registration_address(self, address, address_level):
        """
        Method select address in drop-down menu in registration adress block on the current level
        :param address: String address. If address exists in select menu, then method will click on it, else will leave default value
        :param address_level: Integer number which means level in current block
        :return:
        """
        self.is_element_visible(
            self.get_selector_for_current_block_and_level(self.REG_POST_ADDRESS_LEVEL_SELECTOR, address_level + 1))
        self.driver.find_element(
            *self.get_selector_for_current_block_and_level(self.REG_POST_ADDRESS_LEVEL_SELECTOR, address_level + 1)).click()
        all_level_addresses = self.driver.find_elements(
            *self.get_selector_for_current_block_and_level(self.REG_POST_ADDRESS_PLACE_SELECTOR, address_level + 1))
        self.find_element_in_select(all_level_addresses, address).click()
        self.is_element_present(self.SPINNER_OFF)

    def set_zip_code(self, index):
        """
        Method sets the zip code
        :param index: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.INDEX_INPUT, index)

    def set_post_zip_code(self, index):
        """
        Method sets the post zip code
        :param index: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.INDEX_POST_INPUT, index)

    def reg_address_type_select(self, address_type):
        """
        Method select type of address in select menu
        :param address_type: String address type. If type exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_visible(self.ADDRESS_TYPE_CHOOSER)
        Select(self.driver.find_element(*self.ADDRESS_TYPE_CHOOSER)).select_by_visible_text(address_type)

    def post_address_type_select(self, address_type):
        """
        Method select type of post address in select menu
        :param address_type: String address type. If type exists in select menu, then method will click on it, else will leave default value
        :return:
        """
        self.is_element_visible(self.ADDRESS_TYPE_POST_CHOOSER)
        Select(self.driver.find_element(*self.ADDRESS_TYPE_POST_CHOOSER)).select_by_visible_text(address_type)

    def set_street(self, street):
        """
        Method sets the street
        :param street: String parametr.
        :return:
        """
        self.emulation_of_input(self.STREET_INPUT, street)

    def set_street_for_post_address(self, street):
        """
        Method sets the street fo post address.
        :param street: String parametr.
        :return:
        """
        self.emulation_of_input(self.STREET_POST_INPUT, street)

    def set_house(self, house):
        """
        Method sets the house
        :param house: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.HOUSE_INPUT, house)

    def set_house_for_post_address(self, house):
        """
        Method sets the house for post address.
        :param house: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.HOUSE_POST_INPUT, house)

    def set_apartment(self, apartment):
        """
        Method sets the apartment
        :param apartment: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.APARTMENT_INPUT, apartment)

    def set_apartment_for_post_address(self, apartment):
        """
        Method sets the apartment for post address.
        :param apartment: Integer parametr.
        :return:
        """
        self.emulation_of_input(self.APARTMENT_POST_INPUT, apartment)

    def check_is_reg_and_post_addresses_the_same(self, is_addresses_match):
        """
        Method checks or unchecks "Is registration address and post address the same?" checkbox
        :param is_addresses_match: Boolean format. Must be True, if registration address and post address are the same.
        :return:
        """
        common_methods = CommonMethods(self.driver)
        common_methods.checkbox_manager(self.driver.find_element(*self.IS_ADDRESSES_MATCH), is_addresses_match)

    def fill_in_address_page(self, person):
        """
        Method fill in data on the address persons page
        :param person: persons model in Person format
        :return:
        """
        common_methods = CommonMethods(self.driver)
        self.is_this_page
        for i in range(0, len(person.burn_place)):
            self.select_birth_place(person.burn_place[i], i)

        for i in range(0, len(person.registration_place["area"])):
            self.select_registration_address(person.registration_place["area"][i], i)

        self.set_zip_code(person.registration_place["index"])
        self.reg_address_type_select(person.registration_place["type"])
        self.set_street(person.registration_place["street"])
        self.set_house(person.registration_place["house"])
        self.set_apartment(person.registration_place["apartment"])
        self.check_is_reg_and_post_addresses_the_same(person.registration_place["is_addresses_match"])
        if not common_methods.is_checkbox_checked(self.driver.find_element(*self.IS_ADDRESSES_MATCH)):

            for i in range(0, len(person.post_registration_place["area"])):
                self.select_post_registration_address(person.registration_place["area"][i], i)

            self.set_post_zip_code(person.post_registration_place["index"])
            self.post_address_type_select(person.post_registration_place["type"])
            self.set_street_for_post_address(person.post_registration_place["street"])
            self.set_house_for_post_address(person.post_registration_place["house"])
            self.set_apartment_for_post_address(person.post_registration_place["apartment"])

    def read_in_address_page(self, person_new):
        """
        Method read the data on the address persons page
        :param person_new: persons model in Person format
        :return:
        """
        common_methods = CommonMethods(self.driver)
        self.is_this_page
        self.wait_until_page_generate()

        # reading birth place
        for place in self.driver.find_elements(*self.FULL_BIRTH_PLACE_TEXT):
            person_new.burn_place.append(place.text)

        # reading registration address
        for place in self.driver.find_elements(*self.FULL_BIRTH_REGISTRATION_TEXT):
            person_new.registration_place["area"].append(place.text)

        person_new.registration_place["index"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.INDEX_INPUT))
        person_new.registration_place["type"] = self.address_type_chooser().text
        person_new.registration_place["street"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.STREET_INPUT)).encode('cp1251')
        person_new.registration_place["house"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.HOUSE_INPUT))
        person_new.registration_place["apartment"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.APARTMENT_INPUT))
        person_new.registration_place["is_addresses_match"] = common_methods.is_checkbox_checked(
            self.driver.find_element(*self.IS_ADDRESSES_MATCH))

        if person_new.registration_place["is_addresses_match"]:
            person_new.post_registration_place["index"] = person_new.registration_place["index"]
            person_new.post_registration_place["type"] = person_new.registration_place["type"]
            person_new.post_registration_place["street"] = person_new.registration_place["street"]
            person_new.post_registration_place["house"] = person_new.registration_place["house"]
            person_new.post_registration_place["apartment"] = person_new.registration_place["apartment"]
            return person_new

        # reading post address
        for place in self.driver.find_elements(*self.FULL_BIRTH_POST_REGISTRATION_TEXT):
            person_new.post_registration_place["area"].append(place.text)

        person_new.post_registration_place["index"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.INDEX_POST_INPUT))
        person_new.post_registration_place["type"] = common_methods.get_value_from_select(self.driver.find_element(*self.ADDRESS_TYPE_POST_CHOOSER)).encode('cp1251')
        person_new.post_registration_place["street"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.STREET_POST_INPUT)).encode('cp1251')
        person_new.post_registration_place["house"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.HOUSE_POST_INPUT)).encode('cp1251')
        person_new.post_registration_place["apartment"] = common_methods.get_value_from_text_field(self.driver.find_element(*self.APARTMENT_POST_INPUT))
        return person_new
