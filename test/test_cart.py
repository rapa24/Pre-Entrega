
from selenium.webdriver.common.by import By
from utils.logger import logger 

# CORREGIDO: Cambiamos 'login_in_driver' por 'driver_logged'
def test_cart(driver_logged):
    logger.info("--- Iniciando test_cart ---")
    driver = driver_logged  # Asignamos el fixture correcto a la variable driver

    # Agregar producto
    logger.info("Buscando los botones de los productos...")
    botones_productos = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    
    logger.info("Haciendo clic en el primer producto disponible para agregarlo al carrito...")
    botones_productos[0].click()

    # Contador del carro
    logger.info("Verificando el contador del carrito de compras...")
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge") 
    logger.info(f"Valor actual del contador en la interfaz: '{contador_cart.text}'")
    assert contador_cart.text == "1", f"El contador del carrito debería ser '1' pero es '{contador_cart.text}'"
 
    # Nombre de producto
    logger.info("Obteniendo el nombre del producto agregado desde la lista...")
    product_name = driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].text
    logger.info(f"Producto seleccionado: '{product_name}'")

    # Ir al carro
    logger.info("Haciendo clic en el icono del carrito para ir al detalle...")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener nombre producto en el carrito
    logger.info("Verificando el nombre del producto dentro del carrito...")
    cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    logger.info(f"Producto encontrado en el carrito: '{cart_item}'")

    # Validación final
    logger.info("Validando que el producto seleccionado coincida con el que está en el carrito...")
    assert product_name == cart_item, f"El producto en el carrito ({cart_item}) no coincide con el seleccionado ({product_name})"
    
    logger.info("--- test_cart finalizado con éxito ---")