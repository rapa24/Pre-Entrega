from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#login paso a paso

driver = webdriver.Chrome() 
try:
    driver.get("https://www.saucedemo.com/")

    #USUARIO
    usuario = driver.find_element(By.ID,"user-name")
    usuario.send_keys("standard_user")
    
    #PASS
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    #LOGIN
    password.send_keys(Keys.RETURN) 

    #URL
    if"/inventory.html" in driver.current_url:
        print("Si esta en la pagina correcta")

    else:
        print("No es la pagina correcta")    

finally:
    driver.quit()

