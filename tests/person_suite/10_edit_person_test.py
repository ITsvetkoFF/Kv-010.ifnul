# -*- coding: utf-8 -*-
import pytest
from model.person import Person

__author__ = 'stako'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
def test_edit_person(logout_login, person_for_edit, screenshot):
    with pytest.allure.step('Testing of edit person.'):
        expected_person = person_for_edit
        app = logout_login
        id_of_person_in_first_row = app.persons_page.id_of_person_in_first_row().text
        app.persons_page.edit_first_person_in_page.click()
        edit_person(app, expected_person)
        app.persons_page.search_person_by_id(id_of_person_in_first_row)
        # this variable changes unicode because there is invisible mistake in web application
        expected_person.post_registration_place["type"] = expected_person.post_registration_place["type"].encode('cp1251')
        app.persons_page.edit_first_person_in_page.click()
        actual_person = create_a_person_according_to_the_received_data_from_the_edited_person(app)
        list_with_not_matching_fields = compare_fields_of_persons(expected_person, actual_person)
        if len(list_with_not_matching_fields) is not 0:
            for field in list_with_not_matching_fields:
                print field
        screenshot.assert_and_get_screenshot(app, len(list_with_not_matching_fields) == 0)


def compare_fields_of_persons(expected_person, actual_person):
    """
    This method compares all fields in two person one by one.
    :param expected_person: expected person
    :param actual_person: actual person
    :return: list with values do not match.
    """
    list_with_not_matching_fields = []
    dict_keys = expected_person.__dict__.keys()
    for key in dict_keys:
        if not expected_person.__dict__[key] == actual_person.__dict__[key]:
            list_with_not_matching_fields.append(
            "In persons field \'" + key + "\' is different: expected field = " + str(expected_person.__dict__[key]) + \
            " : actual field = " + str(actual_person.__dict__[key]))
    return list_with_not_matching_fields


def edit_person(app, actual_person):
    """
    This method edits person.
    :param app:
    :param actual_person: person with data for edition.
    """
    base_page = app.person_base_page
    with pytest.allure.step('Fill data on the main person page'):
        app.person_main_page.fill_in_main_person_page(actual_person)
        base_page.click_extra_tab()
    with pytest.allure.step('Fill data on the extra person page'):
        app.extra_page.fill_in_extra_person_page(actual_person)
        base_page.click_addresses_tab
    with pytest.allure.step('Fill data on the address person page'):
        app.address_page.fill_in_address_page(actual_person)
        base_page.click_contacts_tab
    with pytest.allure.step('Fill data on the contacts person page'):
        app.contact_page.fill_in_contact_page(actual_person)
        base_page.click_papers_tab
    with pytest.allure.step('Fill data on the documents person page'):
        app.papers_page.fill_in_document_page(actual_person)
        base_page.save_new_person()


def create_a_person_according_to_the_received_data_from_the_edited_person(app):
    """
    This method views all edited fields and creates the person by this data.
    :param app:
    """
    expected_person = Person()
    base_page = app.person_base_page
    with pytest.allure.step('Add info in new person from the main person page'):
        expected_person = add_info_in_person_from_person_main_page(app, expected_person)
        base_page.click_extra_tab()
    with pytest.allure.step('Add info in new person from the extra person page'):
        expected_person = add_info_in_person_from_person_extra_page(app, expected_person)
        base_page.click_addresses_tab
    with pytest.allure.step('Add info in new person from the address person page'):
        expected_person = add_info_in_person_from_person_address_page(app, expected_person)
        base_page.click_contacts_tab
    with pytest.allure.step('Add info in new person from the contacts person page'):
        expected_person = add_info_in_person_from_person_contact_page(app, expected_person)
        base_page.click_papers_tab
    with pytest.allure.step('Add info in new person from the documents person page'):
        expected_person = add_info_in_person_from_person_document_page(app, expected_person)
        app.internal_page.persons_page_link
    return expected_person


def add_info_in_person_from_person_main_page(app, person_new):
    return app.person_main_page.read_in_main_person_page(person_new)


def add_info_in_person_from_person_extra_page(app, person_new):
    return app.extra_page.read_in_extra_person_page(person_new)


def add_info_in_person_from_person_address_page(app, person_new):
    return app.address_page.read_in_address_page(person_new)


def add_info_in_person_from_person_contact_page(app, person_new):
    return app.contact_page.read_in_contact_page(person_new)


def add_info_in_person_from_person_document_page(app, person_new):
    return app.papers_page.read_in_document_page(person_new)
