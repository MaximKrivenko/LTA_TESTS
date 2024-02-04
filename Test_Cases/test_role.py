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


class TestRole:
    print(f'TEST ROLES LAUNCHED ON {env_url}')

    @allure.description("Проверка работоспособности раздела 'Роли'")
    # roles smoke test
    @allure.title("Посещение раздела 'Роли' и его проверка")
    def test_role_0(self, roles_page):
        print('"Roles smoke test" launched...')
        self.driver = roles_page

        wait = WebDriverWait(self.driver, 20, 0.5)

        try:
            table_roles = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div[1]/lta-table/table')
        except:
            print('Roles table is missing, check it out!')

        table_name = self.driver.find_element(By.XPATH, "//*[contains(text(),'Название')]")
        assert table_name.text == 'Название', 'Сolumn "Имя" is missing'

        table_description = self.driver.find_element(By.XPATH, "//*[contains(text(),'Описание')]")
        assert table_description.text == 'Описание', 'Сolumn "Описание" is missing'

        print('"Roles smoke test" passed')

    @allure.description("Проверка работоспособности раздела 'Роли'")
    # roles creation test
    @allure.title("Создание и удаление роли")
    def test_role_1(self, get_webdriver):
        print('"Roles creation test" launched...')
        self.driver = get_webdriver

        name = 'AutoTest_Role'
        description = 'Тестовая роль'

        wait = WebDriverWait(self.driver, 20, 0.5)

        same_roles = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        if same_roles == 1:
            print(f'{same_roles} role with the name {name} was found. Check it out!')

        while same_roles != 0:
            name = name + str(random.randint(0, 100))
            same_roles = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        try:
            button_create_role = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        except:
            print('Create button is missing, check it out!')

        button_create_role = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_role.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div['
                                                             '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                             '/span[2]/input')))

        role_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                       '-page/lta-header-layout/div/div['
                                                       '2]/lta-aside-layout/div['
                                                       '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                       '/span[2]/input')
        role_name.send_keys(name)

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'textarea.ng-untouched.ng-pristine.ng-valid')))
        role_description = self.driver.find_element(By.CLASS_NAME, 'textarea.ng-untouched.ng-pristine.ng-valid')
        role_description.send_keys(description)

        try:
            radiobutton_permissions = self.driver.find_element(By.CLASS_NAME, 'unchecked')
        except:
            print('Radio button "Permissions" is missing, check it out!')

        radiobutton_permissions = self.driver.find_element(By.CLASS_NAME, 'unchecked')
        radiobutton_permissions.click()

        try:
            create_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        except:
            print('Create button is missing, check it out!')

        create_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('Role created')

        try:
            cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        except:
            print('Cancel button is missing, check it out!')

        cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        cancel_button.click()

        time.sleep(1)

        created_role = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_role.text == f'{name}', 'Role was not created'
        print('Role checked')

        created_role.click()
        created_role.click()

        time.sleep(2)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div['
                                                             '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                             '/span[2]/input')))

        try:
            delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        except:
            print('Delete button is missing, check it out!')

        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        delete_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        try:
            delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        except:
            print('Delete modal button is missing, check it out!')

        delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        delete_modal_button.click()

        wait.until(ec.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Role ' \
                                                                                                      'was not deleted'

        print('Role deleted')
        print('"Roles creation test" passed')


    @allure.description("Проверка работоспособности раздела 'Роли'")
    # roles same name creation test
    @allure.title("Попытка создания ролей с одинаковыми именами, проверка и удаление")
    def test_role_2(self, get_webdriver):
        print('"Roles same name creation test" launched...')
        self.driver = get_webdriver

        name = 'AutoTest_Role'
        description = 'Тестовая роль'

        wait = WebDriverWait(self.driver, 20, 0.5)

        same_roles = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        if same_roles == 1:
            print(f'{same_roles} role with the name {name} was found. Check it out!')

        while same_roles != 0:
            name = name + str(random.randint(0, 100))
            same_roles = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_role = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_role.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div['
                                                             '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                             '/span[2]/input')))

        role_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                       '-page/lta-header-layout/div/div['
                                                       '2]/lta-aside-layout/div['
                                                       '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                       '/span[2]/input')
        role_name.send_keys(name)

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'textarea.ng-valid.ng-dirty.ng-touched')))
        role_description = self.driver.find_element(By.CLASS_NAME, 'textarea.ng-valid.ng-dirty.ng-touched')
        role_description.send_keys(description)

        try:
            radiobutton_permissions = self.driver.find_element(By.CLASS_NAME, 'unchecked')
        except:
            print('Radio button "Permissions" is missing, check it out!')

        radiobutton_permissions = self.driver.find_element(By.CLASS_NAME, 'unchecked')
        radiobutton_permissions.click()

        try:
            create_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        except:
            print('Create button is missing, check it out!')

        create_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('First role created')

        try:
            cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        except:
            print('Cancel button is missing, check it out!')

        cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        cancel_button.click()

        time.sleep(1)

        created_role = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_role.text == f'{name}', 'Role was not created'
        print('Role checked')

        print('Trying to create second role with the same name...')

        button_create_role = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_role.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div['
                                                             '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                             '/span[2]/input')))

        role_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                       '-page/lta-header-layout/div/div['
                                                       '2]/lta-aside-layout/div['
                                                       '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                       '/span[2]/input')
        role_name.send_keys(name)

        create_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')

        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Имя уже занято')]")))
        print('Warning "Имя уже занято" is active')

        cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        cancel_button.click()

        time.sleep(1)

        number_of_created_roles = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        assert number_of_created_roles == 1, f'Two roles with the name {name} were created, check it out!'

        print(f'There is only one role with the name {name}')

        created_role = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")

        created_role.click()

        time.sleep(2)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div['
                                                             '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                             '/span[2]/input')))

        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        delete_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        delete_modal_button.click()

        wait.until(ec.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Role ' \
                                                                                                      'was not deleted'

        print('First role deleted')
        print('"Roles same name creation test" passed')

    @allure.description("Проверка работоспособности раздела 'Роли'")
    # roles editing test
    @allure.title("Создание и редактирование роли")
    def test_role_3(self, get_webdriver):
        print('"Roles editing test" launched...')
        self.driver = get_webdriver

        name = 'AutoTest_Role'
        description = 'Тестовая роль'

        wait = WebDriverWait(self.driver, 20, 0.5)

        same_roles = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        if same_roles == 1:
            print(f'{same_roles} role with the name {name} was found. Check it out!')

        while same_roles != 0:
            name = name + str(random.randint(0, 100))
            same_roles = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        try:
            button_create_role_check = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        except:
            print('Create button is missing, check it out!')

        button_create_role = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_role.click()
        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                          '-page/lta-header-layout/div/div['
                                                          '2]/lta-aside-layout/div['
                                                          '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                          '/span[2]/input')))

        role_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                           '-page/lta-header-layout/div/div['
                                                           '2]/lta-aside-layout/div['
                                                           '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                           '/span[2]/input')
        role_name.send_keys(name)

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'textarea.ng-valid.ng-dirty.ng-touched')))
        role_description = self.driver.find_element(By.CLASS_NAME, 'textarea.ng-valid.ng-dirty.ng-touched')
        role_description.send_keys(description)

        try:
            radiobutton_permissions_check = self.driver.find_element(By.CLASS_NAME, 'unchecked')
        except:
            print('Radio button "Permissions" is missing, check it out!')

        radiobutton_permissions = self.driver.find_element(By.CLASS_NAME, 'unchecked')
        radiobutton_permissions.click()

        try:
            create_button_check = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        except:
            print('Create button is missing, check it out!')

        create_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('Role created')

        try:
            cancel_button_check = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        except:
            print('Cancel button is missing, check it out!')

        cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        cancel_button.click()

        time.sleep(1)

        created_role = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_role.text == f'{name}', 'Role was not created'
        print('Role checked')

        created_role.click()
        created_role.click()

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                          '-page/lta-header-layout/div/div['
                                                          '2]/lta-aside-layout/div['
                                                          '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                          '/span[2]/input')))

        name_edited = name + str(random.randint(0, 100))
        role_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                       '-page/lta-header-layout/div/div['
                                                       '2]/lta-aside-layout/div['
                                                       '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                       '/span[2]/input')
        role_name.clear()

        time.sleep(1)

        role_name.send_keys(name_edited)

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'textarea.ng-valid.ng-dirty.ng-touched')))
        role_description = self.driver.find_element(By.CLASS_NAME, 'textarea.ng-valid.ng-dirty.ng-touched')
        description_edited = description + str(random.randint(0, 100))
        role_description.clear()

        time.sleep(1)

        role_description.send_keys(description_edited)

        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name_edited + "')]")))

        cancel_button.click()

        time.sleep(1)

        edited_role = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name_edited + "')]")
        assert edited_role.text == f'{name_edited}', 'Role has not been edited'
        print('Role has been edited')

        edited_role.click()
        edited_role.click()

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta-roles'
                                                             '-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div['
                                                             '2]/lta-roles-info-panel/div/form/div/lta-input/label'
                                                             '/span[2]/input')))

        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        delete_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        delete_modal_button.click()

        wait.until(ec.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name_edited + "')]")) == 0, 'Role ' \
                                                                                                      'was not deleted'

        print('Role deleted')
        print('"Roles editing test" passed')

        self.driver.close()
        self.driver.quit()








