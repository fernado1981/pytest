from web.hook.locator import locator
from web.hook.utility import utility


class areaPrivadaPage(utility):

    def __init__(self):
        super().__init__()
        self.data_private_area = locator.data_area_privada
        self.data_my_vodafone = locator.data_my_vodafone_particular
        self.data_my_environment = locator.data_my_vodafone_empresa

    def test_title(self):
        title = self.get_title()
        assert title == self.data_private_area['title_cliente']

    def test_tap_my_vodafone_user(self):
        self.btn_tap_area_privada()
        title = self.get_title()
        assert title == self.data_my_vodafone['title']

    def test_tap_my_vodafone_emvironment(self):
        self.btn_tap_area_privada('my_vodafone_business')
        title = self.get_title()
        assert title == self.data_my_environment['title']
