import time
import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage

@pytest.fixture
def driver():
    """
    Fixture que inicializa y cierra el navegador para cada prueba.
    """
    driver = webdriver.Chrome()  # O el driver que prefieras
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    """
    Prueba de ejemplo para un login exitoso usando el patrón POM.
    """
    login_page = LoginPage(driver)
    login_page.open('https://the-internet.herokuapp.com/login')
    login_page.login('tomsmith', 'SuperSecretPassword!')
    # Aquí irían las aserciones reales
    mensaje = login_page.get_flash_message()
    assert "You logged into a secure area!" in mensaje
    time.sleep(2)  # Espera para ver el resultado antes de cerrar el navegador