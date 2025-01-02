from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Config:
    BASE_URL = "https://www.youtube.com"
    DRIVER_PATH = "C:\\Code\\SDET\\YouTube-Testing-Framework\\WebDrivers\\chromedriver.exe"
    IMPLICIT_WAIT = 15
    EXPLICIT_WAIT = 20
    SEARCH_QUERY = "Never Gonna Give You Up"

    @staticmethod
    def get_webdriver():
        """
        Centralized WebDriver setup.
        Returns a configured WebDriver instance.
        """
        options = Options()
        # Add custom options here if needed
        # options.add_argument("--headless")  # Example: Headless mode

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        driver.implicitly_wait(Config.IMPLICIT_WAIT)
        driver.maximize_window()
        return driver
