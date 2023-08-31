import pytest
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Firefox_Options

#   добавляем опции:
#       - по заданию языка на странице;
#       - по выбору браузера (только хром или файерфокс, хром по умолчанию)
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome (by default) or firefox')

#   в условном операторе объявляем разные Options и webdriver для каждого браузера
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('--browser_name')
    user_language = request.config.getoption('--language')
    if browser_name == 'chrome':
        options = Chrome_Options()
        options.add_experimental_option('prefs', {"intl.accept_languages": user_language})
        print('\nоткрываем хром\n')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = Firefox_Options()
        options.set_preference("intl.accept_languages", user_language)
        print('\nоткрываем файерфокс\n')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nзакрываем браузер\n')
    browser.close()
