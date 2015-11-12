# coding=utf-8
from datetime import date

__author__ = 'stako'

class Enrollment():
    def __init__(self):
        self.person_name = ""
        self.series_of_statements = ""
        self.number_statements = 0
        self.radiobutton_higher_education = ""
        self.radiobutton_evaluation_of_the_interview = ""
        self.checkbox_is_state = False
        self.checkbox_is_contract = False
        self.checkbox_is_privilege = False
        self.checkbox_is_hostel = False
        self.checkbox_document_is_original = False
        self.offers = ""
        self.form_of_education = ""
        self.document = ""
        self.grading_scale = ""
        self.total_score = 0
        self.priority = 1
        self.structural_unit = ""
        self.type_of_entry = ""
        self.detailing_start = ""
        self.date_of_entry = date(1, 1, 1)
        self.date_closing = date(1, 1, 1)

    def get_day_of_entry_str_for_view(self):
        return self.date_of_entry.strftime("%Y-%m-%d")

    def get_text_hostel_for_view(self, boolean):
        if(boolean == "True"):
            return u'потреб. гуртож.'
        else:
            return u'не потреб. гуртож.'

    def get_text_privilege_for_view(self, boolean):
        if(boolean == "True"):
            return u'є пільги'
        else:
            return u'немає пільг'
