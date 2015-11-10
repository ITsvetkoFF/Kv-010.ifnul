#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.web_elem_utils import input_text_in_field
from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By
from utils.common_methods import CommonMethods
__author__ = 'Deorditsa'


class AddPersonContactsPage(AddPersonPage):
    MOBILE_PHONE1_INPUT = (By.ID, "phone")
    MOBILE_PHONE2_INPUT = (By.ID, "mobilePhone")
    HOME_PHONE_INPUT = (By.ID, "homePhone")
    WORK_PHONE_INPUT = (By.ID, "workPhone")
    EMAIL_INPUT = (By.ID, "email")
    SKYPE_INPUT = (By.ID, "skype")
    SITE_INPUT = (By.ID, "site")
    ICQ_INPUT = (By.ID, "ICQ")

    # overriding functions
    def is_this_page(self):
        return self.is_element_visible(self.SKYPE_INPUT)

    # web elements
    @property
    def first_mobile_phone_field(self):
        return self.driver.find_element(*self.MOBILE_PHONE1_INPUT)

    @property
    def second_mobile_phone_field(self):
        return self.driver.find_element(*self.MOBILE_PHONE2_INPUT)

    @property
    def home_phone_field(self):
        return self.driver.find_element(*self.HOME_PHONE_INPUT)

    @property
    def work_phone_field(self):
        return self.driver.find_element(*self.WORK_PHONE_INPUT)

    @property
    def email_field(self):
        return self.driver.find_element(*self.EMAIL_INPUT)

    @property
    def skype_field(self):
        return self.driver.find_element(*self.SKYPE_INPUT)

    @property
    def site_field(self):
        return self.driver.find_element(*self.SITE_INPUT)

    @property
    def icq_field(self):
        return self.driver.find_element(*self.ICQ_INPUT)
    
    def mobile_phone1_input(self):
        return self.is_element_visible(self.MOBILE_PHONE1_INPUT)

    def mobile_phone2_input(self):
        return self.is_element_visible(self.MOBILE_PHONE2_INPUT)

    def home_phone_input(self):
        return self.is_element_visible(self.HOME_PHONE_INPUT)

    def work_phone_input(self):
        return self.is_element_visible(self.WORK_PHONE_INPUT)

    def email_input(self):
        return self.is_element_visible(self.EMAIL_INPUT)

    def skype_input(self):
        return self.is_element_visible(self.SKYPE_INPUT)

    def site_input(self):
        return self.is_element_visible(self.SITE_INPUT)

    def icq_input(self):
        return self.is_element_visible(self.ICQ_INPUT)

    # web element's functions
   

    def set_first_mobile_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parameter. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.first_mobile_phone_field, phone)

    def set_second_mobile_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parameter. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.second_mobile_phone_field, phone)

    def set_home_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parameter. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.home_phone_field, phone)

    def set_work_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parameter. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.work_phone_field, phone)

    def set_email(self, email):
        """
        Method sets the e-mail address.
        :param email: String parameter.
        :return:
        """
        input_text_in_field(self.email_field, email)

    def set_skype(self, skype):
        """
        Method sets the persons Skype ID
        :param skype: String parameter.
        :return:
        """
        input_text_in_field(self.skype_field, skype)

    def set_site(self, site):
        """
        Method sets the persons web-site
        :param site: String parameter.
        :return:
        """
        input_text_in_field(self.site_field, site)

    def set_icq(self, icq):
        """
        Method sets the persons ICQ ID
        :param icq: Integer parameter.
        :return:
        """
        input_text_in_field(self.icq_field, str(icq))

    # general functions
    def fill_in_contact_page(self, person):
        """
        Method fill in data on the contact persons page
        :param person: persons model in Person format
        :return:
        """
        self.is_this_page()
        self.set_first_mobile_phone(person.mobile_phone1)
        self.set_second_mobile_phone(person.mobile_phone2)
        self.set_home_phone(person.home_phone)
        self.set_work_phone(person.work_phone)
        self.set_email(person.email)
        self.set_skype(person.skype)
        self.set_site(person.web_site)
        self.set_icq(person.icq)

    def read_in_contact_page(self, person_new):
        """
        Method read the data on the contact persons page
        :param person_new: persons model in Person format
        :return:
        """
        self.is_this_page
        common_methods = CommonMethods(self.driver)
        person_new.mobile_phone1 = common_methods.get_value_from_text_field(self.driver.find_element(*self.MOBILE_PHONE1_INPUT))
        person_new.mobile_phone2 = common_methods.get_value_from_text_field(self.driver.find_element(*self.MOBILE_PHONE2_INPUT))
        person_new.home_phone = common_methods.get_value_from_text_field(self.driver.find_element(*self.HOME_PHONE_INPUT))
        person_new.work_phone = common_methods.get_value_from_text_field(self.driver.find_element(*self.WORK_PHONE_INPUT))
        person_new.email = common_methods.get_value_from_text_field(self.driver.find_element(*self.EMAIL_INPUT))
        person_new.skype = common_methods.get_value_from_text_field(self.driver.find_element(*self.SKYPE_INPUT))
        person_new.web_site = common_methods.get_value_from_text_field(self.driver.find_element(*self.SITE_INPUT))
        person_new.icq = common_methods.get_value_from_text_field(self.driver.find_element(*self.ICQ_INPUT))
        return person_new
