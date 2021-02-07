from web.hook.after_before import after_before
from web.page_object.areaPrivadaPage import areaPrivadaPage
from web.page_object.fillformempresaPage import fillformempresaPage
from web.page_object.homePage import homePage

up = after_before()
down = after_before()
launch = homePage()
private_area = areaPrivadaPage()
fillform = fillformempresaPage()


def test_tear_up():
    up.test_go_url()


def test_homePage():
    launch.test_accept_cookie()
    launch.test_title()
    launch.test_nav()


def test_private_area():
    private_area.test_title()
    private_area.test_tap_my_vodafone_emvironment()


def test_fill_form_enviroments():
    fillform.test_fill_user()
    fillform.test_fill_pass()
    fillform.test_acept()


def test_tear_down():
    down.test_close()
