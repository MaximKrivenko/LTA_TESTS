import time

import pytest
import os
import allure
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

load_dotenv()
env_url = os.getenv('URL')
env_username = os.getenv('USERNAME')
env_password = os.getenv('PASSWORD')


@pytest.fixture(scope='session', autouse=True)
def get_chrome_options():
    options = webdriver.ChromeOptions()
    options.set_capability('unhandledPromptBehavior', 'accept')
    #options.add_argument('--no-sandbox')
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    #options.add_argument('--headless=new')
    options.add_argument("--disable-popup-blocking")
    return options


@pytest.fixture(scope='session')
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


@pytest.fixture(scope='session')
def setup(get_webdriver):
    driver = get_webdriver
    driver.get(env_url)
    return driver


@pytest.fixture(scope='session')
def authorization(setup):
    driver = setup
    wait_authorization_window = WebDriverWait(driver, 10, 0.3)
    wait_authorization_window.until(ec.presence_of_element_located((By.CLASS_NAME, 'with-icon.ng-untouched.ng'
                                                                                   '-pristine.ng-valid')))
    username = driver.find_element(By.CLASS_NAME, 'with-icon.ng-untouched.ng-pristine.ng-valid')
    username.send_keys(env_username)
    print('USERNAME PLACED')
    password = driver.find_element(By.XPATH,
                                   '/html/body/app-root/app-auth-screen/app-login-screen/form/div/lta-input['
                                   '2]/label/span[2]/input')
    password.send_keys(env_password)
    print('PASSWORD PLACED')
    button_login = driver.find_element(By.XPATH,
                                       '/html/body/app-root/app-auth-screen/app-login-screen/form/lta-btn/button')
    button_login.click()
    wait = WebDriverWait(driver, 20, 0.5)
    wait.until(ec.url_to_be(f'{env_url}hmi/755'))
    print('LOG IN SUCCESS')
    return driver


@pytest.fixture(scope='session')
def authorization1(setup):
    driver = setup
    wait_authorization_window = WebDriverWait(driver, 10, 0.3)
    wait_authorization_window.until(
        ec.presence_of_element_located((By.CLASS_NAME, 'with-icon.ng-untouched.ng-pristine.ng-valid')))
    username = driver.find_element(By.CLASS_NAME, 'with-icon.ng-untouched.ng-pristine.ng-valid')
    username.send_keys(env_username)
    password = driver.find_element(By.CLASS_NAME, 'with-icon.password.ng-untouched.ng-pristine.ng-valid')
    password.send_keys(env_password)
    button_login = driver.find_element(By.CLASS_NAME, 'btn.primary.lg')
    button_login.click()
    wait = WebDriverWait(driver, 20, 0.5)
    wait.until(ec.url_to_be(f'{env_url}hmi/755'))
    return driver


@pytest.fixture(scope='session')
def models_page(authorization1):
    driver = authorization1
    button_settings = driver.find_element(By.XPATH, '/html/body/app-root/lta-main-page/lta-toolbar/div/div[3]/div['
                                                    '5]/lta-svg-icon')
    button_settings.click()
    wait_settings = WebDriverWait(driver, 10, 0.3)
    wait_settings.until(ec.url_to_be(f'{env_url}conf/settings/main'))
    models_button = driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/lta-menu/aside/nav/ul/li['
                                                  '4]/a')
    models_button.click()
    wait_models = WebDriverWait(driver, 10, 0.3)
    wait_models.until(ec.url_to_be(f'{env_url}conf/models'))
    return driver


@pytest.fixture(scope='session')
def objects_page(authorization1):
    driver = authorization1
    button_settings = driver.find_element(By.XPATH, '/html/body/app-root/app-main-page/toolbar/div/div[3]/div['
                                                    '5]/svg-icon')
    button_settings.click()
    wait = WebDriverWait(driver, 10, 0.3)
    wait_settings = WebDriverWait(driver, 10, 0.3)
    wait_settings.until(ec.url_to_be(f'{env_url}conf/settings/main'))
    objects_button = driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                   '/li[5]/a')
    objects_button.click()
    wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
    return driver

@pytest.fixture(scope='session')
def roles_page(authorization1):
    driver = authorization1
    button_settings = driver.find_element(By.XPATH, '/html/body/app-root/lta-main-page/lta-toolbar/div/div[3]/div['
                                                    '5]/lta-svg-icon')
    button_settings.click()
    wait = WebDriverWait(driver, 10, 0.3)
    wait_settings = WebDriverWait(driver, 10, 0.3)
    wait_settings.until(ec.url_to_be(f'{env_url}conf/settings/main'))
    roles_button = driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/lta-menu/aside/nav/ul/li['
                                                 '2]/a')
    roles_button.click()
    wait.until(ec.url_to_be(f'{env_url}conf/roles'))
    return driver

@pytest.fixture(scope='session')
def users_page(authorization1):
    driver = authorization1
    button_settings = driver.find_element(By.XPATH, '/html/body/app-root/lta-main-page/lta-toolbar/div/div[3]/div['
                                                    '5]/lta-svg-icon')
    button_settings.click()
    wait = WebDriverWait(driver, 10, 0.3)
    wait_settings = WebDriverWait(driver, 10, 0.3)
    wait_settings.until(ec.url_to_be(f'{env_url}conf/settings/main'))
    users_button = driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/lta-menu/aside/nav/ul/li['
                                                 '3]/a')
    users_button.click()
    wait.until(ec.url_to_be(f'{env_url}conf/users'))
    return driver
