from time import sleep
from model.user import User


__author__ = 'stako'


def test_add_enrollments(app):
    app.ensure_logout()
    app.login(User.Admin(), True)
    sleep(3)
    app.internal_page.enrollments_page_link.click()
    assert app.enrollments_page.is_this_page
    app.enrollments_page.is_this_page.click()
    app.enrollments_main_page.fill_enrollment()
    app.enrollments_page.search_enrollment_by_doc_number("7778777")





