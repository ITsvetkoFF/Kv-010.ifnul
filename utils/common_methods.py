__author__ = 'stako'


class CommonMethods():
    @staticmethod
    def is_checkbox_checked(checkbox):
        if checkbox.get_attribute("checked"):
            return True
        return False
