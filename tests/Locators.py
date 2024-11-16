from selenium.webdriver.common.by import By

class Locators:
    # HomePage locators
    HOME_SEARCH_BOX = (By.NAME, "search_query")

    # ResultsPage locators
    RESULTS_VIDEO_TITLES = (By.XPATH, "//a[@id='video-title']")