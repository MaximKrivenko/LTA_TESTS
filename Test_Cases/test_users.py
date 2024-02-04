import pytest
import time
import random
import allure
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()
env_url = os.getenv('URL')


class TestUser:
    print(f'TEST USERS LAUNCHED ON {env_url}')

    @allure.description("Проверка работоспособности раздела 'Пользователи'")
    # users smoke test
    @allure.title("Посещение раздела 'Пользователи' и его проверка")
    def test_user_0(self, users_page):
        print('"Users smoke test" launched...')
        self.driver = users_page

        wait = WebDriverWait(self.driver, 20, 0.5)

        try:
            table_users = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div[1]/lta-table/table')
        except:
            print('Users table is missing, check it out!')

        table_name = self.driver.find_element(By.XPATH, "//*[contains(text(),'Имя')]")
        assert table_name.text == 'Имя', 'Сolumn "Имя" is missing'

        table_email = self.driver.find_element(By.XPATH, "//*[contains(text(),'Email')]")
        assert table_email.text == 'Email', 'Сolumn "Email" is missing'

        table_role = self.driver.find_element(By.XPATH, "//*[contains(text(),'Роль')]")
        assert table_role.text == 'Роль', 'Сolumn "Роль" is missing'

        print('"Users smoke test" passed')

    @allure.description("Проверка работоспособности раздела 'Пользователи'")
    # users creation test
    @allure.title("Создание и удаление пользователя")
    def test_user_1(self, get_webdriver):
        print('"Users creation test" launched...')
        self.driver = get_webdriver

        wait = WebDriverWait(self.driver, 20, 0.5)

        name = 'AutoTest_User'
        login = 'autotest_user'
        email = 'autotest_user@test.com'

        same_users = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        same_emails = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + email + "')]"))

        if same_users or same_emails == 1:
            login = login + str(random.randint(0, 100))

        if same_users == 1:
            print(f'{same_users} user with the name {name} was found. Check it out!')

        while same_users != 0:
            name = name + str(random.randint(0, 100))
            same_users = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        same_emails = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + email + "')]"))
        if same_emails == 1:
            print(f'{same_emails} user with the email {email} was found. Check it out!')

        while same_emails != 0:
            email = email + str(random.randint(0, 100))
            same_emails = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + email + "')]"))

        try:
            button_create_user_check = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        except:
            print('Create button is missing, check it out!')

        button_create_user = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_user.click()
        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '1]/label/span[2]/input')))

        user_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '1]/label/span[2]/input')
        user_name.send_keys(name)

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '2]/label/span[2]/input')))
        user_login = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '2]/label/span[2]/input')
        user_login.send_keys(login)

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '3]/label/span[2]/input')))
        user_email = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '3]/label/span[2]/input')
        user_email.send_keys(email)

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                           '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                           '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                           '1]/label/span[2]/span/span')))
        role_dropdown = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                           '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                           '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                           '1]/label/span[2]/span/span')

        role_dropdown.click()

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta'
                                                               '-users-page/lta-header-layout/div/div['
                                                               '2]/lta-aside-layout/div['
                                                               '2]/lta-user-info-panel/div/div/form/section/lta'
                                                               '-select[1]/label/span[2]/span/span[2]/span/span/span['
                                                               '1]')))
        admin_role_select = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta'
                                                               '-users-page/lta-header-layout/div/div['
                                                               '2]/lta-aside-layout/div['
                                                               '2]/lta-user-info-panel/div/div/form/section/lta'
                                                               '-select[1]/label/span[2]/span/span[2]/span/span/span['
                                                               '1]')
        admin_role_select.click()

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                            '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                            '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                            '2]/label/span[2]/span/span[1]')))
        mnemo_dropdown = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                            '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                            '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                            '2]/label/span[2]/span/span[1]')
        mnemo_dropdown.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Электросети')]")))
        mnemo_select = self.driver.find_element(By.XPATH, "//*[contains(text(),'Электросети')]")
        mnemo_select.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Сгенерировать пароль')]")))
        generate_password_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Сгенерировать пароль')]")
        generate_password_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Создать')]")))
        create_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Создать')]")
        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))

        cancel_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Отмена')]")
        cancel_button.click()

        time.sleep(1)

        created_user = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_user.text == f'{name}', 'User was not created'
        print('User created and checked')

        created_user.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Отмена')]")))

        try:
            delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        except:
            print('Delete button is missing, check it out!')

        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        delete_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        delete_modal_button.click()

        wait.until(ec.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'User' \
                                                                                                      'was not deleted'

        print('User deleted')
        print('"Users creation test" passed')

    @allure.description("Проверка работоспособности раздела 'Пользователи'")
    # users validation test
    @allure.title("Попытка создания пользователя с одинаковыми email и логином")
    def test_user_2(self, get_webdriver):
        print('"Users validation test" launched...')
        self.driver = get_webdriver

        wait = WebDriverWait(self.driver, 20, 0.5)

        name = 'AutoTest_User'
        login = 'autotest_user'
        email = 'autotest_user@test.com'

        same_users = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        same_emails = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + email + "')]"))

        if same_users or same_emails == 1:
            login = login + str(random.randint(0, 100))

        if same_users == 1:
            print(f'{same_users} user with the name {name} was found. Check it out!')

        while same_users != 0:
            name = name + str(random.randint(0, 100))
            same_users = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        same_emails = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + email + "')]"))
        if same_emails == 1:
            print(f'{same_emails} user with the email {email} was found. Check it out!')

        while same_emails != 0:
            email = email + str(random.randint(0, 100))
            same_emails = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + email + "')]"))

        try:
            button_create_user_check = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        except:
            print('Create button is missing, check it out!')

        button_create_user = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_user.click()
        wait.until(
                ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                          '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                          '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                          '1]/label/span[2]/input')))

        user_name = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                 '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                 '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                 '1]/label/span[2]/input')
        user_name.send_keys(name)

        wait.until(
                ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                          '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                          '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                          '2]/label/span[2]/input')))
        user_login = self.driver.find_element(By.XPATH,
                                                  '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                  '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                  '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                  '2]/label/span[2]/input')
        user_login.send_keys(login)

        wait.until(
                ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                          '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                          '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                          '3]/label/span[2]/input')))
        user_email = self.driver.find_element(By.XPATH,
                                                  '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                  '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                  '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                  '3]/label/span[2]/input')
        user_email.send_keys(email)

        wait.until(
                ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                          '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                          '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                          '1]/label/span[2]/span/span')))
        role_dropdown = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                               '-page/lta-header-layout/div/div['
                                                           '2]/lta-aside-layout/div['
                                                               '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                               '1]/label/span[2]/span/span')

        role_dropdown.click()

        wait.until(
                ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta'
                                                          '-users-page/lta-header-layout/div/div['
                                                          '2]/lta-aside-layout/div['
                                                          '2]/lta-user-info-panel/div/div/form/section/lta'
                                                          '-select[1]/label/span[2]/span/span[2]/span/span/span['
                                                          '1]')))
        admin_role_select = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta'
                                                                   '-users-page/lta-header-layout/div/div['
                                                                   '2]/lta-aside-layout/div['
                                                                   '2]/lta-user-info-panel/div/div/form/section/lta'
                                                                   '-select[1]/label/span[2]/span/span[2]/span/span/span['
                                                                   '1]')
        admin_role_select.click()

        wait.until(
                ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                          '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                          '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                          '2]/label/span[2]/span/span[1]')))
        mnemo_dropdown = self.driver.find_element(By.XPATH,
                                                      '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                      '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                      '2]/label/span[2]/span/span[1]')
        mnemo_dropdown.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Электросети')]")))
        mnemo_select = self.driver.find_element(By.XPATH, "//*[contains(text(),'Электросети')]")
        mnemo_select.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Сгенерировать пароль')]")))
        generate_password_button = self.driver.find_element(By.XPATH,
                                                                "//*[contains(text(),'Сгенерировать пароль')]")
        generate_password_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Создать')]")))
        create_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Создать')]")
        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))

        cancel_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Отмена')]")
        cancel_button.click()

        time.sleep(1)

        created_user = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_user.text == f'{name}', 'User was not created'
        print('User created and checked')

        print('Trying to create second user with the same login and email')

        button_create_user.click()
        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '1]/label/span[2]/input')))

        user_name = self.driver.find_element(By.XPATH,
                                             '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                             '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                             '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                             '1]/label/span[2]/input')
        user_name.send_keys(name)

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '2]/label/span[2]/input')))
        user_login = self.driver.find_element(By.XPATH,
                                              '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                              '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                              '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                              '2]/label/span[2]/input')
        user_login.send_keys(login)
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Логин уже занят')]")))
        print('Warning "Логин уже занят" is active')

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                                      '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                                      '3]/label/span[2]/input')))
        user_email = self.driver.find_element(By.XPATH,
                                              '/html/body/app-root/app-admin-layout/div/main/lta-users-page'
                                              '/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                              '2]/lta-user-info-panel/div/div/form/section/lta-input['
                                              '3]/label/span[2]/input')
        user_email.send_keys(email)
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Email уже занят')]")))
        print('Warning "Email уже занят" is active')

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                      '-page/lta-header-layout/div/div[2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                      '1]/label/span[2]/span/span')))
        role_dropdown = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-users'
                                                           '-page/lta-header-layout/div/div['
                                                           '2]/lta-aside-layout/div['
                                                           '2]/lta-user-info-panel/div/div/form/section/lta-select['
                                                           '1]/label/span[2]/span/span')

        role_dropdown.click()

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta'
                                                      '-users-page/lta-header-layout/div/div['
                                                      '2]/lta-aside-layout/div['
                                                      '2]/lta-user-info-panel/div/div/form/section/lta'
                                                      '-select[1]/label/span[2]/span/span[2]/span/span/span['
                                                      '1]')))
        admin_role_select = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta'
                                                               '-users-page/lta-header-layout/div/div['
                                                               '2]/lta-aside-layout/div['
                                                               '2]/lta-user-info-panel/div/div/form/section/lta'
                                                               '-select[1]/label/span[2]/span/span[2]/span/span/span['
                                                               '1]')
        admin_role_select.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Создать')]")))
        create_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Создать')]")
        create_button.click()

        time.sleep(1)

        cancel_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Отмена')]")
        cancel_button.click()

        time.sleep(1)

        number_of_created_users = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + email + "')]"))
        assert number_of_created_users == 1, f'Two users with the login {login} and email {email} were created, check it out!'

        print(f'There is only one user with the login {login} and email {email}')

        created_user.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Отмена')]")))

        try:
            delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        except:
            print('Delete button is missing, check it out!')

        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        delete_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        delete_modal_button.click()

        wait.until(ec.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'User' \
                                                                                                      'was not deleted'

        print('User deleted')
        print('"Users validation test" passed')

        self.driver.close()
        self.driver.quit()
