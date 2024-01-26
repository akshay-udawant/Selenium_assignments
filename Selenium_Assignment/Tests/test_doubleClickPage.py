from Pages.DoubleClickPage import DoubleClickPage
from Tests.test_base import BaseTest


class Test_DoubleClick(BaseTest):

    def test_double_click(self):
        self.doubleClickPage = DoubleClickPage(self.driver)
        self.doubleClickPage.do_double_click(self.driver)
