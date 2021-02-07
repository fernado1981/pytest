from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from web.driver.chrome import chrome_drive
from web.hook.locator import locator


class utility(chrome_drive):
    __timeout = 10

    def __init__(self):
        self.web_driver = chrome_drive.data['drive']
        self._web_driver_wait = WebDriverWait(self.web_driver, utility.__timeout)
        self.data = locator.data_home
        self.data_area_privada = locator.data_area_privada
        self.data_my_vodafone_empresa = locator.data_my_vodafone_empresa

    def openUrl(self):
        self.web_driver.get(self.data['url'])

    def get_title(self):
        return self.web_driver.title

    def cookie(self):
        self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data['cookie'])))
        self.web_driver.find_element_by_xpath(self.data['cookie']).click()

    def nav_option(self, option='soy_cliente'):
        if option is 'soy_cliente':
            self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data['nav_cliente'])))
            self.web_driver.find_element_by_xpath(self.data['nav_cliente']).click()
        elif option is 'movil_fibra':
            self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data['nav_movil_fibra'])))
            self.web_driver.find_element_by_xpath(self.data['nav_movil_fibra']).click()
        elif option is 'tarifa_movil':
            self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data['nav_tarifa_movil'])))
            self.web_driver.find_element_by_xpath(self.data['nav_tarifa_movil']).click()
        elif option is 'sólo_fibra':
            self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data['nav_sólo_fibra'])))
            self.web_driver.find_element_by_xpath(self.data['nav_sólo_fibra']).click()
        elif option is 'televisiónl':
            self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data['nav_televisión'])))
            self.web_driver.find_element_by_xpath(self.data['nav_televisión']).click()
        else:
            self._web_driver_wait.until(
                EC.visibility_of_element_located((By.XPATH, self.data['nav_Móviles_dispositivos'])))
            self.web_driver.find_element_by_xpath(self.data['nav_Móviles_dispositivos']).click()

    def btn_tap_area_privada(self, option='my_vodafone'):
        self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data_area_privada[option])))
        self.web_driver.find_element_by_xpath(self.data_area_privada[option]).click()

    def insert_name(self, name='pepe', xpath_name=''):
        self._web_driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath_name)))
        self.web_driver.find_element_by_xpath(xpath_name).send_keys(name)

    def insert_pass(self, password='pepe@pepe.com', xpath_pass=''):
        self._web_driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, xpath_pass)))
        self.web_driver.find_element_by_xpath(xpath_pass).send_keys(password)

    def submit(self):
        self._web_driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, self.data_my_vodafone_empresa['accept'])))
        self.web_driver.find_element_by_xpath(self.data_my_vodafone_empresa['accept']).click()

    def search_error_txt(self):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, self.data_my_vodafone_empresa['errortxt']))).is_displayed()

    def quit_driver(self):
        self.web_driver.quit()
