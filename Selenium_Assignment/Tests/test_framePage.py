from Pages.FramePage import FramePage
from Tests.test_base import BaseTest


class Test_Frame(BaseTest):

    def test_frame(self):
        self.framePage = FramePage(self.driver)
        self.framePage.frame_data(self.driver)