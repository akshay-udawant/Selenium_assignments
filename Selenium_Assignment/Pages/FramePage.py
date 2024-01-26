import time

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class FramePage(BasePage):
    # FRAME_NAME = (By.ID, "frame-one796456169")
    # ELEMENT = (By.ID, "RESULT_TextField-0")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def frame_data(self, driver):
        # self.driver.switch_to.frame(self.FRAME_NAME)
        # self.ELEMENT.send_keys("akshay")
        # time.sleep(4)
        driver.switch_to.frame(driver.find_element(By.ID, "frame-one796456169"))
        element = driver.find_element(By.ID, "RESULT_TextField-0")
        element.send_keys("akshay")
        time.sleep(4)