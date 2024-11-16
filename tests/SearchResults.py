import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from HomePage import HomePage

@pytest.fixture(scope="function")
def setup():
    """
    Fixture to set up and tear down the WebDriver instance.
    """
    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    base_url = "https://www.youtube.com"

    # Yield WebDriver and base URL to the test
    yield driver, base_url

    # Quit the WebDriver after the test
    driver.quit()

def test_search_functionality(setup):
    """
    Test to verify the YouTube search functionality.
    """
    driver, base_url = setup

    # Initialize HomePage with the driver and base URL
    homepage = HomePage(driver, base_url)

    # Navigate to the home page
    homepage.navigate_to()

    # Perform a search for "SDET tutorial"
    search_query = "SDET tutorial"
    homepage.search_video(search_query)

    # Assert that the page title contains the search query
    assert search_query in homepage.get_title(), f"Search did not yield the correct results for '{search_query}'"
