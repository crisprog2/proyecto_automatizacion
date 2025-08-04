
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class LoginPage(BasePage):
    """
    Página de Login que hereda de BasePage.
    Aquí se definen los métodos y acciones específicas de la página de inicio de sesión.
    """

    def __init__(self, driver):
        """
        Inicializa la página de login con el driver del navegador.
        :param driver: Instancia del navegador (WebDriver)
        """

        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.flash_message = (By.ID, "flash")

        super().__init__(driver)

    def login(self, username, password):
        """
        Realiza la acción de login usando usuario y contraseña.
        Aquí se deben implementar los selectores y acciones reales.
        :param username: Nombre de usuario
        :param password: Contraseña
        """
        # Aquí irían los selectores y acciones reales
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password + Keys.RETURN)
        pass

    def get_flash_message(self):
        return self.driver.find_element(*self.flash_message).text