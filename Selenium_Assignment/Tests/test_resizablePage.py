import pytest
from Pages.ResizablePage import ResizablePage
from Tests.test_base import BaseTest


class Test_Resizable(BaseTest):

    def test_alert_button(self):
        self.resizablePage = ResizablePage(self.driver)
        self.resizablePage.do_resizable(self.driver)

