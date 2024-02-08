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

class TestModel:
    print(f'TEST MODELS LAUNCHED ON {env_url}')

    @allure.description("Проверка работоспособности раздела 'Модели'")
    # simple model test
    @allure.title("Посещение раздела 'Модели' и его проверка")
    def test_model_0(self, models_page):
        print('"Models smoke test" launched...')
        self.driver = models_page

        try:
            models_tree = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/lta'
                                                             '-models-page/lta-header-layout/div/div['
                                                             '2]/lta-aside-layout/div[1]/lta-empty-panel/lta-tree')
        except:
            print('Models tree is missing, check it out!')

        boolean_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'Boolean')]")
        assert boolean_model.text == 'Boolean', 'Base model "Boolean" is missing'

        float_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'Float')]")
        assert float_model.text == 'Float', 'Base model "Float" is missing'

        string_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'String')]")
        assert string_model.text == 'String', 'Base model "String" is missing'

        directory_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'Directory')]")
        assert directory_model.text == 'Directory', 'Base model "Directory" is missing'

        print('"Models smoke test" passed')


    @allure.description("Проверка работоспособности раздела 'Модели'")
    # simple model test
    @allure.title("Создание простой модели, проверка и удаление")
    def test_model_1(self, get_webdriver):
        print('Simple model test launched...')
        self.driver = get_webdriver

        name = 'AutoTest_Model'
        description = 'Тестовая модель'

        wait = WebDriverWait(self.driver, 20, 0.5)

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        if same_models == 1:
            print(f'{same_models} model with the name {name} was found. Check it out!')

        while same_models != 0:
            name = name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        try:
            button_create_model_check = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        except:
            print('Create button is missing, check ot out!')

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Имя')]")))

        try:
            model_name_check = self.driver.find_element(By.CLASS_NAME, 'classes.ng-untouched.ng-pristine.ng-valid')
        except:
            print('Name input is missing, check it out!')

        model_name = self.driver.find_element(By.CLASS_NAME, 'classes.ng-untouched.ng-pristine.ng-valid')
        model_name.send_keys(name)

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Описание')]")))

        try:
            model_description_check = self.driver.find_element(By.CLASS_NAME, 'textarea.ng-untouched.ng-pristine.ng'
                                                                              '-valid')
        except:
            print('Description input is missing, check it out!')

        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.ng-untouched.ng-pristine.ng-valid')
        model_description.send_keys(description)

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Создать')]")))
        create_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Создать')]")
        create_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Создано')]")))

        print('Simple model created')

        cancel_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Отмена')]")
        cancel_button.click()

        time.sleep(1)

        created_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_model.text == f'{name}', 'Model was not created'
        print('Simple model checked')

        created_model.click()
        created_model.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Отмена')]")))

        try:
            delete_button_check = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        except:
            print('Delete button is missing, check it out!')

        delete_button = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.danger.md')
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))
        delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        delete_modal_button.click()

        time.sleep(2)

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))
        delete_modal_button = self.driver.find_element(By.XPATH, "//*[contains(text(),'Удалить')]")
        delete_modal_button.click()

        time.sleep(2)

        wait.until(ec.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'Удалить')]")))

        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Simple model ' \
                                                                                                      'was not deleted'
        print('Simple model deleted')
        print('"Simple model test" passed')

    # simple model component test
    @allure.description("Проверка работоспособности раздела 'Модели'")
    @allure.title("Создание простой модели, добавление в нее компонентов, проверка и удаление")
    def test_model_2(self, get_webdriver):
        print('Simple model component test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Model'
        description = 'Тестовая модель'
        wait = WebDriverWait(self.driver, 15, 0.5)

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_models != 0:
            name = name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        model_name = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")
        model_name.send_keys(name)
        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/div')))
        unroll_component_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/div')
        unroll_component_button.click()
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'btn.dashed.md')))
        add_component_button = self.driver.find_element(By.CLASS_NAME, 'btn.dashed.md')
        add_component_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/app-model-component-dialog/lta'
                                                             '-modal-layout/div/lta-modal/div[2]/lta-btn[1]/button')))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Arrow_Left ')]")))
        first_component = self.driver.find_element(By.XPATH, "//*[contains(text(),' Arrow_Left ')]")
        first_component.click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-models-page/header-layout/div/div['
                                                               '2]/aside-layout/div['
                                                               '2]/app-models-info-panel/app-model-component-dialog'
                                                               '/lta-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                               '2]/button')))
        add_component_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-models-page/header-layout/div/div['
                                                               '2]/aside-layout/div['
                                                               '2]/app-models-info-panel/app-model-component-dialog'
                                                               '/lta-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                               '2]/button')
        add_component_button_window.click()
        time.sleep(2)
        first_component_added = self.driver.find_element(By.XPATH, "//*[contains(text(),' Arrow_Left ')]")
        assert first_component_added.text == 'Arrow_Left', 'First component was not added'
        print('First component added')
        add_component_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/app-model-component-dialog/lta'
                                                             '-modal-layout/div/lta-modal/div[2]/lta-btn[1]/button')))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Pump / Right  ')]")))
        second_component = self.driver.find_element(By.XPATH, "//*[contains(text(),' Pump / Right  ')]")
        second_component.click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-models-page/header-layout/div/div['
                                                               '2]/aside-layout/div['
                                                               '2]/app-models-info-panel/app-model-component-dialog'
                                                               '/lta-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                               '2]/button')))
        add_component_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-models-page/header-layout/div/div['
                                                               '2]/aside-layout/div['
                                                               '2]/app-models-info-panel/app-model-component-dialog'
                                                               '/lta-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                               '2]/button')
        add_component_button_window.click()
        time.sleep(2)
        second_component_added = self.driver.find_element(By.XPATH, "//*[contains(text(),' Pump / Right ')]")
        assert second_component_added.text == 'Pump / Right', 'Second component was not added'
        print('Second component added')
        print('Simple model with components created and checked')
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))
        delete_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                 '/header-layout/div/div['
                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn[2]/button')
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/lta-delete-dialog/lta-modal-layout/div/lta'
                                                             '-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-models-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
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
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Simple model ' \
                                                                                                      'with ' \
                                                                                                      'components' \
                                                                                                      'was not deleted'
        print('Simple model with components deleted')

    #simple model name validation test
    @allure.description("Проверка работоспособности раздела 'Модели'")
    @allure.title("Создание двух простых моделей с одинаковыми именами, проверка и удаление")
    def test_model2(self, get_webdriver):
        print('Simple model name validation test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Model'
        description = 'Тестовая модель'
        wait = WebDriverWait(self.driver, 15, 0.5)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel/app-tree')))

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_models != 0:
            name = name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        model_name = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")
        model_name.send_keys(name)
        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('First simple model created')
        created_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_model.text == f'{name}', 'First simple model was not created'
        print('First simple model checked')
        cancel_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                           '-page/header-layout/div/div[2]/aside-layout/div['
                                                           '2]/app-models-info-panel/form/lta-save-cancel-panel/div'
                                                           '/lta-btn[1]/button')
        cancel_button.click()
        print('Trying to create second simple model with the same name...')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        model_name.send_keys(name)
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/lta-save-cancel-panel/div'
                                                             '/lta-btn[2]/button')))
        save_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                         '-page/header-layout/div/div[2]/aside-layout/div['
                                                         '2]/app-models-info-panel/form/lta-save-cancel-panel/div/lta'
                                                         '-btn[2]/button')
        save_button.click()
        time.sleep(5)
        number_of_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        assert number_of_models == 1, F'Two simple ' \
                                                                                                     F'models with ' \
                                                                                                     F'the name ' \
                                                                                                     F'{name} were ' \
                                                                                                     F'created, ' \
                                                                                                     F'need to fix'
        print('There is only one simple model with the name', name)

        simple_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        simple_model.click()
        simple_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page'
                                                             '/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))
        delete_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                 '/header-layout/div/div['
                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn[2]/button')
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
                                                         '-page/app-model-delete-options-dialog/lta-modal-layout/div'
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
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'First simple ' \
                                                                                                      'model ' \
                                                                                                      'was not deleted'
        print('First simple model deleted')

    # complex model test
    @allure.description("Проверка работоспособности раздела 'Модели'")
    @allure.title("Создание сложной модели, содержащей две дочерние модели по каждой базовой модели, удаление одной из дочерних моделей, проверка и удаление сложной модели")
    def test_model3(self, get_webdriver):
        print('Complex model test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Model'
        description = 'Тестовая модель'
        wait = WebDriverWait(self.driver, 15, 0.5)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                             '-page/header-layout/div/div[2]/aside-layout/div['
                                                             '1]/lta-empty-panel/app-tree')))

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_models != 0:
            name = name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        model_name = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")
        model_name.send_keys(name)
        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        cancel_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
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
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")
        sub_model_name.send_keys('Test_boolean1')
        sub_model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        sub_model_description.send_keys('Дочерняя модель по модели Boolean #1')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta-spoiler-panel/div'
                                                             '/form/lta-select/label/span[2]/span/span[2]/span[1]')))
        sub_model_boolean_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta-spoiler-panel/div'
                                                             '/form/lta-select/label/span[2]/span/span[2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_boolean1 ')]")))
        print('Sub model boolean1 created')
        sub_model_boolean1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_boolean1 ')]")
        assert sub_model_boolean1.text == 'Test_boolean1', 'Sub model boolean 1 ' \
                                                                                                'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_boolean2')
        sub_model_description.send_keys('Дочерняя модель по модели Boolean #2')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta-spoiler-panel/div'
                                                             '/form/lta-select/label/span[2]/span/span[2]/span[1]')))
        sub_model_boolean_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta-spoiler-panel/div'
                                                             '/form/lta-select/label/span[2]/span/span[2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_boolean2 ')]")))
        print('Sub model boolean2 created')
        sub_model_boolean2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_boolean2 ')]")
        assert sub_model_boolean2.text == 'Test_boolean2', 'Sub model boolean 2 ' \
                                                                                                'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_directory1')
        sub_model_description.send_keys('Дочерняя модель по модели Directory #1')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/lta'
                                                                        '-spoiler-panel/div/form/lta-select/label'
                                                                        '/span[2]/span/span[2]/span[4]')))
        sub_model_directory_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/lta'
                                                                        '-spoiler-panel/div/form/lta-select/label'
                                                                        '/span[2]/span/span[2]/span[4]')
        sub_model_directory_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_directory1 ')]")))
        print('Sub model directory1 created')
        sub_model_directory1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_directory1 ')]")
        assert sub_model_directory1.text == 'Test_directory1', 'Sub model ' \
                                                                                                      'directory 1 ' \
                                                                                                      'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_directory2')
        sub_model_description.send_keys('Дочерняя модель по модели Directory #2')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                             '/main/app-models-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta'
                                                             '-spoiler-panel/div/form/lta-select/label'
                                                             '/span[2]/span/span[2]/span[4]')))
        sub_model_directory_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/lta'
                                                                        '-spoiler-panel/div/form/lta-select/label'
                                                                        '/span[2]/span/span[2]/span[4]')
        sub_model_directory_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_directory2 ')]")))
        print('Sub model directory2 created')
        sub_model_directory2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_directory2 ')]")
        assert sub_model_directory2.text == 'Test_directory2', 'Sub model ' \
                                                                                                      'directory 2 ' \
                                                                                                      'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_float1')
        sub_model_description.send_keys('Дочерняя модель по модели Float #1')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                    '/app-models-page/header-layout/div/div['
                                                                    '2]/aside-layout/div['
                                                                    '2]/app-models-info-panel/form/div/lta-spoiler'
                                                                    '-panel/div/form/lta-select/label/span['
                                                                    '2]/span/span[2]/span[2]')))
        sub_model_float_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                    '/app-models-page/header-layout/div/div['
                                                                    '2]/aside-layout/div['
                                                                    '2]/app-models-info-panel/form/div/lta-spoiler'
                                                                    '-panel/div/form/lta-select/label/span['
                                                                    '2]/span/span[2]/span[2]')
        sub_model_float_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_float1 ')]")))
        print('Sub model float1 created')
        sub_model_float1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_float1 ')]")
        assert sub_model_float1.text == 'Test_float1', 'Sub model ' \
                                                                                          'float 1 ' \
                                                                                          'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_float2')
        sub_model_description.send_keys('Дочерняя модель по модели Float #2')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                             '/app-models-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta-spoiler'
                                                             '-panel/div/form/lta-select/label/span['
                                                             '2]/span/span[2]/span[2]')))
        sub_model_float_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                    '/app-models-page/header-layout/div/div['
                                                                    '2]/aside-layout/div['
                                                                    '2]/app-models-info-panel/form/div/lta-spoiler'
                                                                    '-panel/div/form/lta-select/label/span['
                                                                    '2]/span/span[2]/span[2]')
        sub_model_float_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_float2 ')]")))
        print('Sub model float2 created')
        sub_model_float2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_float2 ')]")
        assert sub_model_float2.text == 'Test_float2', 'Sub model ' \
                                                                                          'float 2 ' \
                                                                                          'was not created'
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_string1')
        sub_model_description.send_keys('Дочерняя модель по модели String #1')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                     '/app-models-page/header-layout/div/div['
                                                                     '2]/aside-layout/div['
                                                                     '2]/app-models-info-panel/form/div/lta-spoiler'
                                                                     '-panel/div/form/lta-select/label/span['
                                                                     '2]/span/span[2]/span[3]')))
        sub_model_string_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                     '/app-models-page/header-layout/div/div['
                                                                     '2]/aside-layout/div['
                                                                     '2]/app-models-info-panel/form/div/lta-spoiler'
                                                                     '-panel/div/form/lta-select/label/span['
                                                                     '2]/span/span[2]/span[3]')
        sub_model_string_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_string1 ')]")))
        print('Sub model string1 created')
        sub_model_string1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_string1 ')]")
        assert sub_model_string1.text == 'Test_string1', 'Sub model ' \
                                                                                             'string 1 ' \
                                                                                             'was not created'
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_string2')
        sub_model_description.send_keys('Дочерняя модель по модели String #2')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                             '/app-models-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta-spoiler'
                                                             '-panel/div/form/lta-select/label/span['
                                                             '2]/span/span[2]/span[3]')))
        sub_model_string_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                     '/app-models-page/header-layout/div/div['
                                                                     '2]/aside-layout/div['
                                                                     '2]/app-models-info-panel/form/div/lta-spoiler'
                                                                     '-panel/div/form/lta-select/label/span['
                                                                     '2]/span/span[2]/span[3]')
        sub_model_string_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_string2 ')]")))
        print('Sub model string2 created')
        sub_model_string2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_string2 ')]")
        assert sub_model_string2.text == 'Test_string2', 'Sub model ' \
                                                                                             'string 2 ' \
                                                                                             'was not created'
        print('Complex model created and checked')

        delete_button_last_sub_model = self.driver.find_element(By.XPATH,
                                                                '/html/body/app-root/app-admin-layout/div/main/app'
                                                                '-models-page'
                                                                '/header-layout/div/div['
                                                                '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                                '2]/button')
        delete_button_last_sub_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/lta-delete-dialog/lta-modal-layout/div/lta'
                                                             '-modal/div[2]/lta-btn[2]/button')))
        delete_button_last_sub_model_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin'
                                                                                 '-layout/div/main/app'
                                                                                 '-models-page/lta-delete-dialog/lta'
                                                                                 '-modal-layout'
                                                                                 '/div/lta-modal/div[2]/lta-btn['
                                                                                 '2]/button')
        time.sleep(2)
        delete_button_last_sub_model_window.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                 '-models-page/header-layout/div/div['
                                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta'
                                                                 '-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),' Test_string2 ')]")) == 0, 'Sub model ' \
                                                                                                        'string2 ' \
                                                                                                        'was not ' \
                                                                                                        'deleted'
        print('Sub model string2 deleted')
        complex_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        complex_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page'
                                                             '/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))
        delete_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                 '/header-layout/div/div['
                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn[2]/button')
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/lta-delete-dialog/lta-modal-layout/div/lta'
                                                             '-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-models-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
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
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Complex model ' \
                                                                                                      'was not deleted'
        print('Complex model deleted')

    #Complex model child models name validation test
    @allure.description("Проверка работоспособности раздела 'Модели'")
    @allure.title("Создание сложной моедели с двумя дочерними моделями с одинаковыми именами, проверка и удаление")
    def test_model4(self, get_webdriver):
        print('Complex model child models name validation test launched...')
        self.driver = get_webdriver
        name = 'AutoTest_Model'
        description = 'Тестовая модель'
        wait = WebDriverWait(self.driver, 15, 0.5)

        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                          '-page/header-layout/div/div[2]/aside-layout/div['
                                                          '1]/lta-empty-panel/app-tree')))

        same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))
        while same_models != 0:
            name = name + str(random.randint(0, 100))
            same_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]"))

        button_create_model = self.driver.find_element(By.CLASS_NAME, 'btn.btn-icon.primary.md')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        model_name = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")
        model_name.send_keys(name)
        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
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
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name = self.driver.find_element(By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")
        sub_model_name.send_keys('Test_sub_model1')
        sub_model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm.ng-valid.ng-dirty.ng-touched')
        sub_model_description.send_keys('Дочерняя модель #1')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH,'/html/body/app-root/app-admin-layout/div/main/app'
                                                                '-models-page/header-layout/div/div['
                                                                '2]/aside-layout/div['
                                                                '2]/app-models-info-panel/form/div/lta-spoiler-panel'
                                                                '/div/form/lta-select/label/span[2]/span/span['
                                                                '2]/span[1]')))
        sub_model_boolean_choose = self.driver.find_element(By.XPATH,
                                                                '/html/body/app-root/app-admin-layout/div/main/app'
                                                                '-models-page/header-layout/div/div['
                                                                '2]/aside-layout/div['
                                                                '2]/app-models-info-panel/form/div/lta-spoiler-panel'
                                                                '/div/form/lta-select/label/span[2]/span/span['
                                                                '2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_sub_model1 ')]")))
        print('Sub model #1 created')
        sub_model_boolean1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_sub_model1 ')]")
        assert sub_model_boolean1.text == 'Test_sub_model1', 'Sub model #1 ' \
                                                                                                    'was not created'
        print('Trying to create second sub model with the same name...')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/app-root/app-admin-layout/div/main/app"
                                                             "-models-page/header-layout/div/div[2]/aside-layout/div["
                                                             "2]/app-models-info-panel/form/div/lta-spoiler-panel/div"
                                                             "/form/lta-input/label/span[2]/input")))
        sub_model_name.send_keys('Test_sub_model1')
        sub_model_description.send_keys('Дочерняя модель #2')
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME, 'input.sm')))
        models_list.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div['
                                                             '2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/lta-spoiler-panel'
                                                             '/div/form/lta-select/label/span[2]/span/span['
                                                             '2]/span[1]')))
        sub_model_boolean_choose = self.driver.find_element(By.XPATH,
                                                            '/html/body/app-root/app-admin-layout/div/main/app'
                                                            '-models-page/header-layout/div/div['
                                                            '2]/aside-layout/div['
                                                            '2]/app-models-info-panel/form/div/lta-spoiler-panel'
                                                            '/div/form/lta-select/label/span[2]/span/span['
                                                            '2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        number_of_sub_models = len(self.driver.find_elements(By.XPATH, "//*[contains(text(),' Test_sub_model1 ')]"))
        assert number_of_sub_models == 1, 'There are two sub models with the same name, need to fix'
        print('Second sub model with the same name was not created')
        complex_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        complex_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page'
                                                             '/header-layout/div/div['
                                                             '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn['
                                                             '2]/button')))
        delete_button = self.driver.find_element(By.XPATH,
                                                 '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                 '/header-layout/div/div['
                                                 '1]/lta-header-panel/div/lta-empty-panel/div/lta-btn[2]/button')
        delete_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/lta-delete-dialog/lta-modal-layout/div/lta'
                                                             '-modal/div[2]/lta-btn[2]/button')))
        delete_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                  '-models-page/lta-delete-dialog/lta-modal-layout'
                                                                  '/div/lta-modal/div[2]/lta-btn[2]/button')
        time.sleep(2)
        delete_button_window.click()
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
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Complex model ' \
                                                                                                      'was not deleted'
        print('Complex model deleted')

        self.driver.close()
        self.driver.quit()