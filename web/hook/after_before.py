from web.hook.utility import utility


class after_before(utility):

    def test_go_url(self):
        self.openUrl()

    def test_close(self):
        self.quit_driver()
