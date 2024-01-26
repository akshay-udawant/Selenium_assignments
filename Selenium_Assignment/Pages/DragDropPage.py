import time

from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class DragDropPage(BasePage):
    # DRAG_ELEMENT = (By.XPATH, "//div[@id='draggable']")
    # DROP_ELEMENT = (By.XPATH, "//div[@id='droppable']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_drag_drop(self, driver):

        draggable_element = driver.find_element(By.XPATH, "//div[@id='draggable']")
        target_element = driver.find_element(By.XPATH, "//div[@id='droppable']")

        actions = ActionChains(driver)
        actions.drag_and_drop(draggable_element, target_element).perform()