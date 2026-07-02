
from selenium.webdriver.common.by import By
from page.inventory_page import InventoryPage
# Importamos el logger ya configurado
from utils.logger import logger 

def test_inventory_title(driver_logged):
    logger.info("--- Iniciando test_inventory_title ---")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Obteniendo el título de la página de inventario...")
    titulo = inventory_page.obtener_titulo()
    
    logger.info(f"Título obtenido: '{titulo}'. Validando assert...")
    assert titulo == "Swag Labs", "El titulo de la pagina no es correcto"
    logger.info("test_inventory_title completado con éxito.")

def test_productos_visibles(driver_logged):
    logger.info("--- Iniciando test_productos_visibles ---")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Buscando productos visibles en la pantalla...")
    productos = inventory_page.obtener_productos()
    
    logger.info(f"Cantidad de productos encontrados: {len(productos)}. Validando presencia...")
    assert len(productos) > 0, "No se encontraron productos en la página"
    logger.info("test_productos_visibles completado con éxito.")

def test_ui_elements(driver_logged):
    logger.info("--- Iniciando test_ui_elements ---")
    inventory_page = InventoryPage(driver_logged)

    logger.info("Validando visibilidad del menú lateral...")
    menu_ok = inventory_page.menu_visible()
    assert menu_ok, "El menu no está presente en la pagina"
    logger.info("Menú lateral verificado correctamente.")

    logger.info("Validando visibilidad del filtro de productos...")
    filtro_ok = inventory_page.filtro_visible()
    assert filtro_ok, "El filtro no está presente en la pagina"
    logger.info("Filtro de productos verificado correctamente.")
    
    logger.info("test_ui_elements completado con éxito.")