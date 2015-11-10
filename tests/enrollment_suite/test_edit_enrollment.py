# /coding=utf-8
import datetime
import allure
from allure.constants import AttachmentType
from selenium.common.exceptions import NoSuchElementException

import pytest
from utils.enrollment_creator import EnrollmentCreator

__author__ = 'Vadym'

class TestEditEnrollment(object):

    speciality_id = ""
    DataProvider_filter_to_find_enrollment = "124988"

    @pytest.fixture
    def enrollment(request):
        """
        Fixture create model of enrollment
        :return: Model of Enrollment
        """
        return EnrollmentCreator("enrollment_edit_test.json").get_enrollment()

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_open_enrollment_with_filter(self, logout_login):
        with pytest.allure.step('Authorize to the application and click enrollment page edit enrollment button by filter'):
            app = logout_login
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("Trying to find enrollment by filtering variable 'DataProvider_filter_to_find_enrollment'"):
            app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["document_number"], TestEditEnrollment.DataProvider_filter_to_find_enrollment)
            try:
                app.enrollments_page.edit_button_on_first_row_click()
            except NoSuchElementException:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise
        with pytest.allure.step('Assert the text Редагування заяви on the page'):
            try:
                assert app.enrollments_main_page.get_text_add_enrollment().text == u"Редагування заяви"
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_edit_enrollment(self, app, enrollment):
        with pytest.allure.step('Search person to add enrollment'):
            app.enrollments_main_page.add_person_in_enrollment(enrollment.person_name)
        with pytest.allure.step('Fill data on the add enrollment page'):
            app.enrollments_main_page.emulation_of_input(app.enrollments_main_page.SERIES_OF_STATEMENTS, enrollment.series_of_statements)
            app.enrollments_main_page.emulation_of_input(app.enrollments_main_page.NUMBER_STATEMENTS, enrollment.number_statements)
            # save edited number_statement. We will use this value for filtering and find the edited enrollment
            TestEditEnrollment.DataProvider_filter_to_find_enrollment = str(enrollment.number_statements)
            app.enrollments_main_page.click_all_checkbox(enrollment.checkbox_is_state,
                                    enrollment.checkbox_is_contract,
                                    enrollment.checkbox_is_privilege,
                                    enrollment.checkbox_is_hostel,
                                    enrollment.checkbox_document_is_original)
            app.enrollments_main_page.radiobutton_higher_education(enrollment.radiobutton_higher_education)
            app.enrollments_main_page.radiobutton_evaluation_of_the_interview(enrollment.radiobutton_evaluation_of_the_interview)
        with pytest.allure.step('Search and choose proposition of speciality for person'):
            app.enrollments_main_page.search_offers(enrollment.offers, enrollment.form_of_education)
            # save edited speciality_id. We will use this value for assert actual (edited) speciality_id with this value
            TestEditEnrollment.speciality_id = app.enrollments_main_page.find_first_specialities_id().text
            app.enrollments_main_page.choose_first_specialties.click()
        with pytest.allure.step('Choose document to attach to the enrollment'):
            try:
                app.enrollments_main_page.choose_document(enrollment.document)
            except Exception:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise
        with pytest.allure.step('Fill other data after choose document on the add enrollment page'):
            app.enrollments_main_page.choose_grading_scale(enrollment.grading_scale)
            app.enrollments_main_page.add_total_score(app.enrollments_main_page.TOTAL_SCORE, enrollment.total_score)
            app.enrollments_main_page.add_priority(app.enrollments_main_page.PRIORITY, enrollment.priority)
            app.enrollments_main_page.choose_structural_unit(enrollment.structural_unit)
            app.enrollments_main_page.type_of_entry(enrollment.type_of_entry)
            app.enrollments_main_page.specification_of_entry(enrollment.detailing_start)
        with pytest.allure.step('Choose beginning and closing dates on the add enrollment page'):
            app.enrollments_main_page.set_date(app.enrollments_main_page.DATE_OF_ENTRY_STATEMENTS, enrollment.date_of_entry)
            app.enrollments_main_page.set_date(app.enrollments_main_page.DATE_CLOSING_STATEMENTS, enrollment.date_closing)
            app.enrollments_main_page.is_element_present(app.enrollments_main_page.SPINNER_OFF)
        with pytest.allure.step('Save data on the add enrollment page'):
            app.enrollments_main_page.button_save.click()
        with pytest.allure.step('Assert the text after save enrollment Заяви on the page'):
            try:
                assert app.enrollments_main_page.get_text_add_enrollment().text == u"Заяви"
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_open_edited_enrollment_with_filter(self, logout_login):
        with pytest.allure.step('Authorize to the application and click enrollment page edit enrollment button by filter'):
            app = logout_login
            app.internal_page.enrollments_page_link.click()
            app.enrollments_page.is_this_page
        with pytest.allure.step("Trying to find enrollment by filtering edited variable 'DataProvider_filter_to_find_enrollment' (we changed this value when we were editing enrollmnet)"):
            app.enrollments_page.search_enrollment(app.enrollments_page.SEARCH_METHOD["document_number"], TestEditEnrollment.DataProvider_filter_to_find_enrollment)
            try:
                app.enrollments_page.edit_button_on_first_row_click()
            except NoSuchElementException:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise
        with pytest.allure.step('Assert the text Редагування заяви on the page'):
            try:
                assert app.enrollments_main_page.get_text_add_enrollment().text == u"Редагування заяви"
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_edited_person_in_enrollment(self, app, enrollment):
        with pytest.allure.step('Assert current person FIO with expected'):
            actual_person_in_enrollment = app.enrollments_main_page.person_fio_already_added_view().text
            try:
                assert actual_person_in_enrollment == enrollment.person_name
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_serial_and_number_enrollment(self, app, enrollment):
        with pytest.allure.step('Assert serial and number enrollment'):
            field_serial_of_enroll = app.enrollments_main_page.find_series_of_statements()
            field_number_of_enroll = app.enrollments_main_page.find_number_statements()
            actual_value_serial_enollment = app.driver.execute_script("return angular.element(arguments[0]).scope().enrolment.docSeries", field_serial_of_enroll)
            actual_value_number_enollment = app.driver.execute_script("return angular.element(arguments[0]).scope().enrolment.docNum", field_number_of_enroll)
            try:
                assert actual_value_serial_enollment == enrollment.series_of_statements
                assert actual_value_number_enollment == str(enrollment.number_statements)
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_all_checkboxes(self, app, enrollment):
        with pytest.allure.step('Assert all checkboxes'):
            is_state_checked = self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_state())
            is_contract_checked = self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_contract())
            is_privilege_checked = self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_privilege())
            is_hostel_checked = self.is_checkbox_checked(app.enrollments_main_page.find_checkbox_is_hostel())
            document_is_original = self.is_checkbox_checked(app.enrollments_main_page.checkbox_document_is_original)
            try:
                assert enrollment.checkbox_is_state == is_state_checked
                assert enrollment.checkbox_is_contract == is_contract_checked
                assert enrollment.checkbox_is_privilege == is_privilege_checked
                assert enrollment.checkbox_is_hostel == is_hostel_checked
                assert enrollment.checkbox_document_is_original == document_is_original
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_edited_suggestion(self, app):
        with pytest.allure.step('Assert added before speciality id with actual'):
            try:
                assert str(TestEditEnrollment.speciality_id) == app.enrollments_main_page.find_first_specialities_id_in_view_table().text
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_document(self, app, enrollment):
        with pytest.allure.step('Assert the document of person'):
            actual_value_document_text = app.enrollments_main_page.get_document_title().text
            try:
                assert actual_value_document_text == enrollment.document
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_total_score_and_scale_enrollment(self, app, enrollment):
        with pytest.allure.step('Assert total score and scale enrollment'):
            field_total_score = app.enrollments_main_page.find_total_score()
            scale = app.enrollments_main_page.get_text_choose_grading_scale().text
            actual_value_total_score = app.driver.execute_script("return angular.element(arguments[0]).scope().enrolment.mark", field_total_score)
            try:
                assert actual_value_total_score == enrollment.total_score
                assert scale == enrollment.grading_scale
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_priority_enrollment(self, app, enrollment):
        with pytest.allure.step('Assert priority'):
            field_priority = app.enrollments_main_page.get_priority()
            actual_value_priority = app.driver.execute_script("return angular.element(arguments[0]).scope().enrolment.priority", field_priority)
            try:
                assert actual_value_priority == enrollment.priority
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_structural_unit_enrollment(self, app, enrollment):
        with pytest.allure.step('Assert structural unit'):
            actual_value_structural_unit = app.enrollments_main_page.get_structural_unit_text().text
            try:
                assert actual_value_structural_unit == enrollment.structural_unit
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_type_of_entry_and_detailing_start_enrollment(self, app, enrollment):
        with pytest.allure.step('Assert type of entry and datailing start of fields'):
            field_type_of_entry = app.enrollments_main_page.get_type_of_entry()
            field_detailing_start = app.enrollments_main_page.get_detailing_start_menu()
            actual_value_type_of_entry = app.driver.execute_script("var dummy_scope = angular.element(arguments[0]).scope(); return dummy_scope.chiefEnrolTypes[dummy_scope.enrolmentTypes.chiefs-1].name", field_type_of_entry)
            actual_value_detailing_start = app.driver.execute_script("var res; var outer_scope = angular.element(arguments[0]).scope(); var ar= outer_scope.childEnrolTypes; ar.forEach(function(obj) {if (obj.id == outer_scope.enrolmentTypeId){res = obj};}); return res.name", field_detailing_start)
            try:
                assert actual_value_type_of_entry == enrollment.type_of_entry
                assert actual_value_detailing_start == enrollment.detailing_start
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_verify_date_of_entry_closing_enrollment(self, app, enrollment):
        with pytest.allure.step('Assertdate of entry and closing of enrollment'):
            actual_value_date_of_entry = app.enrollments_main_page.find_date_of_begining().get_attribute("value")
            actual_value_date_of_closing = app.enrollments_main_page.find_date_of_ending().get_attribute("value")
            try:
                assert actual_value_date_of_entry == str(enrollment.date_of_entry)
                assert actual_value_date_of_closing == str(enrollment.date_closing)
            except AssertionError:
                allure.attach('screenshot', app.enrollments_page.driver.get_screenshot_as_png(), type=AttachmentType.PNG)
                raise

    def is_checkbox_checked(self, checkbox):
        if checkbox.get_attribute("checked"):
            return True
        return False




#     {
#   "enrollment":
#   {
#       "person_name": "Комаров Володимир Михайлович",
#       "series_of_statements": "ТЦ",
#       "number_statements": 789654,
#       "radiobutton_higher_education": "Є вища освіта",
#       "radiobutton_evaluation_of_the_interview": "Не пройшов співбесіду",
#       "checkbox_is_state": true,
#       "checkbox_is_contract": false,
#       "checkbox_is_privilege": true,
#       "checkbox_is_hostel": true,
#       "checkbox_document_is_original": true,
#       "offers": "Фізичний",
#       "form_of_education": "Бакалавр",
#       "document": "Атестат про повну загальну середню освіту",
#       "grading_scale": "двохсотбальна",
#       "total_score": 250,
#       "priority": 3,
#       "structural_unit": "Фізичний",
#       "type_of_entry": "За результатами іспитів",
#       "detailing_start": "Учасник міжнародної олімпіади",
#       "date_of_entry":
#       {
#           "day":17,
#           "month":10,
#           "year":2016
#       },
#       "date_closing":
#       {
#           "day":21,
#           "month":11,
#           "year":2017
#       }
#   }
# }