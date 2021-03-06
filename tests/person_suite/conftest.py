import pytest
from utils.personCreator import PersonCreator

__author__ = 'stako'


@pytest.fixture(scope="session")
def person(dictionary_with_json_files):
    create_person = PersonCreator(dictionary_with_json_files["person"])
    #create_person = PersonCreator(dictionary_with_json_files["existing_person"])
    person = create_person.create_person_from_json()
    return person


@pytest.fixture(scope="session")
def person_for_edit(dictionary_with_json_files):
    create_person = PersonCreator(dictionary_with_json_files["person_for_edit"])
    person = create_person.create_person_from_json()
    return person


@pytest.fixture(scope="session")
def invalid_person(dictionary_with_json_files):
    create_person = PersonCreator(dictionary_with_json_files["person_incorrect"])
    person = create_person.create_person_from_json()
    return person

