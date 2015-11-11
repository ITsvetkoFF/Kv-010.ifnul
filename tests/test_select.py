from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utils.web_elem_utils import dropdown_select_by_index

__author__ = 'max'


def test_01():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)
    driver.get("http://www.ex.ua/")
    s = (By.XPATH, ".//*[@id='menu']/tbody//select")

    elem = driver.find_element(*s)
    print Select(elem).all_selected_options
    dropdown_select_by_index(elem, 2)
    time.sleep(1)
    elem = driver.find_element(*s)
    print Select(elem).all_selected_options
    driver.quit()
