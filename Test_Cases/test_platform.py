import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestPlatform:
    print('TEST LTA PLATFORM LAUNCHED')

    def test_platform(self, authorization):
        self.driver = authorization
        wait = WebDriverWait(self.driver, 10, 0.3)

        #settings
        print("Settings are being tested...")
        button_settings = self.driver.find_element(By.XPATH, '/html/body/app-root/app-main-page/toolbar/div/div['
                                                            '3]/div[4]/svg-icon')
        button_settings.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/settings/figma'))
        button_settings_main = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/main/app'
                                                                 '-settings-page/header-layout/div/div['
                                                                 '2]/aside-layout/div['
                                                                 '2]/lta-empty-panel/app-settings-menu/ul/li[1]/a')
        button_settings_main.click()
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                          '/main/app-settings-page/header-layout/div'
                                                                          '/div[2]/aside-layout/div['
                                                                          '1]/div/div/lta-empty-panel/app-main'
                                                                          '-settings/form/lta-select')))
        print('SETTINGS ARE ACTIVE')

        #services
        print("Services are being tested...")
        button_services = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                            '/nav/ul/li[12]')
        button_services.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/services'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                           '/main/app-services-page/header-layout/div'
                                                                           '/div[2]/aside-layout/div['
                                                                           '1]/app-services-table/lta-table-view/div')))
        print('SERVICES ARE ACTIVE')

        #alerts
        print("Alerts are being tested...")
        button_alerts = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                          '/nav/ul/li[11]/a')
        button_alerts.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/alerts'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                         '/main/app-alerts-page/header-layout/div'
                                                                         '/div[2]/aside-layout/div['
                                                                         '1]/app-alerts-table/lta-table-view')))
        print('ALERTS ARE ACTIVE')

        #cluster
        print("Cluster is being tested...")
        button_cluster = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                           '/nav/ul/li[10]/a')
        button_cluster.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/cluster'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                          '/main/app-cluster-page/header-layout/div'
                                                                          '/div[2]/app-cluster-table/lta-table-view')))
        print('CLUSTER IS ACTIVE')

        #driver_types
        print('Driver types are being tested...')
        button_driver_types = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu'
                                                                '/aside/nav/ul/li[9]/a')
        button_driver_types.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/driver-types'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout'
                                                                               '/div/main/app-driver-types/header'
                                                                               '-layout/div/div[2]/aside-layout/div['
                                                                               '1]/app-driver-types-table/lta-table'
                                                                               '-view')))
        print('DRIVER TYPES ARE ACTIVE')

        #drivers
        print('Drivers are being tested...')
        button_drivers = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                           '/nav/ul/li[8]/a')
        button_drivers.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/drivers'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                          '/main/app-drivers-page/header-layout/div'
                                                                          '/div[2]/aside-layout/div['
                                                                          '1]/app-drivers-table/lta-table-view')))
        print('DRIVERS ARE ACTIVE')

        #components
        print('Components are being tested...')
        components_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu'
                                                              '/aside/nav/ul/li[7]/a')
        components_button.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/hmi/components'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout'
                                                                             '/div/main/app-hmi-components-dashboard'
                                                                             '/header-layout/div/div[2]')))
        print('COMPONENTS ARE ACTIVE')

        #hmi
        print('HMI is being tested...')
        hmi_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav'
                                                       '/ul/li[6]/a')
        hmi_button.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/hmi/screens'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div/main'
                                                                      '/app-hmi-dashboard/header-layout/div/div[2]')))
        print('HMI IS ACTIVE')

        #models
        print('Models are being tested...')
        models_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                          '/nav/ul/li[5]/a')
        models_button.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/data/models'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                         '/main/app-models-page/header-layout/div'
                                                                         '/div[2]/aside-layout/div['
                                                                         '1]/lta-empty-panel')))
        print('MODELS ARE ACTIVE')

        #objects
        print('Objects are being tested...')
        objects_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside'
                                                           '/nav/ul/li[4]/a')
        objects_button.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/data/objects'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                          '/main/app-objects-page/header-layout/div'
                                                                          '/div[2]/aside-layout/div['
                                                                          '1]/lta-empty-panel')))
        print('OBJECTS ARE ACTIVE')

        #roles
        print('Roles are being tested...')
        roles_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav'
                                                         '/ul/li[3]/a')
        roles_button.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/user-administration/roles'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-roles-page/header-layout/div/div['
                                                                        '2]')))
        print('ROLES ARE ACTIVE')

        #users
        print('Users are being tested...')
        users_button = self.driver.find_element(By.XPATH, '/html/body/app-root/app-admin-layout/div/app-menu/aside/nav'
                                                         '/ul/li[2]/a')
        users_button.click()
        wait.until(ec.url_to_be('http://185.221.152.176/conf/user-administration/users'))
        wait.until(ec.presence_of_element_located((By.XPATH, '/html/body/app-root/app-admin-layout/div'
                                                                        '/main/app-users-page/header-layout/div/div['
                                                                        '2]/aside-layout')))
        print('USERS ARE ACTIVE')

        self.driver.quit()

        print('ALL LTA PLATFORM SECTIONS ACT PROPERLY')