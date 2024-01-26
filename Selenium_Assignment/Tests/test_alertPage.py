import pytest

from Config.config import TestData
from Pages.AlertPage import AlertPage
from Pages.TextFieldPage import TextFieldPage
from Tests.test_base import BaseTest


class Test_AlertPage(BaseTest):

    def test_alert_button(self):
        self.alertPage = AlertPage(self.driver)
        self.alertPage.do_alert(self.driver)

    def test_confirm_alert_box_button(self):
        self.alertPage = AlertPage(self.driver)
        self.alertPage.do_alert_confirm_box(self.driver)

    def test_prompt_button(self):
        self.alertPage = AlertPage(self.driver)
        self.alertPage.do_prompt_button(self.driver)
