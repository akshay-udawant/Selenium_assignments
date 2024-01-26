import time

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver

class AlertPage(BasePage):

    ALERT_BUTTON = (By.XPATH, "//button[normalize-space()='Alert']")
    CONFIRM_ALERT_BUTTON = (By.XPATH, "//button[normalize-space()='Confirm Box']")
    PROMPT_BUTTON = (By.XPATH, "//button[normalize-space()='Prompt']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_alert(self, driver):
        self.do_click(self.ALERT_BUTTON)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        assert alert.text == "I am an alert box!"
        time.sleep(2)
        alert.accept()
        time.sleep(4)

    def do_alert_confirm_box(self, driver):
        self.do_click(self.CONFIRM_ALERT_BUTTON)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        assert alert.text == "Press a button!"
        time.sleep(2)
        alert.accept()
        time.sleep(4)

    def do_prompt_button(self, driver):
        self.do_click(self.PROMPT_BUTTON)
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(4)