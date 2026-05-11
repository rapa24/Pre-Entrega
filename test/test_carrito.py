from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

def test_cart(login_in_driver):
    driver = login_in_driver

#agregar producto
    driver.find_elements(By.CLASS_NAME,"btn_inventory")[0].click()

#contador del carro
    contador_cart = driver.find_element(By.CLASS_NAME,"shopping_cart_badge") 
    assert contador_cart.text == "1"
 
 #nombre de producto
    product_name = driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text

#ir al carro
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

#obtener nombre producto
    cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text




    