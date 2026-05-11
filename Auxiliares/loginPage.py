from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(driver):
    driver.get("https://www.saucedemo.com/")

    #USUARIO
    usuario = driver.find_element(By.ID,"user-name")
    usuario.send_keys("standard_user")
    
    #PASS
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    #LOGIN
    password.send_keys(Keys.RETURN) 