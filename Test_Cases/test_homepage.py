import time

import pytest
import allure
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()
env_url = os.getenv('URL')

class TestHomepage:
    print(f'TEST HOMEPAGE LAUNCHED ON {env_url}')

    @allure.description("Проверка работоспособности главной страницы")
    def test_homepage(self, authorization):
        self.driver = authorization
        print('URL REACHED')
        wait_homepage = WebDriverWait(self.driver, 15, 0.5)
        wait_homepage.until(ec.presence_of_element_located((By.XPATH, "//*[@id='background']")))
        menu = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-page/toolbar/div/div[4]')
        assert menu.text == "Меню", 'Title is missing, HOMEPAGE IS NOT ACTIVE'
        print('HOMEPAGE IS ACTIVE')

    def test_homepage2(self, setup):
        self.driver = setup
        print('URL REACHED TWICE')
        time.sleep(5)
        self.driver.refresh()
        wait_homepage = WebDriverWait(self.driver, 15, 0.5)
        wait_homepage.until(ec.presence_of_element_located((By.XPATH, "//*[@id='background']")))
        button_settings = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-page/toolbar/div/div[3]/div['
                                                        '5]/svg-icon')
        button_settings.click()
        wait_settings = WebDriverWait(self.driver, 10, 0.3)

        self.driver.switch_to.window(self.driver.window_handles[1])

        wait_settings.until(ec.url_to_be(f'{env_url}conf/settings/figma'))
        time.sleep(5)
        self.driver.close()
