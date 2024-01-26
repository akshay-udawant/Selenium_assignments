import time

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class TextFieldPage(BasePage):

    NAME_TEXT_FIELD =(By.ID, "name")
    EMAIL_TEXT_FIELD = (By.ID, "email")
    PHONE_TEXT_FIELD = (By.ID, "phone")
    ADDRESS_TEXT_FIELD = (By.ID, "textarea")
    GENDER_RADIO_BUTTON = (By.ID, "male")
    SUNDAY_CHEKBOX = (By.ID, "sunday")
    MONDAY_CHEKBOX = (By.ID, "monday")
    COUNTRY_DROPDOWN = (By.ID, "country")
    BLUE_COLORS = (By.XPATH, "//option[@value='blue']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def enter_textfield_data(self, name, email, phone, address):
        self.do_send_keys(self.NAME_TEXT_FIELD, name)
        self.do_send_keys(self.EMAIL_TEXT_FIELD, email)
        self.do_send_keys(self.PHONE_TEXT_FIELD, phone)
        self.do_send_keys(self.ADDRESS_TEXT_FIELD, address)
        self.do_click(self.GENDER_RADIO_BUTTON)
        self.do_click(self.SUNDAY_CHEKBOX)
        self.do_click(self.MONDAY_CHEKBOX)
        self.get_dropdown_element(self.COUNTRY_DROPDOWN)
        self.do_click(self.BLUE_COLORS)
        time.sleep(4)
        # self.do_click(self.LOGIN_BUTTON)