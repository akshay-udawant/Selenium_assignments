import pytest

from Config.config import TestData
from Pages.TextFieldPage import TextFieldPage
from Tests.test_base import BaseTest


class Test_TextFields(BaseTest):

    def test_text_fields(self):
        self.textFields = TextFieldPage(self.driver)
        self.textFields.enter_textfield_data(TestData.NAME, TestData.EMAIL, TestData.PHONE, TestData.ADDRESS)



