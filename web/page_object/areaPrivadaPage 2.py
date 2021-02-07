from web.hook.locator import locator
from web.hook.utility import utility


class areaPrivadaPage(utility):

    def __init__(self):
        super().__init__()
        self.data_area_privada = locator.data_area_privada
        self.data_my_vodafone = locator.data_my_vodafone_particular
        self.data_my_empresa = locator.data_my_vodafone_empresa

    def test_title(self):
        title = self.get_title()
        assert title == self.data_area_privada['title_cliente']

    def test_tap_my_vodafone_particular(self):
        self.btn_tap_area_privada()
        title = self.get_title()
        assert title == self.data_my_vodafone['title']

    def test_tap_my_vodafone_empresas(self):
        self.btn_tap_area_privada('my_vodafone_business')
        title = self.get_title()
        assert title == self.data_my_empresa['title']
