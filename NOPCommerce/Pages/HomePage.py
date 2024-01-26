

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Tests.test_base import BaseTest


class HomePage(BasePage):
    BUILD_YOUR_OWN_COMPUTER = (By.XPATH, "//h2/a[contains(text(),'Build your own computer')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    def go_to_build_your_own_computer(self):
        self.do_click(self.BUILD_YOUR_OWN_COMPUTER)
