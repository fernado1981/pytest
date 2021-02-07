from web.hook.after_before import after_before
from web.page_object.areaPrivadaPage import areaPrivadaPage
from web.page_object.fillformempresaPage import fillformempresaPage
from web.page_object.homePage import homePage

up = after_before()
down = after_before()
lanza = homePage()
area_privada = areaPrivadaPage()
fillform = fillformempresaPage()


def test_tear_up():
    up.test_go_url()


def test_homePage():
    lanza.test_accept_cookie()
    lanza.test_title()
    lanza.test_nav()


def test_private_area():
    area_privada.test_title()
    # area_privada.tap_my_vodafone_particular()
    area_privada.test_tap_my_vodafone_empresas()


def test_fill_form_enviroments():
    fillform.test_fill_user()
    fillform.test_fill_pass()
    fillform.test_acept()


def test_tear_down():
    down.test_close()
