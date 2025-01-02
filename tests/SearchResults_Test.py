import re
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ResultsPage import ResultsPage
from Locators import Locators
from HomePage import HomePage
from Config import Config

@pytest.fixture(scope="function")
def setup():
    """
    Fixture to set up and tear down the WebDriver instance.
    """
    driver = Config.get_webdriver()
    yield driver
    driver.quit()

def test_search_functionality(setup):
    """
    Test to verify the YouTube search functionality.
    """
    driver = setup

    # Initialize HomePage with the driver
    homepage = HomePage(driver)

    # Navigate to the base URL (handled in BasePage via navigate_to)
    homepage.navigate_to()

    # Perform a search using the default query from Config
    search_box_value =homepage.search_video()
    WebDriverWait(driver, Config.EXPLICIT_WAIT).until(
        EC.presence_of_element_located(Locators.RESULTS_VIDEO_TITLES),
        "Search results did not load."
    )

    # Verify the search query is in the search box
    search_query = Config.SEARCH_QUERY
    assert search_query.lower() in search_box_value.lower(), (
        f"Search box does not contain the query '{search_query}'"
    )

    def normalize_text(text):
        return re.sub(r'\s+', ' ', text.strip().lower())

    # Verify the search query appears in at least one video title
    results_page = ResultsPage(driver)
    video_titles = results_page.get_video_titles()
    assert any(normalize_text(search_query) in title.lower() for title in video_titles), (
        f"No video titles contain the search query '{search_query}'"
    )

