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


@pytest.fixture
def cookie(get_webdriver):
    # get_webdriver.add_cookie({"name": "__Secure-access-token",
    #                           "value": "3.104122666.S0NmUPAcQVqh-HJKqY9Ieg.23.l8cMBQAAAABiqg4TC2gY8KN3ZWKrNzk4MjQ5MTE1ODIAgJCg.20220615145350.20220615185131.XoBcHy1VXBAKkW18tYyAbQVBJBvEaWHkKYJcJSJUQsk",
    #                           "domain": ".ozon.ru", "path": "/", "size": "181"})
    # get_webdriver.add_cookie(
    #     {"name": "__Secure-user-id", "value": "104122666", "domain": ".ozon.ru", "path": "/", "size": "25"})
    get_webdriver.add_cookie(
        {"name": "__Secure-ab-group", "value": "23", "domain": ".ozon.ru", "path": "/", "size": "19"})
    # get_webdriver.add_cookie({"name": "__Secure-refresh-token",
    #                           "value": "3.104122666.S0NmUPAcQVqh-HJKqY9Ieg.23.l8cMBQAAAABiqg4TC2gY8KN3ZWKrNzk4MjQ5MTE1ODIAgJCg.20220615145350.20220615185131.e9OfTdBaxt1cUFUhSIAjUU5INrapezc5P-Kweep5Cys",
    #                           "domain": ".ozon.ru", "path": "/", "size": "182"}) - мб куки пользователя
    # get_webdriver.add_cookie(
    #     {"name": "__Secure-ext_xcid", "value": "532d465b45ed9eb5f79ff542488ad647", "domain": ".ozon.ru", "path": "/",
    #      "size": "49"})
    # get_webdriver.add_cookie({"name": "isFromYandex", "value": "true", "domain": ".ozon.ru", "path": "/", "size": "16"})
    # get_webdriver.add_cookie(
    #     {"name": "xcid", "value": "532d465b45ed9eb5f79ff542488ad647", "domain": "www.ozon.ru", "path": "/",
    #      "size": "36"})
    # get_webdriver.add_cookie({"name": "AREA_ID", "value": "25949", "domain": "www.ozon.ru", "path": "/", "size": "12"})
    get_webdriver.add_cookie({"name": "__cf_bm",
                              "value": "_oYcBXdnqm5PwCRBCUYNheoFsHWguLypN0_yYRk_1oA-1655311854-0-AewQGEYoHaq4aANveQVfuIYlWyC9uEI0I7f/yUza3KT3BdutxmCe8WDMXZncHTQTWHOuaIO0H13Zx71QaMETI20=",
                              "domain": ".ozon.ru", "path": "/", "size": "152"})
    return get_webdriver
