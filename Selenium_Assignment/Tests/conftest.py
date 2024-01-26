
import pytest
from selenium import webdriver


@pytest.fixture
def init_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
