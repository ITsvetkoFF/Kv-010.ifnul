from time import sleep
import pytest
from model.person import Person

__author__ = 'stako'


def test_example_execute_js(logout_login):
    expected_person = Person()
    app = logout_login
    app.persons_page.edit_first_person_in_page.click()
    app.person_base_page.click_papers_tab()
    app.papers_page.read_in_document_page(app, expected_person)
    sleep(3)
    assert True
