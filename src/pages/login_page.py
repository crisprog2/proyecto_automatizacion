from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        # Aquí irían los selectores y acciones reales
        pass
