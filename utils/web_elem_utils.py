from selenium.webdriver.support.select import Select

__author__ = 'dmakstc'


def input_text_in_field(text_field_web_elem, text, by_symbols=True):
    """
    Method emulates one by one symbols input into input form or block text input
    :param text_field_web_elem: textfield to input:
    :param text: message to input:
    :param by_symbols: boolean value(if true input by symbols else insert text block), default = by symbol input
    :return:
    """
    text_field_web_elem.clear()
    if type(text) == int:
        text = str(text)
    if by_symbols:
        for letter in text:
            text_field_web_elem.send_keys(letter)
    else:
        text_field_web_elem.send_keys(text)


def checkbox_set_state(check_box_web_elem, is_checked):
    """
    :param check_box_web_elem: checkbox web element
    :param is_checked: boolean value(true if we want check checkbox else false)
    :return:
    """
    if is_checked:
        if not check_box_web_elem.is_selected():
            check_box_web_elem.click()
    else:
        if check_box_web_elem.is_selected():
            check_box_web_elem.click()


def dropdown_select_by_text(dropdown_web_elem, text):
    """

    :param dropdown_web_elem: select web element
    :param text: text to find in web element
    :return:
    """
    case_value = Select(dropdown_web_elem)
    case_value.select_by_visible_text(text)


def dropdown_select_by_index(dropdown_web_elem, index):
    """

    :param dropdown_web_elem: select web element
    :param text: index of row
    :return:
    """
    case_value = Select(dropdown_web_elem)
    case_value.select_by_index(index)


def is_checkbox_checked(checkbox):
    """
    This method gets the value of checkbox.
    :param checkbox: is the verifiable checkbox.
    :return: the value of checkbox.
    """
    if checkbox.get_attribute("checked"):
        return True
    return False
