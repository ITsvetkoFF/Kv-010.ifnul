# coding: utf8
import allure
from allure.constants import AttachmentType
import pytest
from utils.add_person_pattern import AddPersonPattern

__author__ = 'Denys'


@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
@pytest.mark.usefixtures('pre_login')
class TestSearchPerson:
    def test_surname_search(self, person):
        try:
            with pytest.allure.step("Prepare Data"):
                add_person_pattern = AddPersonPattern()
                add_person_pattern.search_person_by_surname(self.app, person.surname_ukr)
            with pytest.allure.step("Check Data"):
                assert self.app.persons_page.try_get_searched_surname(person.surname_ukr).text.partition(' ')[
                           0] == person.surname_ukr
        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_person_id_search(self):
        try:
            with pytest.allure.step("Prepare Data"):
                person_page = self.app.persons_page
                person_page.try_get_choose_person_id().click()
                person_page.try_get_input_group().clear()
                id = person_page.try_get_id_for_search().text
                person_page.try_get_input_group().send_keys(id)
                person_page.try_get_ok_button().click()
            with pytest.allure.step("Check Data"):
                assert person_page.try_get_searched_person_id(id).text == id

        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_num_os_search(self, person):
        try:
            with pytest.allure.step("Prepare Data"):
                person_page = self.app.persons_page
                person_page.try_get_choose_num_os().click()
                person_page.try_get_input_group().clear()
                person_page.try_get_input_group().send_keys(person.private_case_number)
                person_page.try_get_ok_button().click()
            with pytest.allure.step("Check Data"):
                assert person_page.try_get_searched_num_os(str(person.private_case_number)).text == str(person.private_case_number)
        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    def test_series_os_search(self, person):
        try:
            with pytest.allure.step("Prepare Data"):
                person_page = self.app.persons_page
                person_page.try_get_choose_series_os().click()
                person_page.try_get_input_group().clear()
                person_page.try_get_input_group().send_keys(person.private_case_chars)
                person_page.try_get_ok_button().click()
            with pytest.allure.step("Check Data"):
                assert person_page.try_get_searched_series_os(person.private_case_chars).text == person.private_case_chars
        except Exception:
            allure.attach('screenshot', self.app.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise
