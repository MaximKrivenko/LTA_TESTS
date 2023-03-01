import pytest
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestModel:
    # simple model test
    def test_model(self, models_page):
        print('Simple model test launched...')
        self.driver = models_page
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@class='classes']")))
        model_name = self.driver.find_element(By.XPATH, "//input[@class='classes']")
        model_name.send_keys(name)
        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('Simple model created')
        created_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_model.text == f'{name} Тестовая модель', 'Model was not created'
        print('Simple model checked')
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
        delete_button_window1.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                       '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                       '/app-model-delete-options-dialog/lta-modal-layout/div/lta'
                                                       '-modal/div[2]/lta-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Simple model ' \
                                                                                                      'was not deleted'
        print('Simple model deleted')
        self.driver.close()

    # simple model component test
    def test_model1(self, models_page):
        print('Simple model component test launched...')
        self.driver = models_page
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@class='classes']")))
        model_name = self.driver.find_element(By.XPATH, "//input[@class='classes']")
        model_name.send_keys(name)
        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.dashed.md')))
        add_component_button = self.driver.find_element(By.CLASS_NAME, 'btn.dashed.md')
        add_component_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/app-model-component-dialog/lta'
                                                             '-modal-layout/div/lta-modal/div[3]/lta-btn[1]/button')))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Arrow_Left ')]")))
        first_component = self.driver.find_element(By.XPATH, "//*[contains(text(),' Arrow_Left ')]")
        first_component.click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-models-page/header-layout/div/div['
                                                               '2]/aside-layout/div['
                                                               '2]/app-models-info-panel/app-model-component-dialog'
                                                               '/lta-modal-layout/div/lta-modal/div[3]/lta-btn['
                                                               '2]/button')))
        add_component_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                         '/main/app-models-page/header-layout/div'
                                                                         '/div[2]/aside-layout/div['
                                                                         '2]/app-models-info-panel/app-model'
                                                                         '-component-dialog/lta-modal-layout/div/lta'
                                                                         '-modal/div[3]/lta-btn[2]/button')
        add_component_button_window.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/div/div['
                                                             '2]/app-model-component-widget/div/div[2]/lta-btn['
                                                             '1]/button')))
        first_component_added = self.driver.find_element(By.XPATH, "//*[contains(text(),' Arrow_Left ')]")
        assert first_component_added.text == 'Arrow_Left', 'First component was not added'
        print('First component added')
        add_component_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/app-model-component-dialog/lta'
                                                             '-modal-layout/div/lta-modal/div[3]/lta-btn[1]/button')))
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Pump / Right  ')]")))
        second_component = self.driver.find_element(By.XPATH, "//*[contains(text(),' Pump / Right  ')]")
        second_component.click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                               '-models-page/header-layout/div/div['
                                                               '2]/aside-layout/div['
                                                               '2]/app-models-info-panel/app-model-component-dialog'
                                                               '/lta-modal-layout/div/lta-modal/div[3]/lta-btn['
                                                               '2]/button')))
        add_component_button_window = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                         '/main/app-models-page/header-layout/div'
                                                                         '/div[2]/aside-layout/div['
                                                                         '2]/app-models-info-panel/app-model'
                                                                         '-component-dialog/lta-modal-layout/div/lta'
                                                                         '-modal/div[3]/lta-btn[2]/button')
        add_component_button_window.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/div/div['
                                                             '2]/app-model-component-widget/div/div[2]/lta-btn['
                                                             '1]/button')))
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
        delete_button_window.click()
        wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                         '-page/app-model-delete-options-dialog/lta-modal-layout/div'
                                                         '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window1 = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                   '-models-page/app-model-delete-options-dialog/lta'
                                                                   '-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                                   '2]/button')
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
        self.driver.quit()

    #simple model name validation test
    def test_model2(self, models_page):
        print('Simple model name validation test launched...')
        self.driver = models_page
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@class='classes']")))
        model_name = self.driver.find_element(By.XPATH, "//input[@class='classes']")
        model_name.send_keys(name)
        model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        model_description.send_keys(description)
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),'" + name + "')]")))
        print('First simple model created')
        created_model = self.driver.find_element(By.XPATH, "//*[contains(text(),'" + name + "')]")
        assert created_model.text == f'{name} Тестовая модель', 'First simple model was not created'
        print('First simple model checked')
        cancel_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                           '-page/header-layout/div/div[2]/aside-layout/div['
                                                           '2]/app-models-info-panel/form/lta-save-cancel-panel/div'
                                                           '/lta-btn[1]/button')
        cancel_button.click()
        print('Trying to create second simple model with the same name...')
        button_create_model.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                             '-models-page/header-layout/div/div[2]/aside-layout/div['
                                                             '2]/app-models-info-panel/form/div/form/lta-input/label'
                                                             '/span[2]/input')))
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
        print('There is only one simple model with the name', name, 'created')

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
        delete_button_window1.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                       '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                       '/app-model-delete-options-dialog/lta-modal-layout/div/lta'
                                                       '-modal/div[2]/lta-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'First simple ' \
                                                                                                      'model ' \
                                                                                                      'was not deleted'
        print('First simple model deleted')
        self.driver.close()

    # complex model test
    def test_model3(self, models_page):
        print('Complex model test launched...')
        self.driver = models_page
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@class='classes']")))
        model_name = self.driver.find_element(By.XPATH, "//input[@class='classes']")
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
                                                                  "'" + name + "')]//parent::div//parent::div//child"
                                                                               "::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name = self.driver.find_element(By.CLASS_NAME, 'classes.error')
        sub_model_name.send_keys('Test_boolean1')
        sub_model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        sub_model_description.send_keys('Дочерняя модель по модели Boolean #1')
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_boolean1 ')]")))
        print('Sub model boolean1 created')
        sub_model_boolean1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_boolean1 ')]")
        assert sub_model_boolean1.text == 'Test_boolean1 Дочерняя модель по модели Boolean #1', 'Sub model boolean 1 ' \
                                                                                                'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_boolean2')
        sub_model_description.send_keys('Дочерняя модель по модели Boolean #2')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_boolean_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                      '/app-models-page/header-layout/div/div['
                                                                      '2]/aside-layout/div['
                                                                      '2]/app-models-info-panel/form/div/form/lta'
                                                                      '-select/label/span[2]/span/span[2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_boolean2 ')]")))
        print('Sub model boolean2 created')
        sub_model_boolean2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_boolean2 ')]")
        assert sub_model_boolean2.text == 'Test_boolean2 Дочерняя модель по модели Boolean #2', 'Sub model boolean 2 ' \
                                                                                                'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_directory1')
        sub_model_description.send_keys('Дочерняя модель по модели Directory #1')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_directory_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/form/lta'
                                                                        '-select/label/span[2]/span/span[2]/span[2]')
        sub_model_directory_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_directory1 ')]")))
        print('Sub model directory1 created')
        sub_model_directory1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_directory1 ')]")
        assert sub_model_directory1.text == 'Test_directory1 Дочерняя модель по модели Directory #1', 'Sub model ' \
                                                                                                      'directory 1 ' \
                                                                                                      'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_directory2')
        sub_model_description.send_keys('Дочерняя модель по модели Directory #2')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_directory_choose = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-models-page/header-layout/div/div['
                                                                        '2]/aside-layout/div['
                                                                        '2]/app-models-info-panel/form/div/form/lta'
                                                                        '-select/label/span[2]/span/span[2]/span[2]')
        sub_model_directory_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_directory2 ')]")))
        print('Sub model directory2 created')
        sub_model_directory2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_directory2 ')]")
        assert sub_model_directory2.text == 'Test_directory2 Дочерняя модель по модели Directory #2', 'Sub model ' \
                                                                                                      'directory 2 ' \
                                                                                                      'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_float1')
        sub_model_description.send_keys('Дочерняя модель по модели Float #1')
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_float1 ')]")))
        print('Sub model float1 created')
        sub_model_float1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_float1 ')]")
        assert sub_model_float1.text == 'Test_float1 Дочерняя модель по модели Float #1', 'Sub model ' \
                                                                                          'float 1 ' \
                                                                                          'was not created'

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_float2')
        sub_model_description.send_keys('Дочерняя модель по модели Float #2')
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_float2 ')]")))
        print('Sub model float2 created')
        sub_model_float2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_float2 ')]")
        assert sub_model_float2.text == 'Test_float2 Дочерняя модель по модели Float #2', 'Sub model ' \
                                                                                          'float 2 ' \
                                                                                          'was not created'
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_string1')
        sub_model_description.send_keys('Дочерняя модель по модели String #1')
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_string1 ')]")))
        print('Sub model string1 created')
        sub_model_string1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_string1 ')]")
        assert sub_model_string1.text == 'Test_string1 Дочерняя модель по модели String #1', 'Sub model ' \
                                                                                             'string 1 ' \
                                                                                             'was not created'
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_string2')
        sub_model_description.send_keys('Дочерняя модель по модели String #2')
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_string2 ')]")))
        print('Sub model string2 created')
        sub_model_string2 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_string2 ')]")
        assert sub_model_string2.text == 'Test_string2 Дочерняя модель по модели String #2', 'Sub model ' \
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
        delete_button_window.click()
        wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                         '-page/app-model-delete-options-dialog/lta-modal-layout/div'
                                                         '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window1 = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                   '-models-page/app-model-delete-options-dialog/lta'
                                                                   '-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                                   '2]/button')
        delete_button_window1.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                       '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                       '/app-model-delete-options-dialog/lta-modal-layout/div/lta'
                                                       '-modal/div[2]/lta-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Complex model ' \
                                                                                                      'was not deleted'
        print('Complex model deleted')

        self.driver.close()

    #Complex model child models name validation test
    def test_model4(self, models_page):
        print('Complex model child models name validation test launched...')
        self.driver = models_page
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
        wait.until(ec.presence_of_element_located((By.XPATH, "//input[@class='classes']")))
        model_name = self.driver.find_element(By.XPATH, "//input[@class='classes']")
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
                                                                      "'" + name + "')]//parent::div//parent::div//child"
                                                                                   "::span//child::svg-icon")
        chevron_right_button.click()

        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name = self.driver.find_element(By.CLASS_NAME, 'classes.error')
        sub_model_name.send_keys('Test_sub_model1')
        sub_model_description = self.driver.find_element(By.CLASS_NAME, 'textarea.sm')
        sub_model_description.send_keys('Дочерняя модель #1')
        models_list = self.driver.find_element(By.CLASS_NAME, 'input.sm')
        models_list.click()
        sub_model_boolean_choose = self.driver.find_element(By.XPATH,
                                                                '/html/body/app-root/app-admin-layout/div/main'
                                                                '/app-models-page/header-layout/div/div['
                                                                '2]/aside-layout/div['
                                                                '2]/app-models-info-panel/form/div/form/lta'
                                                                '-select/label/span[2]/span/span[2]/span[1]')
        sub_model_boolean_choose.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'btn.success.md')))
        save_button = self.driver.find_element(By.CLASS_NAME, 'btn.success.md')
        save_button.click()
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Test_sub_model1 ')]")))
        print('Sub model #1 created')
        sub_model_boolean1 = self.driver.find_element(By.XPATH, "//*[contains(text(),' Test_sub_model1 ')]")
        assert sub_model_boolean1.text == 'Test_sub_model1 Дочерняя модель #1', 'Sub model #1 ' \
                                                                                                    'was not created'
        print('Trying to create second sub model with the same name...')
        wait.until(ec.presence_of_element_located((By.XPATH, "//*[contains(text(),' Новая модель ')]")))
        sub_model_button = self.driver.find_element(By.XPATH, "//*[contains(text(),' Новая модель ')]")
        sub_model_button.click()
        wait.until(ec.presence_of_element_located((By.CLASS_NAME, 'classes.error')))
        sub_model_name.send_keys('Test_sub_model1')
        sub_model_description.send_keys('Дочерняя модель #2')
        models_list.click()
        sub_model_boolean_choose = self.driver.find_element(By.XPATH,
                                                                '/html/body/app-root/app-admin-layout/div/main'
                                                                '/app-models-page/header-layout/div/div['
                                                                '2]/aside-layout/div['
                                                                '2]/app-models-info-panel/form/div/form/lta'
                                                                '-select/label/span[2]/span/span[2]/span[1]')
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
        delete_button_window.click()
        wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app-models'
                                                         '-page/app-model-delete-options-dialog/lta-modal-layout/div'
                                                         '/lta-modal/div[2]/lta-btn[2]/button')))
        delete_button_window1 = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                   '-models-page/app-model-delete-options-dialog/lta'
                                                                   '-modal-layout/div/lta-modal/div[2]/lta-btn['
                                                                   '2]/button')
        delete_button_window1.click()
        wait.until(ec.invisibility_of_element_located((By.XPATH,
                                                       '/html/body/app-root/app-admin-layout/div/main/app-models-page'
                                                       '/app-model-delete-options-dialog/lta-modal-layout/div/lta'
                                                       '-modal/div[2]/lta-btn[2]/button')))
        assert len(self.driver.find_elements(By.XPATH, "//*[contains(text(),'" + name + "')]")) == 0, 'Complex model ' \
                                                                                                      'was not deleted'
        print('Complex model deleted')

        self.driver.close()