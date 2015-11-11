import pytest
from utils.web_elem_utils import  get_text_from_select


@pytest.mark.usefixtures('stand_for_dictionary_tests')
class Test_01(object):
    def test_01(self):
        self.app.internal_page.persons_page_link.click()
        self.app.internal_page.wait_until_page_generate()
        self.app.persons_page.edit_first_person_in_page.click()
        self.app.persons_page.wait_until_page_generate()
        self.app.person_base_page.click_addresses_tab()
        print get_text_from_select(self.app.address_page.address_type_chooser())


