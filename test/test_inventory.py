from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


#login
@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

 #titulo del inventario   
def test_inventory_title(driver_logged):
    titulo = driver_logged.title
    assert titulo=="Swag Labs", "titulo incorrecto"
    
#producto que se muestra en el carrito
def test_productos_visibles(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos) >0

# botones importantes
def test_ui_elements(driver_logged):
    menu = driver_logged.find_element(By.ID,"react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME,"product_sort_container")

    assert menu.is_displayed(), "El menu no esta"
    assert filtro.is_displayed(), "el filtro no existe"

