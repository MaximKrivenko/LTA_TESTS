import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def setup(get_webdriver):
    driver = get_webdriver
    driver.get('http://185.221.152.176/')
    return driver


@pytest.fixture(scope='function')
def authorization(setup):
    driver = setup
    username = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-auth-screen/app-login-screen/form/div/lta-input[1]/label/span[2]/input')
    username.send_keys('admin')
    print('USERNAME PLACED')
    password = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-auth-screen/app-login-screen/form/div/lta-input[2]/label/span[2]/input')
    password.send_keys('admin')
    print('PASSWORD PLACED')
    button_login = driver.find_element(By.XPATH,
                                       '/html/body/app-root/app-auth-screen/app-login-screen/form/lta-btn/button')
    button_login.click()
    wait = WebDriverWait(driver, 20, 0.5)
    wait.until(ec.url_to_be('http://185.221.152.176/hmi/17'))
    print('LOG IN SUCCESS')
    return driver

@pytest.fixture(scope='function')
def authorization1(setup):
    driver = setup
    username = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-auth-screen/app-login-screen/form/div/lta-input[1]/label/span[2]/input')
    username.send_keys('admin')
    password = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-auth-screen/app-login-screen/form/div/lta-input[2]/label/span[2]/input')
    password.send_keys('admin')
    button_login = driver.find_element(By.XPATH,
                                       '/html/body/app-root/app-auth-screen/app-login-screen/form/lta-btn/button')
    button_login.click()
    wait = WebDriverWait(driver, 15, 0.5)
    wait.until(ec.url_to_be('http://185.221.152.176/hmi/17'))
    return driver

@pytest.fixture
def models_page(authorization1):
    driver = authorization1
    button_settings = driver.find_element(By.XPATH, '/html/body/app-root/app-main-page/toolbar/div/div['
                                                    '3]/div[4]/svg-icon')
    button_settings.click()
    wait_settings = WebDriverWait(driver, 10, 0.3)
    wait_settings.until(ec.url_to_be('http://185.221.152.176/conf/settings/figma'))
    models_button = driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                  '/nav/ul/li[5]/a')
    models_button.click()
    wait_models = WebDriverWait(driver, 10, 0.3)
    wait_models.until(ec.url_to_be('http://185.221.152.176/conf/data/models'))
    return driver
