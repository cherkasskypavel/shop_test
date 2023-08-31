from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
class TestShop():

    def test_item_page_contains_basket_button(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(10)
        basket_button_checking = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form'))
        )
        child_element_button_check = browser.find_elements(
            By.CSS_SELECTOR, "#add_to_basket_form button"
        )
        assert len(child_element_button_check) > 0

