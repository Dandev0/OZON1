# в conftest живет конфигурация тестов по типу: chrome options, setup...
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import fake_useragent

@pytest.fixture
def get_chrome_options():
    user_agent = fake_useragent
    options = chrome_options()
    options.add_argument('--enable-cookie-encryption')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1280,720')
    options.add_argument(f"__user-agent={user_agent}")
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.ozon.ru'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver  # в отличии от return возвращает объект-генератор
    # driver.quit()
