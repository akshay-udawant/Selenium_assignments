import time

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class ResizablePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_resizable(self, driver):
        resizable_element = driver.find_element(By.CSS_SELECTOR, ".ui-resizable-handle.ui-resizable-e")

        # Get the initial size of the resizable element
        initial_size = resizable_element.size

        # Perform the resize action (e.g., click and drag the resize handle)
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(resizable_element).move_by_offset(50, 50).release().perform()

        # Get the size of the resizable element after resizing
        final_size = resizable_element.size

        # Verify if the size has changed as expected
        if final_size != initial_size:
            print("Resize action successful!")
        else:
            print("Resize action failed!")
