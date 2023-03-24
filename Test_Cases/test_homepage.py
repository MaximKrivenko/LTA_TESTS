import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestHomepage:
    def test_homepage(self, authorization):
        self.driver = authorization
        print('URL REACHED')
        wait_homepage = WebDriverWait(self.driver, 15, 0.5)
        wait_homepage.until(ec.presence_of_element_located((By.XPATH, "//*[@id='background']")))
        menu = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-page/toolbar/div/div[4]')
        assert menu.text == "Меню", 'Title is missing, HOMEPAGE IS NOT ACTIVE'
        print('HOMEPAGE IS ACTIVE')
        self.driver.quit()