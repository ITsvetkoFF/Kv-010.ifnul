__author__ = 'Evgen'
import pytest
from model.user import User
from selenium.webdriver.common.keys import Keys


def test_valid_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()


def test_remember_me_checkbox(app):
    app.ensure_logout()
    app.login(User.Admin(), True)
    ip = app.internal_page
    main_window_handle = ip.driver.current_window_handle
    body = ip.driver.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 'n')
    ip.driver.switch_to.window(main_window_handle)
    all_windows = ip.driver.window_handles
    ip.driver.close()
    ip.driver.switch_to.window(all_windows[1])
    ip.driver.get("http://localhost:9000/#/add/list")
    assert app.is_logged_in()


def test_invalid_login(app):
    app.ensure_logout()
    app.login(User.random())
    assert app.is_not_logged_in()
