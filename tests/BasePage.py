from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Config import Config

class BasePage:
    #constructor
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Config.BASE_URL

    def find_element(self, locator, timeout_sec=Config.EXPLICIT_WAIT):
        try:
            return WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_element_located(locator), f"Can't find the element by locator {locator}")
        except Exception as e:
            print(f"Error finding the element: {e}")
            return None

    def find_elements(self, locator, timeout_sec=Config.EXPLICIT_WAIT):
        try:
            return WebDriverWait(self.driver, timeout_sec).until(EC.presence_of_all_elements_located(locator), f"Can't find elements by locator {locator}")
        except Exception as e:
            print(f"Error finding elements: {e}")
            return None

    def click_on(self, locator, timeout_sec=Config.EXPLICIT_WAIT):
        try: 
            self.find_element(locator, timeout_sec).click()
        except Exception as e:
            print(f"Error clicking on element: {e}")
            return None

    def navigate_to(self, url = ''):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def enter_txt(self, locator, txt):
        try:
            self.find_element(locator).send_keys(txt)
        except Exception as e:
            print(f"Error entering text: {e}")
            return None

    def get_url(self):
        return self.driver.current_url

