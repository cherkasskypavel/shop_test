import pytest
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestShop():
    def presence_of_element(self, browser, css_selector=str):
        try:
            elem = WebDriverWait(browser, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            print(f'Текст в элементе: "{elem.text}"')
            return True
        except:
            # print('Элемент отсутствует')
            return False
    def test_item_page_contains_basket_button(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        # time.sleep(30)
        basket_button_checking = self.presence_of_element(browser, '#add_to_basket_form button')
        assert basket_button_checking == True

if __name__ == '__main__':
    pytest.main()