class BasePage:
    """
    Clase base para todas las páginas del proyecto.
    Proporciona métodos comunes para interactuar con el navegador.
    """

    def __init__(self, driver):
        """
        Inicializa la página con una instancia del driver de Selenium.
        :param driver: Instancia del navegador (WebDriver)
        """
        self.driver = driver

    def open(self, url):
        """
        Abre la URL especificada en el navegador.
        :param url: Dirección web a la que navegar
        """
        self.driver.get(url)
