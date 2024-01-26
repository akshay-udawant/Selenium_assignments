import pytest

from Config.config import TestData
from Pages.AlertPage import AlertPage
from Pages.DragDropPage import DragDropPage
from Pages.TextFieldPage import TextFieldPage
from Tests.test_base import BaseTest


class Test_DragDrop(BaseTest):

    def test_drag_drop(self):
        self.dragDropPage = DragDropPage(self.driver)
        self.dragDropPage.do_drag_drop(self.driver)


