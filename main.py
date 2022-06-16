import time
import pickle
import pytest
from selenium import webdriver
from conftest import get_webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup')
class TestHomepage:
    def test_homepage(self, get_webdriver):
        time.sleep(1)
        get_webdriver.add_cookie({"name": "__Secure-access-token",
                                  "value": "3.104122666.S0NmUPAcQVqh-HJKqY9Ieg.23.l8cMBQAAAABiqg4TC2gY8KN3ZWKrNzk4MjQ5MTE1ODIAgJCg.20220615145350.20220615185131.XoBcHy1VXBAKkW18tYyAbQVBJBvEaWHkKYJcJSJUQsk", "domain":".ozon.ru", "path":"/", "size":"181"})
        get_webdriver.add_cookie(
             {"name": "__Secure-user-id", "value": "104122666", "domain":".ozon.ru", "path":"/", "size":"25"})
        get_webdriver.add_cookie({"name":"__Secure-ab-group", "value":"23", "domain":".ozon.ru", "path":"/", "size":"19"})
        get_webdriver.add_cookie({"name":"__Secure-refresh-token", "value":"3.104122666.S0NmUPAcQVqh-HJKqY9Ieg.23.l8cMBQAAAABiqg4TC2gY8KN3ZWKrNzk4MjQ5MTE1ODIAgJCg.20220615145350.20220615185131.e9OfTdBaxt1cUFUhSIAjUU5INrapezc5P-Kweep5Cys", "domain":".ozon.ru", "path":"/", "size":"182"})
        get_webdriver.add_cookie({"name":"__Secure-ext_xcid", "value":"532d465b45ed9eb5f79ff542488ad647", "domain":".ozon.ru", "path":"/", "size":"49"})
        get_webdriver.add_cookie({"name":"isFromYandex", "value":"true", "domain":".ozon.ru", "path":"/", "size":"16"})
        get_webdriver.add_cookie({"name":"xcid", "value":"532d465b45ed9eb5f79ff542488ad647", "domain":"www.ozon.ru", "path":"/", "size":"36"})
        get_webdriver.add_cookie({"name":"AREA_ID", "value":"25949", "domain":"www.ozon.ru", "path":"/", "size":"12"})
        get_webdriver.add_cookie({"name":"__cf_bm", "value":"_oYcBXdnqm5PwCRBCUYNheoFsHWguLypN0_yYRk_1oA-1655311854-0-AewQGEYoHaq4aANveQVfuIYlWyC9uEI0I7f/yUza3KT3BdutxmCe8WDMXZncHTQTWHOuaIO0H13Zx71QaMETI20=", "domain":".ozon.ru", "path":"/", "size":"152"})
        time.sleep(8)
        get_webdriver.find_element(By.XPATH, '//*[@class="ui-j9"]').click()
        # time.sleep(10)

        get_webdriver.add_cookie({"name": "__Secure-access-token",
                                  "value": "3.104122666.S0NmUPAcQVqh-HJKqY9Ieg.23.l8cMBQAAAABiqg4TC2gY8KN3ZWKrNzk4MjQ5MTE1ODIAgJCg.20220615145350.20220615185131.XoBcHy1VXBAKkW18tYyAbQVBJBvEaWHkKYJcJSJUQsk",
                                  "domain": ".ozon.ru", "path": "/", "size": "181"})
        get_webdriver.add_cookie(
            {"name": "__Secure-user-id", "value": "104122666", "domain": ".ozon.ru", "path": "/", "size": "25"})
        get_webdriver.add_cookie(
            {"name": "__Secure-ab-group", "value": "23", "domain": ".ozon.ru", "path": "/", "size": "19"})
        get_webdriver.add_cookie({"name": "__Secure-refresh-token",
                                  "value": "3.104122666.S0NmUPAcQVqh-HJKqY9Ieg.23.l8cMBQAAAABiqg4TC2gY8KN3ZWKrNzk4MjQ5MTE1ODIAgJCg.20220615145350.20220615185131.e9OfTdBaxt1cUFUhSIAjUU5INrapezc5P-Kweep5Cys",
                                  "domain": ".ozon.ru", "path": "/", "size": "182"})
        get_webdriver.add_cookie(
            {"name": "__Secure-ext_xcid", "value": "532d465b45ed9eb5f79ff542488ad647", "domain": ".ozon.ru",
             "path": "/", "size": "49"})
        get_webdriver.add_cookie(
            {"name": "isFromYandex", "value": "true", "domain": ".ozon.ru", "path": "/", "size": "16"})
        get_webdriver.add_cookie(
            {"name": "xcid", "value": "532d465b45ed9eb5f79ff542488ad647", "domain": "www.ozon.ru", "path": "/",
             "size": "36"})
        get_webdriver.add_cookie(
            {"name": "AREA_ID", "value": "25949", "domain": "www.ozon.ru", "path": "/", "size": "12"})
        get_webdriver.add_cookie({"name": "__cf_bm",
                                  "value": "_oYcBXdnqm5PwCRBCUYNheoFsHWguLypN0_yYRk_1oA-1655311854-0-AewQGEYoHaq4aANveQVfuIYlWyC9uEI0I7f/yUza3KT3BdutxmCe8WDMXZncHTQTWHOuaIO0H13Zx71QaMETI20=",
                                  "domain": ".ozon.ru", "path": "/", "size": "152"})



        pickle.dump(get_webdriver.get_cookie("Name"), open("cookies1", "wb"))
        print("Запись окончена")




