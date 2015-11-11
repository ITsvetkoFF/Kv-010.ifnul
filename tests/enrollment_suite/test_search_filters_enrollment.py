# -*- coding: utf-8 -*-

from allure.constants import AttachmentType
from datetime import time
import pytest
import allure
import sys
import traceback

__author__ = 'Evgen'


class TestSearchFilters(object):

    DataProvider = {
        'filter_id' : '4',
        'filter_document_series' : 'MR',
        'filter_number_document' : '457895',
        'filter_proposal_id' : '71',
    }

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_search_by_person_id(self, app):
        with pytest.allure.step("Authorize on the site with admin credentials"):
            app.ensure_logged_in()
            app.internal_page.is_this_page()
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page()
        with pytest.allure.step("Searching by person ID"):
            en_page = app.enrollments_page
            expected_id = TestSearchFilters.DataProvider['filter_id']
            actual_search = en_page.search_enrollment(en_page.SEARCH_METHOD["person_id"], expected_id)
            try:
                assert expected_id in actual_search
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_search_by_document_series(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's series"):
            expected_document_series = TestSearchFilters.DataProvider['filter_document_series']
            actual_search = en_page.search_enrollment(en_page.SEARCH_METHOD["document_series"], expected_document_series)
            try:
                assert expected_document_series in actual_search
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_search_by_document_number(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by document's number"):
            expected_number_document = TestSearchFilters.DataProvider['filter_number_document']
            actual_search = en_page.search_enrollment(en_page.SEARCH_METHOD["document_number"], expected_number_document)
            try:
                assert expected_number_document in actual_search
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_search_by_proposal_id(self, app):
        en_page = app.enrollments_page
        with pytest.allure.step("Searching by proposal ID"):
            expected_proposal_id = TestSearchFilters.DataProvider['filter_proposal_id']
            actual_search_results = en_page.search_enrollment(en_page.SEARCH_METHOD["proposal_id"], expected_proposal_id)
            try:
                assert expected_proposal_id in actual_search_results
            except AssertionError:
                allure.attach('screenshot', en_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_filter_by_budget(self, logout_login):
        app = logout_login
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page()
        with pytest.allure.step("Add budget column"):
            enr_page = app.enrollments_page
            enr_page.add_table_columns(enr_page.COLUMN_BUDGET_ADD)
        with pytest.allure.step("In the filters section click on budget filter"):
            enr_page.add_filters(enr_page.FILTER_BUDGET)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.BUDGET_COLUMN)
            expected = {enr_page.FILTER_RESULTS["budget"]}
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_filter_by_not_budget(self, logout_login):
        app = logout_login
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page()
        with pytest.allure.step("In the filters section add not budget filter"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NOT_BUDGET)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.BUDGET_COLUMN)
            expected = {enr_page.FILTER_RESULTS["not_budget"]}
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_filter_by_privileges(self, logout_login):
        app = logout_login
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page()
        with pytest.allure.step("In the filters section add privileges filter"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_PRIVILEGES)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN)
            expected = {enr_page.FILTER_RESULTS["privileged"]}
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_filter_by_not_privileges(self, logout_login):
        app = logout_login
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page()
        with pytest.allure.step("In the filters section add not privileges filter"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NOT_PRIVILEGES)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN)
            expected = {enr_page.FILTER_RESULTS["not_privileged"]}
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_filter_mix(self, logout_login):
        app = logout_login
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page()
        with pytest.allure.step("In the filters section add necessary filters"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NOT_PRIVILEGES, enr_page.FILTER_BUDGET,
                                 enr_page.FILTER_NEED_ACCOMMODATION)
        with pytest.allure.step("Check the results"):
            actual = enr_page.get_columns_text(enr_page.PRIVILEGES_COLUMN, enr_page.BUDGET_COLUMN,
                                               enr_page.ACCOMMODATION_COLUMN)
            expected = {enr_page.FILTER_RESULTS["not_privileged"], enr_page.FILTER_RESULTS["budget"],
                        enr_page.FILTER_RESULTS["accommodation"]}
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_delete_filters(self, logout_login):
        app = logout_login
        with pytest.allure.step("Go to enrollments page"):
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page()
        with pytest.allure.step("In the filters section add necessary filters"):
            enr_page = app.enrollments_page
            enr_page.add_filters(enr_page.FILTER_NEED_ACCOMMODATION, enr_page.FILTER_BUDGET, enr_page.FILTER_CONTRACT)
        with pytest.allure.step("Delete all the filters"):
            enr_page.delete_all_filters()
        with pytest.allure.step("Check the results"):
            actual = len(enr_page.driver.find_elements(*enr_page.DELETE_FILTER_BUTTON))
            expected = 0
            try:
                assert actual == expected
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
            except AssertionError:
                allure.attach('screenshot', enr_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                self.print_simple_stacktrace()
                raise

    def print_simple_stacktrace(self):
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)
        filename, line, func, text = tb_info[-1]
        print('An error occurred on line: {}, in statement: {}. The filename is: {}, and function is: {}.'
              .format(line, text, filename, func))
