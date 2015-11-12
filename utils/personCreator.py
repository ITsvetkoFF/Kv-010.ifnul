import os

__author__ = 'odeortc'

import json
from model.person import Person
from model.person import Document
import datetime


class PersonCreator(object):
    def __init__(self, file):
        self.file = file

    def person_file(self):
        project_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.normpath(os.path.abspath(project_path) + "/../resources/" + self.file)
        return path

    def parseJson(self):
        fl = open(self.person_file(), 'r')
        st = fl.read()
        fl.close()
        person_json = json.loads(st)
        return person_json["person"]

    def create_person_from_json(self):
        person = Person()
        json_person = self.parseJson()
        person.person_type = json_person["person_type"]
        person.surname_ukr = json_person["surname_ukr"]
        person.first_name_ukr = json_person["first_name_ukr"]
        person.second_name_ukr = json_person["second_name_ukr"]
        person.surname_eng = json_person["surname_eng"]
        person.first_name_eng = json_person["first_name_eng"]
        person.birth_day = datetime.date(json_person["birth_day"]["year"],
                                         json_person["birth_day"]["month"],
                                         json_person["birth_day"]["day"])
        person.sex = json_person["sex"]
        person.marital_status = json_person["marital_status"]
        person.nationality = json_person["nationality"]
        person.private_case_chars = json_person["private_case_chars"]
        person.private_case_number = json_person["private_case_number"]
        person.is_outlander = json_person["is_outlander"]
        person.reservist = json_person["reservist"]
        person.hostel_need = json_person["hostel_need"]
        person.burn_place = json_person["burn_place"]
        person.registration_place = json_person["registration_place"]
        person.post_registration_place = json_person["post_registration_place"]
        person.photo = json_person["photo"]
        person.mobile_phone1 = json_person["mobile_phone1"]
        person.mobile_phone2 = json_person["mobile_phone2"]
        person.home_phone = json_person["home_phone"]
        person.work_phone = json_person["work_phone"]
        person.email = json_person["email"]
        person.skype = json_person["skype"]
        person.web_site = json_person["web_site"]
        person.icq = json_person["icq"]
        for doc in json_person["documents"]:
            document = Document()
            document.category = doc["category"]
            document.document_name = doc["document_name"]
            document.document_case_char = doc["document_case_char"]
            document.document_case_number = doc["document_case_number"]
            document.day_of_issue = datetime.date(doc["day_of_issue"]["year"],
                                                  doc["day_of_issue"]["month"],
                                                  doc["day_of_issue"]["day"])
            document.issued_by = doc["issued_by"]
            document.document_is_original = doc["document_is_original"]
            document.document_is_foreign = doc["document_is_foreign"]
            document.category_reward = doc["category_reward"]
            document.reward = doc["reward"]
            document.type_of_reward = doc["type_of_reward"]
            document.average_rate = doc["average_rate"]
            document.pincode = doc["pincode"]
            person.documents.append(document)
        return person

    def create_readom_person(self):
        person = Person()

        return person
