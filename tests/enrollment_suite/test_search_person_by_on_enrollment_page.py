#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pytest
from model.user import User
from time import sleep
from utils.data_provider_from_json import DataProviderJSON
from utils.personCreator import PersonCreator

__author__ = 'odeortc'


class TestSearchPersonBy(object):

    @pytest.fixture
    def real_person(request):
        project_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.normpath(os.path.abspath(project_path) + "../../../resources/existing_person.json")
        person_creator = PersonCreator(path)
        return person_creator.create_person_from_json()

    @pytest.fixture
    def values(request):
        return DataProviderJSON("values_for_enrollment_test.json").get_dict_value()

    def search_by_pib_and_surname(self, app, searched_value, searched_by_option, is_valid_value):
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        app.enrollments_main_page.search_person_by(searched_by_option)
        app.enrollments_main_page.set_search_person_by(searched_value)
        app.enrollments_main_page.ok_for_input_field
        all_found_persons_pib = app.enrollments_main_page.get_all_found_persons_pib()
        check = False
        if is_valid_value and len(all_found_persons_pib) > 0:
            for pib in all_found_persons_pib:
                if pib.text.__contains__(searched_value):
                    check = True
                else:
                    check = False
                    break
        elif not is_valid_value and len(all_found_persons_pib) == 0:
            check = True
        app.enrollments_main_page.cancel_click
        return check

    def search_by_person_id(self, app, searched_value, searched_by_option, is_valid_value):
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        app.enrollments_main_page.search_person_by(searched_by_option)
        app.enrollments_main_page.set_search_person_by(searched_value)
        app.enrollments_main_page.ok_for_input_field
        all_found_persons_id = app.enrollments_main_page.get_all_found_persons_id()
        check = False
        if is_valid_value and len(all_found_persons_id) == 1 and all_found_persons_id[0].text == str(searched_value):
            check = True
        elif not is_valid_value and len(all_found_persons_id) == 0:
            check = True
        sleep(3)
        app.enrollments_main_page.cancel_click
        return check

    def search_by_doc_number(self, app, searched_value, persons_surname, searched_by_option, is_valid_value):
        app.ensure_logout()
        app.login(User.Admin(), True)
        app.internal_page.is_element_present(app.internal_page.SPINNER_OFF)
        app.internal_page.enrollments_page_link.click()
        app.enrollments_page.is_this_page
        app.enrollments_page.add_new_enrollment_button_click
        app.enrollments_main_page.is_this_page
        app.enrollments_main_page.search_person_by(searched_by_option)
        app.enrollments_main_page.set_search_person_by(searched_value)
        app.enrollments_main_page.ok_for_input_field
        all_found_persons_pib = app.enrollments_main_page.get_all_found_persons_pib()
        check = False
        if is_valid_value and len(all_found_persons_pib) > 0:
            for pib in all_found_persons_pib:
                if pib.text.__contains__(persons_surname):
                    check = True
                else:
                    check = False
                    break
        elif not is_valid_value and len(all_found_persons_pib) == 0:
            check = True
        app.enrollments_main_page.cancel_click
        return check

    def test_search_by_pib_valid(self, app, real_person):
        assert self.search_by_pib_and_surname(app, real_person.second_name_ukr, 0, True)

    def test_search_by_pib_invalid(self, app, values):
        assert self.search_by_pib_and_surname(app, values["search_by"]["invalid_pib"], 0, False)

    def test_search_by_surname_valid(self, app, real_person):
        assert self.search_by_pib_and_surname(app, real_person.surname_ukr, 1, True)

    def test_search_by_surname_invalid(self, app, real_person):
        assert self.search_by_pib_and_surname(app, real_person.second_name_ukr, 1, False)

    def test_search_by_person_id_valid(self, app, values):
        assert self.search_by_person_id(app, values["search_by"]["valid_person_id"], 2, True)

    def test_search_by_person_id_invalid(self, app, values):
        assert self.search_by_person_id(app, values["search_by"]["invalid_person_id"], 2, False)

    def test_search_by_doc_number_valid(self, app, real_person):
        assert self.search_by_doc_number(app, real_person.documents[0].document_case_number, real_person.surname_ukr, 3, True)

    def test_search_by_doc_number_invalid(self, app, values):
        assert self.search_by_doc_number(app, int(values["search_by"]["invalid_document_number"]), values["search_by"]["invalid_pib"], 3, False)