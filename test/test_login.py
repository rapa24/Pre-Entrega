from page.login_page import LoginPage
from utils.logger import logger


# login utilizando @pytest.fixture
def test_login_ok(driver):
    logger.info("Iniciando el driver para el  test_login_ok")
    login_page = LoginPage(driver)

    logger.info("ingresando los datos para las pruebas")
    login_page.login("standard_user","secret_sauce")

    logger.info("iniciando sesion...")

    assert "/inventory.html" in driver.current_url, "No se redirige al inventario"
    logger.info("Sesion iniciada correctamente")

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.login("standard_user","123456")

    error = login_page.get_error_message() 

    #assert error == "hola"

    assert "Epic sadface: Username and password do not match any user in this service" in error