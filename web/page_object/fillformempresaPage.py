from web.hook.locator import locator
from web.hook.utility import utility


class fillformempresaPage(utility):

    def __init__(self):
        super().__init__()
        self.data_my_environment = locator.data_my_vodafone_empresa

    def test_fill_user(self):
        self.insert_name('fer', self.data_my_environment['input_name'])

    def test_fill_pass(self):
        self.insert_pass('fernandito81', self.data_my_environment['input_password'])

    def test_acept(self):
        self.submit()
        error = self.search_error_txt()
        assert error is True
