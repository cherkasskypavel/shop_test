import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print('\nоткрываем хром\n')
    browser = webdriver.Chrome()
    yield browser
    print('\nзакрываем хром\n')
    browser.close()
