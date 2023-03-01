from base.selenium_base import SeleniumBase

class HomepageNav(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
