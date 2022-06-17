import time
import pytest
from selenium import webdriver
from conftest import get_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage:
    def test_homepage(self, cookie, get_webdriver):


        hov = WebDriverWait(cookie, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="ui-c9 ui-d0 ui-h3"]')))
        hov.click()
        # hov = cookie.find_element(By.XPATH, '//*[@class="ui-c9 ui-d0 ui-h3"]').click()
        # action = ActionChains(cookie)
        # action.move_to_element(hov).perform()

        time.sleep(3)
        # iframe = cookie.find_element(By.XPATH, '//*[@class="vue-portal-target"]')
        # cookie.switch_to.frame(iframe)

        cookie.switch_to.frame(cookie.find_element(By.XPATH, '//*[@class="vue-portal-target"]'))


        # get_webdriver.find_element(By.XPATH, '//input[@type="phone"]')


        # WebDriverWait(cookie, 10).until(
        # EC.presence_of_element_located((By.XPATH, '//*[@classd=class="bpa0"]')))
 # ui-ca3







