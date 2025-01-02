from selenium.webdriver.common.keys import Keys
from BasePage import BasePage
from Locators import Locators
from Config import Config

class HomePage(BasePage):
    def search_video(self, video_name=Config.SEARCH_QUERY):
        # main locator for search box
        self.enter_txt(Locators.HOME_SEARCH_BOX, video_name)
        
        # send enter key to search box
        search_box_element = self.find_element(Locators.HOME_SEARCH_BOX)
        if search_box_element:
            search_box_element.send_keys(Keys.ENTER)
        else:
            print("Search box element not found.")
