import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # O el driver que prefieras
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    login_page = LoginPage(driver)
    login_page.open('https://ejemplo.com/login')
    login_page.login('usuario', 'contraseña')
    # Aquí irían las aserciones reales
