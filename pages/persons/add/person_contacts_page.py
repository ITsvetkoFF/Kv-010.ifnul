#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.web_elem_utils import input_text_in_field

__author__ = 'Deorditsa'

from person_base_page import AddPersonPage
from selenium.webdriver.common.by import By


class AddPersonContactsPage(AddPersonPage):
    MOBILE_PHONE1_INPUT = (By.ID, "phone")
    MOBILE_PHONE2_INPUT = (By.ID, "mobilePhone")
    HOME_PHONE_INPUT = (By.ID, "homePhone")
    WORK_PHONE_INPUT = (By.ID, "workPhone")
    EMAIL_INPUT = (By.ID, "email")
    SKYPE_INPUT = (By.ID, "skype")
    SITE_INPUT = (By.ID, "site")
    ICQ_INPUT = (By.ID, "ICQ")

    # override functions
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

    # web element functions
    def set_first_mobile_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.first_mobile_phone_field, phone)

    def set_second_mobile_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.second_mobile_phone_field, phone)

    def set_home_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.home_phone_field, phone)

    def set_work_phone(self, phone):
        """
        Method sets the first mobile phone
        :param phone: String parametr. Pattern is "(xxx) xxx-xx-xx"
        :return:
        """
        input_text_in_field(self.work_phone_field, phone)

    def set_email(self, email):
        """
        Method sets the e-mail address.
        :param email: String parametr.
        :return:
        """
        input_text_in_field(self.email_field, email)

    def set_skype(self, skype):
        """
        Method sets the persons Skype ID
        :param skype: String parametr.
        :return:
        """
        input_text_in_field(self.skype_field, skype)

    def set_site(self, site):
        """
        Method sets the persons web-site
        :param site: String parametr.
        :return:
        """
        input_text_in_field(self.site_field, site)

    def set_icq(self, icq):
        """
        Method sets the persons ICQ ID
        :param icq: Integer parametr.
        :return:
        """
        input_text_in_field(self.icq_field, icq)

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
