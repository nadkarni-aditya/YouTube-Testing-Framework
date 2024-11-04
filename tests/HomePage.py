from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from BasePage import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.NAME, "search_query")  # Adjusted to YouTube's actual search bar identifier

    def search_video(self, video_name):
        self.enter_txt(self.SEARCH_BOX, video_name)
        self.find_element(self.SEARCH_BOX).send_keys(Keys.ENTER)
