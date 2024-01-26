from Config.config import TestData
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DoubleClickPage(BasePage):
    # BUTTON = (By.XPATH, "//button[normalize-space()='Copy Text']")
    # FIELD1 = (By.ID, "field1")
    # FIELD2 = (By.ID, "field2")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_double_click(self, driver):
        button = self.driver.find_element("xpath", "//button[normalize-space()='Copy Text']")

        # Find Field1 and Field2 elements
        field1 = self.driver.find_element("id", "field1")
        field2 = self.driver.find_element("id", "field2")
        action_chains = ActionChains(self.driver)
        action_chains.double_click(button).perform()

        # Copy text from Field1 to Field2
        text_to_copy = field1.get_attribute("value")
        driver.execute_script("arguments[0].value = arguments[1]", field2, text_to_copy)
