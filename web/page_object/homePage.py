from web.hook.locator import locator
from web.hook.utility import utility


class homePage(utility):

    def __init__(self):
        super().__init__()
        self.data_home = locator.data_home
        self.data_private_area = locator.data_area_privada

    def test_accept_cookie(self):
        self.cookie()

    def test_title(self):
        title = self.get_title()
        assert title == self.data_home['title']

    def test_nav(self, option='soy_cliente'):
        self.nav_option(option)
        title = self.get_title()
        assert title == self.data_private_area['title_cliente']
