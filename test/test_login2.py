from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# login utilizando @pytest.fixture

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        # Validación de URL
        assert "/inventory.html" in driver.current_url, "No es la correcta para el inventario"

    except Exception as e:
        print(f"Error en test_login: {e}")



