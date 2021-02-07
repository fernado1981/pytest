class locator:
    data_home = {
        'url': 'https://www.vodafone.es/c/particulares/es/',
        'cookie': "//*[contains(text(),'Aceptar y seguir navegando')]",
        'title': 'Vodafone · #HazteIlimitable | Vodafone particulares',
        'nav_cliente': "//span[@class='mkl_span_client_text']",
        'nav_movil_fibra': "//nav[@id='nav-desktop']//ul//li//button[contains(text(),'Móvil + Fibra')]",
        'nav_tarifa_movil': "//nav[@id='nav-desktop']//ul//li//button[contains(text(),'Tarifa móvil')]",
        'nav_sólo_fibra': "//nav[@id='nav-desktop']//ul//li//button[contains(text(),'Sólo fibra')]",
        'nav_televisión': "//nav[@id='nav-desktop']//ul//li//button[contains(text(),'Televisión')]",
        'nav_Móviles_dispositivos': "//nav[@id='nav-desktop']//ul//li//button[contains(text(),'Móviles y dispositivos')]",
    }

    data_area_privada = {
        'title_cliente': "Acceso MiVodafone | Vodafone particulares",
        'my_vodafone': "//a[@data-analytics-context = 'particulares autonomos microempresa']",
        'my_vodafone_business': "//a[@data-analytics-context = 'pyme gran empresa']",
    }

    data_my_vodafone_particular = {
        'title': "Mi Vodafone"
    }

    data_my_vodafone_empresa = {
        'title': 'Acceso MiVodafone',
        'input_name': "//input[@name='userid']",
        'input_password': "//input[@name='password']",
        'accept': "//input[@id='enter']",
        'errortxt': "//div[@class='mvf-aviso mvf-aviso-show']//p[contains(text(),'Usuario o clave incorrecta')]",
        'txterror': "Usuario o clave incorrecta"

    }
