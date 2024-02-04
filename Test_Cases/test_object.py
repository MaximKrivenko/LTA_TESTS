import pytest
import allure
import time
import random
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()
env_url = os.getenv('URL')


class TestObject:
    print(f'TEST OBJECTS LAUNCHED ON {env_url}')

    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание и удаление корневого объекта")
    def test_object(self, objects_page):
        print('Simple root object test launched...')
        self.driver = objects_page
        name = 'AutoTest_Object'
        description = 'Тестовый объект'
        wait = WebDriverWait(self.driver, 15, 0.5)

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_objects != 0:
            name = name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.primary.md')))
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-icon.primary.md')))
        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('Simple root object created')
        created_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_object.text == f'{name}', 'Object was not created'
        print('Simple root object checked')
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Simple root ' \
                                                                                                      'object ' \
                                                                                                      'was not deleted'
        print('Simple root object deleted')

        time.sleep(2)

    # simple root object name validation test
    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание двух корневых объектов с одинаковыми именами, проверка и удаление")
    def test_object1(self, get_webdriver):
        print('Simple root object name validation test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Object'
        description = 'Тестовый объект'
        wait = WebDriverWait(self.driver, 15, 0.5)

        current_url = self.driver.current_url
        goal_url = f'{env_url}conf/data/objects'

        if current_url != goal_url:
            print(f'Current URL is {current_url}, need to return to the Objects section')
            objects_button = self.driver.find_element(By.XPATH,
                                                      '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                      '/li[5]/a')
            objects_button.click()
            wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
            print('Objects section reached')
        else:
            pass

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_objects != 0:
            name = name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('First simple root object created')

        created_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_object.text == f'{name}', 'First simple object was not created'
        print('First simple root object checked')

        print('Trying to create second simple root object with the same name...')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name.send_keys(name)
        time.sleep(1)
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        time.sleep(5)
        number_of_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        assert number_of_objects == 1, F'Two simple root ' \
                                       F'objects with ' \
                                       F'the name ' \
                                       F'{name} were ' \
                                       F'created, ' \
                                       F'need to fix'
        print('There is only one simple root object with the name', name, 'created')

        simple_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        simple_object.click()
        simple_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))

        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'First simple ' \
                                                                                                      'root ' \
                                                                                                      'object ' \
                                                                                                      'was not deleted'
        print('First simple root object deleted')

        time.sleep(2)

    # Complex root object test
    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание корневого объекта, добавление в него объекта по модели Directory, проверка и удаление корневого объекта")
    def test_object2(self, get_webdriver):
        print('Complex root object test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Object'
        description = 'Тестовый объект'
        wait = WebDriverWait(self.driver, 15, 0.5)

        current_url = self.driver.current_url
        goal_url = f'{env_url}conf/data/objects'

        if current_url != goal_url:
            print(f'Current URL is {current_url}, need to return to the Objects section')
            objects_button = self.driver.find_element(By.XPATH,
                                                      '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                      '/li[5]/a')
            objects_button.click()
            wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
            print('Objects section reached')
        else:
            pass

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_objects != 0:
            name = name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))

        self.driver.refresh()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))
        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + name + "')]//parent::div//parent::div//parent"
                                                                               "::div//child::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                "::div//parent::div"
                                                                                                "//parent::div//parent"
                                                                                                "::node-name//parent"
                                                                                                "::div[1]//parent"
                                                                                                "::div//child::div["
                                                                                                "2]//child::div//child"
                                                                                                "::node//child::div"
                                                                                                "//child::div[1]//child"
                                                                                                "::node-name//child"
                                                                                                "::div//child::div"
                                                                                                "//child::div//child"
                                                                                                "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                         "::div//parent::div"
                                                                                                         "//parent::div//parent"
                                                                                                         "::node-name//parent"
                                                                                                         "::div[1]//parent"
                                                                                                         "::div//child::div["
                                                                                                         "2]//child::div//child"
                                                                                                         "::node//child::div"
                                                                                                         "//child::div[1]//child"
                                                                                                         "::node-name//child"
                                                                                                         "::div//child::div"
                                                                                                         "//child::div//child"
                                                                                                         "::div")
        create_child_object_button.click()
        child_name = 'Child_test_object'
        child_description = 'Дочерний тестовый объект'

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(child_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(child_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name + "')]")))
        print('Child object created')
        child_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + child_name + "')]")
        assert child_object.text == f'{child_name}', 'Root object does not have child object'
        print('Root object has child object')

        cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        cancel_button.click()

        root_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        root_object.click()

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Complex root ' \
                                                                                                      'object ' \
                                                                                                      'was not deleted'
        print('Complex root object deleted')

        time.sleep(2)

    # complex root object child object name validation test
    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание корневого объекта, добавление в него объекта по модели Directory, добавление второго объекта по модели Directory с тем же именем, проверка и удаление корневого объекта")
    def test_object3(self, get_webdriver):
        print('Complex root object child object name validation test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Object'
        description = 'Тестовый объект'
        wait = WebDriverWait(self.driver, 15, 0.5)

        current_url = self.driver.current_url
        goal_url = f'{env_url}conf/data/objects'

        if current_url != goal_url:
            print(f'Current URL is {current_url}, need to return to the Objects section')
            objects_button = self.driver.find_element(By.XPATH,
                                                      '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                      '/li[5]/a')
            objects_button.click()
            wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
            print('Objects section reached')
        else:
            pass

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        self.driver.refresh()

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_objects != 0:
            name = name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))

        self.driver.refresh()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))
        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + name + "')]//parent::div//parent::div//parent"
                                                                               "::div//child::span//child::svg-icon")
        chevron_right_button.click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                "::div//parent::div"
                                                                                                "//parent::div//parent"
                                                                                                "::node-name//parent"
                                                                                                "::div[1]//parent"
                                                                                                "::div//child::div["
                                                                                                "2]//child::div//child"
                                                                                                "::node//child::div"
                                                                                                "//child::div[1]//child"
                                                                                                "::node-name//child"
                                                                                                "::div//child::div"
                                                                                                "//child::div//child"
                                                                                                "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                         "::div//parent::div"
                                                                                                         "//parent::div//parent"
                                                                                                         "::node-name//parent"
                                                                                                         "::div[1]//parent"
                                                                                                         "::div//child::div["
                                                                                                         "2]//child::div//child"
                                                                                                         "::node//child::div"
                                                                                                         "//child::div[1]//child"
                                                                                                         "::node-name//child"
                                                                                                         "::div//child::div"
                                                                                                         "//child::div//child"
                                                                                                         "::div")
        create_child_object_button.click()
        child_name = 'Child_test_object_1'
        same_child_objects = self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + child_name + "')]")
        while same_child_objects != 0:
            child_name = child_name + str(random.randint(0, 100))
            same_child_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + child_name + "')]"))

        child_description = 'Дочерний тестовый объект #1'
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(child_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(child_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name + "')]")))
        print('Child object created')
        child_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + child_name + "')]")
        assert child_object.text == f'{child_name}', 'Root object does not have child object'
        print('Root object has child object')

        print('Trying to create second child object with the same name...')
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                "::div//parent::div"
                                                                                                "//parent::div//parent"
                                                                                                "::node-name//parent"
                                                                                                "::div[1]//parent"
                                                                                                "::div//child::div["
                                                                                                "2]//child::div//child"
                                                                                                "::node[2]//child::div"
                                                                                                "//child::div[1]//child"
                                                                                                "::node-name//child"
                                                                                                "::div//child::div"
                                                                                                "//child::div//child"
                                                                                                "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                         "::div//parent::div"
                                                                                                         "//parent::div//parent"
                                                                                                         "::node-name//parent"
                                                                                                         "::div[1]//parent"
                                                                                                         "::div//child::div["
                                                                                                         "2]//child::div//child"
                                                                                                         "::node[2]//child::div"
                                                                                                         "//child::div[1]//child"
                                                                                                         "::node-name//child"
                                                                                                         "::div//child::div"
                                                                                                         "//child::div//child"
                                                                                                         "::div")
        create_child_object_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(child_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(child_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        time.sleep(5)
        number_of_child_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + child_name + "')]"))
        assert number_of_child_objects == 1, 'There are two child objects with the same name, need to fix'
        print('Second child object with the same name was not created')

        cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        cancel_button.click()

        root_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        root_object.click()

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Complex root ' \
                                                                                                      'object ' \
                                                                                                      'was not deleted'
        print('Complex root object deleted')

        time.sleep(2)

    # complex root object child object deleting test
    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание корневого объекта, добавление в него двух объектов по модели Directory с уникальными именами. Удаление одного дочернего объекта, проверка. Удаление корневого объекта")
    def test_object4(self, get_webdriver):
        print('Complex root object child object deleting test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Object'
        description = 'Тестовый объект'
        wait = WebDriverWait(self.driver, 15, 0.5)

        current_url = self.driver.current_url
        goal_url = f'{env_url}conf/data/objects'

        if current_url != goal_url:
            print(f'Current URL is {current_url}, need to return to the Objects section')
            objects_button = self.driver.find_element(By.XPATH,
                                                      '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                      '/li[5]/a')
            objects_button.click()
            wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
            print('Objects section reached')
        else:
            pass

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        self.driver.refresh()

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_objects != 0:
            name = name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))

        self.driver.refresh()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))
        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + name + "')]//parent::div//parent::div//parent"
                                                                               "::div//child::span//child::svg-icon")
        chevron_right_button.click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                "::div//parent::div"
                                                                                                "//parent::div//parent"
                                                                                                "::node-name//parent"
                                                                                                "::div[1]//parent"
                                                                                                "::div//child::div["
                                                                                                "2]//child::div//child"
                                                                                                "::node//child::div"
                                                                                                "//child::div[1]//child"
                                                                                                "::node-name//child"
                                                                                                "::div//child::div"
                                                                                                "//child::div//child"
                                                                                                "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                         "::div//parent::div"
                                                                                                         "//parent::div//parent"
                                                                                                         "::node-name//parent"
                                                                                                         "::div[1]//parent"
                                                                                                         "::div//child::div["
                                                                                                         "2]//child::div//child"
                                                                                                         "::node//child::div"
                                                                                                         "//child::div[1]//child"
                                                                                                         "::node-name//child"
                                                                                                         "::div//child::div"
                                                                                                         "//child::div//child"
                                                                                                         "::div")
        create_child_object_button.click()
        child_name_1 = 'Child_delete_test_object_1'
        child_name_2 = 'Child_delete_test_object_2'
        child_description_1 = 'Дочерний тестовый объект #1'
        child_description_2 = 'Дочерний тестовый объект #2'
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(child_name_1)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(child_description_1)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name_1 + "')]")))
        print('Child object #1 created')

        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                "::div//parent::div"
                                                                                                "//parent::div//parent"
                                                                                                "::node-name//parent"
                                                                                                "::div[1]//parent"
                                                                                                "::div//child::div["
                                                                                                "2]//child::div//child"
                                                                                                "::node[2]//child::div"
                                                                                                "//child::div[1]//child"
                                                                                                "::node-name//child"
                                                                                                "::div//child::div"
                                                                                                "//child::div//child"
                                                                                                "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]//parent"
                                                                                                         "::div//parent::div"
                                                                                                         "//parent::div//parent"
                                                                                                         "::node-name//parent"
                                                                                                         "::div[1]//parent"
                                                                                                         "::div//child::div["
                                                                                                         "2]//child::div//child"
                                                                                                         "::node[2]//child::div"
                                                                                                         "//child::div[1]//child"
                                                                                                         "::node-name//child"
                                                                                                         "::div//child::div"
                                                                                                         "//child::div//child"
                                                                                                         "::div")
        create_child_object_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-objects'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-object-info-panel/div/div/form/lta-input/label/span['
                                                         '2]/input')
        object_name.send_keys(child_name_2)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description.send_keys(child_description_2)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name_2 + "')]")))
        print('Child object #2 created')

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + child_name_2 + "')]")) == 0, 'Child ' \
                                                                                                              'object' \
                                                                                                              ' #2 ' \
                                                                                                              'was ' \
                                                                                                              'not ' \
                                                                                                              'deleted'
        print('Child object #2 deleted')

        root_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        root_object.click()

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Complex root ' \
                                                                                                      'object ' \
                                                                                                      'was not deleted'
        print('Complex root object deleted')

    # model-object simple test
    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание модели, содержащей подмодели. Создание корневого объекта по модели Directory. Добавление в него объекта по созданной модели. Проверка и удаление объекта. Удаление модели.")
    def test_object5(self, get_webdriver):
        print('Model-Object simple test launched...')
        self.driver = get_webdriver

        models_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul/li['
                                                 '4]/a')
        models_button.click()

        model_name = 'AutoTest_Model'
        model_description = 'Тестовая модель'
        wait = WebDriverWait(self.driver, 15, 0.5)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel/app-tree')))

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]"))
        while same_models != 0:
            model_name = model_name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]"))

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/form/lta-input/label"
                                                             "/span[2]/input")))
        model_name_input = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                              "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                              "2]/app-models-info-panel/form/div/form/lta-input/label"
                                                              "/span[2]/input")
        model_name_input.send_keys(model_name)
        model_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description_input.send_keys(model_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        cancel_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                 '-page/header-layout/div/div[2]/aside-layout/div['
                                                 '2]/app-models-info-panel/form/lta-save-cancel-panel/div'
                                                 '/lta-btn[1]/button')
        cancel_button.click()

        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + name + "')]//parent::div//parent::div//parent"
                                                                               "::div//child::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                            '-page/header-layout/div/div[2]/aside-layout/div['
                                                            '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                            '/span[2]/input')
        sub_model_name.send_keys('Test_boolean')
        sub_model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        sub_model_description.send_keys('Дочерняя модель по модели Boolean')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_boolean_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                      '/app-models-page/header-layout/div/div['
                                                                      '2]/aside-layout/div['
                                                                      '2]/app-models-info-panel/form/div/form/lta'
                                                                      '-select/label/span[2]/span/span[2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_boolean ')]")))
        print('Child model boolean created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_directory')
        sub_model_description.send_keys('Дочерняя модель по модели Directory')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_directory_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/form/lta'
                                                                        '-select/label/span[2]/span/span[2]/span[4]')
        sub_model_directory_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_directory ')]")))
        print('Child model directory created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_float')
        sub_model_description.send_keys('Дочерняя модель по модели Float')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_float_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                    '/app-models-page/header-layout/div/div['
                                                                    '2]/aside-layout/div['
                                                                    '2]/app-models-info-panel/form/div/form/lta'
                                                                    '-select/label/span[2]/span/span[2]/span[3]')
        sub_model_float_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_float ')]")))
        print('Child model float created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_string')
        sub_model_description.send_keys('Дочерняя модель по модели String')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_string_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                     '/app-models-page/header-layout/div/div['
                                                                     '2]/aside-layout/div['
                                                                     '2]/app-models-info-panel/form/div/form/lta'
                                                                     '-select/label/span[2]/span/span[2]/span[4]')
        sub_model_string_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_string ')]")))
        print('Child model string created')
        print('Test model created')

        wait.until(
            ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                      '/li[5]/a')))
        objects_button = self.driver.find_element(By.XPATH,
                                                  '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                  '/li[5]/a')
        objects_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        object_name = 'AutoTest_Object'
        object_description = 'Тестовый объект'

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]"))
        while same_objects != 0:
            object_name = object_name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]"))

        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name_input = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-objects'
                                                               '-page/header-layout/div/div[2]/aside-layout/div['
                                                               '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                               '/span['
                                                               '2]/input')
        object_name_input.send_keys(object_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description_input.send_keys(object_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + object_name + "')]")))
        print('Root object created')

        self.driver.refresh()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))
        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + object_name + "')]//parent::div//parent::div//child"
                                                                               "::span//child::svg-icon")
        chevron_right_button.click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + object_name + "')]//parent"
                                                                                                       "::div//parent::div"
                                                                                                       "//parent::div//parent"
                                                                                                       "::node-name//parent"
                                                                                                       "::div[1]//parent"
                                                                                                       "::div//child::div["
                                                                                                       "2]//child::div//child"
                                                                                                       "::node//child::div"
                                                                                                       "//child::div[1]//child"
                                                                                                       "::node-name//child"
                                                                                                       "::div//child::div"
                                                                                                       "//child::div//child"
                                                                                                       "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH,
                                                              "//*[contains(text(),'" + object_name + "')]//parent"
                                                                                                      "::div//parent::div"
                                                                                                      "//parent::div//parent"
                                                                                                      "::node-name//parent"
                                                                                                      "::div[1]//parent"
                                                                                                      "::div//child::div["
                                                                                                      "2]//child::div//child"
                                                                                                      "::node//child::div"
                                                                                                      "//child::div[1]//child"
                                                                                                      "::node-name//child"
                                                                                                      "::div//child::div"
                                                                                                      "//child::div//child"
                                                                                                      "::div")
        create_child_object_button.click()
        child_name = 'Child_test_object'
        child_description = 'Дочерний тестовый объект'
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name_input = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-objects'
                                                               '-page/header-layout/div/div[2]/aside-layout/div['
                                                               '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                               '/span['
                                                               '2]/input')
        object_name_input.send_keys(child_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        new_model_choose = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + model_name + "')]")
        new_model_choose.click()
        object_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description_input.send_keys(child_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name + "')]")))
        print('Child object created')
        child_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + child_name + "')]")
        assert child_object.text == f'{child_name} {model_name}', f'Root object does not have child object with {model_name} model'
        print(f'Root object has child object with {model_name} model')

        cancel_button = self.driver.find_element(By.CLASS_NAME, 'btn.secondary.md')
        cancel_button.click()

        root_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + object_name + "')]")
        root_object.click()

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]")) == 0, 'Root ' \
                                                                                                             'object ' \
                                                                                                             'was not ' \
                                                                                                             'deleted'
        print('Root object deleted')

        wait.until(ec.presence_of_element_located(
            (By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul/li['
                       '4]/a')))
        models_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul/li['
                                                 '4]/a')
        models_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/models'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                             '/main/app-models-page/header-layout/div'
                                                             '/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel')))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        test_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + model_name + "')]")
        test_model.click()

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page'
                                                             '/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))
        delete_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                 '/header-layout/div/div['
                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn[2]/button')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/lta-delete-dialog/lta-modal-layout/div/lta'
                                                             '-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-models-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/app-model-delete-options-dialog/lta-modal-layout'
                                                             '/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                         '-page/app-model-delete-options-dialog/lta-modal-layout/div'
                                                         '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window1 = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                   '-models-page/app-model-delete-options-dialog/lta'
                                                                   '-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                                   '2]/button')
        time.sleep(2)
        delete_button_window1.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                       '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                       '/app-model-delete-options-dialog/lta-modal-layout/div/lta'
                                                       '-modal/div[2]/lta-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]")) == 0, 'Test' \
                                                                                                            'model ' \
                                                                                                            'was not ' \
                                                                                                            'deleted'
        print('Test model deleted')

    # model-object delete model with deleting object test
    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание модели, содержаей подмодели. Создание корневого объекта по модели Directory. Добавление в него объекта по созданой модели. Проверка объекта. Удаление модели с удалением объекта. Проверка факта удаления объекта. Удаление корневого объекта.")
    def test_object6(self, get_webdriver):
        print('Model-Object delete model with deleting object test launched...')
        self.driver = get_webdriver

        models_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul/li['
                                                 '4]/a')
        models_button.click()

        model_name = 'AutoTest_Model'
        model_description = 'Тестовая модель'
        wait = WebDriverWait(self.driver, 15, 0.5)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel/app-tree')))

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]"))
        while same_models != 0:
            model_name = model_name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]"))

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/form/lta-input/label"
                                                             "/span[2]/input")))
        model_name_input = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/form/lta-input/label"
                                                             "/span[2]/input")
        model_name_input.send_keys(model_name)
        model_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description_input.send_keys(model_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        cancel_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                 '-page/header-layout/div/div[2]/aside-layout/div['
                                                 '2]/app-models-info-panel/form/lta-save-cancel-panel/div'
                                                 '/lta-btn[1]/button')
        cancel_button.click()

        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + model_name + "')]//parent::div//parent::div"
                                                                                     "//child::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')
        sub_model_name.send_keys('Test_boolean')
        sub_model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        sub_model_description.send_keys('Дочерняя модель по модели Boolean')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_boolean_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                      '/app-models-page/header-layout/div/div['
                                                                      '2]/aside-layout/div['
                                                                      '2]/app-models-info-panel/form/div/form/lta'
                                                                      '-select/label/span[2]/span/span[2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_boolean ')]")))
        print('Child model boolean created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_directory')
        sub_model_description.send_keys('Дочерняя модель по модели Directory')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_directory_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/form/lta'
                                                                        '-select/label/span[2]/span/span[2]/span[4]')
        sub_model_directory_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_directory ')]")))
        print('Child model directory created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_float')
        sub_model_description.send_keys('Дочерняя модель по модели Float')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_float_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                    '/app-models-page/header-layout/div/div['
                                                                    '2]/aside-layout/div['
                                                                    '2]/app-models-info-panel/form/div/form/lta'
                                                                    '-select/label/span[2]/span/span[2]/span[3]')
        sub_model_float_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_float ')]")))
        print('Child model float created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_string')
        sub_model_description.send_keys('Дочерняя модель по модели String')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_string_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                     '/app-models-page/header-layout/div/div['
                                                                     '2]/aside-layout/div['
                                                                     '2]/app-models-info-panel/form/div/form/lta'
                                                                     '-select/label/span[2]/span/span[2]/span[4]')
        sub_model_string_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_string ')]")))
        print('Child model string created')
        print('Test model created')

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                   '/li[5]/a')))
        objects_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                   '/li[5]/a')
        objects_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        object_name = 'AutoTest_Object'
        object_description = 'Тестовый объект'

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]"))
        while same_objects != 0:
            object_name = object_name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]"))

        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name_input = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-objects'
                                                               '-page/header-layout/div/div[2]/aside-layout/div['
                                                               '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                               '/span['
                                                               '2]/input')
        object_name_input.send_keys(object_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description_input.send_keys(object_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + object_name + "')]")))
        print('Root object created')

        self.driver.refresh()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + object_name + "')]//parent::div//parent::div//child"
                                                                                      "::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + object_name + "')]//parent"
                                                                                                       "::div//parent::div"
                                                                                                       "//parent::div//parent"
                                                                                                       "::node-name//parent"
                                                                                                       "::div[1]//parent"
                                                                                                       "::div//child::div["
                                                                                                       "2]//child::div//child"
                                                                                                       "::node//child::div"
                                                                                                       "//child::div[1]//child"
                                                                                                       "::node-name//child"
                                                                                                       "::div//child::div"
                                                                                                       "//child::div//child"
                                                                                                       "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH,
                                                              "//*[contains(text(),'" + object_name + "')]//parent"
                                                                                                      "::div//parent::div"
                                                                                                      "//parent::div//parent"
                                                                                                      "::node-name//parent"
                                                                                                      "::div[1]//parent"
                                                                                                      "::div//child::div["
                                                                                                      "2]//child::div//child"
                                                                                                      "::node//child::div"
                                                                                                      "//child::div[1]//child"
                                                                                                      "::node-name//child"
                                                                                                      "::div//child::div"
                                                                                                      "//child::div//child"
                                                                                                      "::div")
        create_child_object_button.click()
        child_name = 'Child_test_object'
        child_description = 'Дочерний тестовый объект'
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name_input = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-objects'
                                                               '-page/header-layout/div/div[2]/aside-layout/div['
                                                               '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                               '/span['
                                                               '2]/input')
        object_name_input.send_keys(child_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        new_model_choose = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + model_name + "')]")
        new_model_choose.click()
        object_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description_input.send_keys(child_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name + "')]")))
        print('Child object created')
        child_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + child_name + "')]")
        assert child_object.text == f'{child_name} {model_name}', f'Root object does not have child object with {model_name} model'
        print(f'Root object has child object with {model_name} model')

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                             '/nav/ul/li[4]/a')))
        models_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                           '/nav/ul/li[4]/a')
        models_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/models'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                             '/main/app-models-page/header-layout/div'
                                                             '/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel')))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        test_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + model_name + "')]")
        test_model.click()

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page'
                                                             '/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))
        delete_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                 '/header-layout/div/div['
                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn[2]/button')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/lta-delete-dialog/lta-modal-layout/div/lta'
                                                             '-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-models-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/app-model-delete-options-dialog/lta-modal-layout'
                                                             '/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                         '-page/app-model-delete-options-dialog/lta-modal-layout/div'
                                                         '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window1 = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                   '-models-page/app-model-delete-options-dialog/lta'
                                                                   '-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                                   '2]/button')
        time.sleep(2)
        delete_button_window1.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                       '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                       '/app-model-delete-options-dialog/lta-modal-layout/div/lta'
                                                       '-modal/div[2]/lta-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]")) == 0, 'Test' \
                                                                                                            'model ' \
                                                                                                            'was not ' \
                                                                                                            'deleted'
        print('Test model deleted')

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                             '/nav/ul/li[5]/a')))
        objects_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                            '/nav/ul/li[5]/a')
        objects_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + child_name + "')]")) == 0, f'Child ' \
                                                                                                            f'object ' \
                                                                                                            f'with ' \
                                                                                                            f'{model_name} was not deleted'
        print(f'Root object does not have child object with {model_name} model')

        root_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + object_name + "')]")
        root_object.click()

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]")) == 0, 'Root ' \
                                                                                                             'object ' \
                                                                                                             'was not ' \
                                                                                                             'deleted'
        print('Root object deleted')

        time.sleep(2)

    # model-object delete model with keeping object test
    @allure.description("Проверка работоспособности раздела 'Объекты'")
    # simple root object test
    @allure.title("Создание модели, содержащей подмодели. Создание корневого объекта по модели Directory. Добавление в него объекта по созданной модели. Проверка объекта. Удаление модели с отвязкой объекта. Проверка факта сохранения объекта и изменения типа модели на Directory. Удаление корневого объекта.")
    def test_object7(self, get_webdriver):
        print('Model-Object delete model with keeping object test launched...')
        self.driver = get_webdriver

        models_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul/li['
                                                 '4]/a')
        models_button.click()

        model_name = 'AutoTest_Model'
        model_description = 'Тестовая модель'
        wait = WebDriverWait(self.driver, 15, 0.5)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel/app-tree')))

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]"))
        while same_models != 0:
            model_name = model_name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]"))

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/form/lta-input/label"
                                                             "/span[2]/input")))
        model_name_input = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/form/lta-input/label"
                                                             "/span[2]/input")
        model_name_input.send_keys(model_name)
        model_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description_input.send_keys(model_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        cancel_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                 '-page/header-layout/div/div[2]/aside-layout/div['
                                                 '2]/app-models-info-panel/form/lta-save-cancel-panel/div'
                                                 '/lta-btn[1]/button')
        cancel_button.click()

        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + model_name + "')]//parent::div//parent::div"
                                                                                     "//child::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')
        sub_model_name.send_keys('Test_boolean')
        sub_model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        sub_model_description.send_keys('Дочерняя модель по модели Boolean')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_boolean_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                      '/app-models-page/header-layout/div/div['
                                                                      '2]/aside-layout/div['
                                                                      '2]/app-models-info-panel/form/div/form/lta'
                                                                      '-select/label/span[2]/span/span[2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_boolean ')]")))
        print('Child model boolean created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_directory')
        sub_model_description.send_keys('Дочерняя модель по модели Directory')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_directory_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/form/lta'
                                                                        '-select/label/span[2]/span/span[2]/span[4]')
        sub_model_directory_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_directory ')]")))
        print('Child model directory created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_float')
        sub_model_description.send_keys('Дочерняя модель по модели Float')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_float_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                    '/app-models-page/header-layout/div/div['
                                                                    '2]/aside-layout/div['
                                                                    '2]/app-models-info-panel/form/div/form/lta'
                                                                    '-select/label/span[2]/span/span[2]/span[3]')
        sub_model_float_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_float ')]")))
        print('Child model float created')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
        sub_model_name.send_keys('Test_string')
        sub_model_description.send_keys('Дочерняя модель по модели String')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_string_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                     '/app-models-page/header-layout/div/div['
                                                                     '2]/aside-layout/div['
                                                                     '2]/app-models-info-panel/form/div/form/lta'
                                                                     '-select/label/span[2]/span/span[2]/span[4]')
        sub_model_string_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_string ')]")))
        print('Child model string created')
        print('Test model created')

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                   '/li[5]/a')))
        objects_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav/ul'
                                                   '/li[5]/a')
        objects_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        object_name = 'AutoTest_Object'
        object_description = 'Тестовый объект'

        same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]"))
        while same_objects != 0:
            object_name = object_name + str(random.randint(0, 100))
            same_objects = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]"))

        button_create_object = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_object.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name_input = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-objects'
                                                               '-page/header-layout/div/div[2]/aside-layout/div['
                                                               '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                               '/span['
                                                               '2]/input')
        object_name_input.send_keys(object_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        model_directory = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')
        model_directory.click()
        object_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description_input.send_keys(object_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + object_name + "')]")))
        print('Root object created')

        self.driver.refresh()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + object_name + "')]//parent::div//parent::div//child"
                                                                                      "::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'" + object_name + "')]//parent"
                                                                                                       "::div//parent::div"
                                                                                                       "//parent::div//parent"
                                                                                                       "::node-name//parent"
                                                                                                       "::div[1]//parent"
                                                                                                       "::div//child::div["
                                                                                                       "2]//child::div//child"
                                                                                                       "::node//child::div"
                                                                                                       "//child::div[1]//child"
                                                                                                       "::node-name//child"
                                                                                                       "::div//child::div"
                                                                                                       "//child::div//child"
                                                                                                       "::div")))
        create_child_object_button = self.driver.find_element(By.XPATH,
                                                              "//*[contains(text(),'" + object_name + "')]//parent"
                                                                                                      "::div//parent::div"
                                                                                                      "//parent::div//parent"
                                                                                                      "::node-name//parent"
                                                                                                      "::div[1]//parent"
                                                                                                      "::div//child::div["
                                                                                                      "2]//child::div//child"
                                                                                                      "::node//child::div"
                                                                                                      "//child::div[1]//child"
                                                                                                      "::node-name//child"
                                                                                                      "::div//child::div"
                                                                                                      "//child::div//child"
                                                                                                      "::div")
        create_child_object_button.click()
        child_name = 'Child_test_object'
        child_description = 'Дочерний тестовый объект'
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                             '/span[2]/input')))
        object_name_input = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-objects'
                                                               '-page/header-layout/div/div[2]/aside-layout/div['
                                                               '2]/app-object-info-panel/div/div/form/lta-input/label'
                                                               '/span['
                                                               '2]/input')
        object_name_input.send_keys(child_name)
        time.sleep(1)
        models_choice = self.driver.find_element(By.CLASS_NAME, 'select__value.placeholder')
        models_choice.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        new_model_choose = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + model_name + "')]")
        new_model_choose.click()
        object_description_input = self.driver.find_element(By.CLASS_NAME, 'textarea')
        object_description_input.send_keys(child_description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name + "')]")))
        print('Child object created')
        child_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + child_name + "')]")
        assert child_object.text == f'{child_name} {model_name}', f'Root object does not have child object with {model_name} model'
        print(f'Root object has child object with {model_name} model')

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                             '/nav/ul/li[4]/a')))
        models_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                           '/nav/ul/li[4]/a')
        models_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/models'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                             '/main/app-models-page/header-layout/div'
                                                             '/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel')))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + model_name + "')]")))
        test_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + model_name + "')]")
        test_model.click()

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page'
                                                             '/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))
        delete_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                 '/header-layout/div/div['
                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn[2]/button')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/lta-delete-dialog/lta-modal-layout/div/lta'
                                                             '-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-models-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/app-model-delete-options-dialog/lta-modal-layout'
                                                             '/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                         '-page/app-model-delete-options-dialog/lta-modal-layout/div'
                                                         '/lta-modal/div[2]/lta-btn[1]/button')))
        delete_button_window1 = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                   '-models-page/app-model-delete-options-dialog/lta'
                                                                   '-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                                   '1]/button')
        time.sleep(2)
        delete_button_window1.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                       '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                       '/app-model-delete-options-dialog/lta-modal-layout/div/lta'
                                                       '-modal/div[2]/lta-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + model_name + "')]")) == 0, 'Test' \
                                                                                                            'model ' \
                                                                                                            'was not ' \
                                                                                                            'deleted'
        print('Test model deleted')

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                             '/nav/ul/li[5]/a')))
        objects_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                            '/nav/ul/li[5]/a')
        objects_button.click()
        wait.until(ec.url_to_be(f'{env_url}conf/data/objects'))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Directory')]")))

        chevron_right_button = self.driver.find_element(By.XPATH, "//*[contains(text(),"
                                                                  "'" + object_name + "')]//parent::div//parent::div//child"
                                                                                      "::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + child_name + "')]")))
        child_untied_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + child_name + "')]")
        assert child_untied_object.text == f'{child_name} Directory', 'Untied object did not change model to Directory'
        print('Untied object model changed to Directory')

        root_object = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + object_name + "')]")
        root_object.click()

        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        time.sleep(2)
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-objects-page/lta-delete-dialog/lta-modal-layout/div'
                                                             '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-objects-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, 'btn.btn-icon.danger.md')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + object_name + "')]")) == 0, 'Root ' \
                                                                                                             'object ' \
                                                                                                             'was not ' \
                                                                                                             'deleted'
        print('Root object deleted')

        self.driver.quit()
