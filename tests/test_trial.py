from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def test_if_home_page():
    service = Service(executable_path="C:\\Code\\SDET\\WebDrivers\\chromedriver.exe")
    browser = webdriver.Chrome(service=service)

    try:
        browser.get("https://www.youtube.com/")
        browser.maximize_window()

        # Assert that we're on the YouTube homepage
        WebDriverWait(browser, 10).until(
            EC.title_contains("YouTube")
        )
        assert "YouTube" in browser.title, "Page title does not contain 'YouTube'"

        # Wait until the search bar is clickable
        search_bar = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.NAME, "search_query"))
        )

        # Click on the search bar to ensure it is focused
        search_bar.click()

        # Enter the search query and press Enter
        search_bar.send_keys("Never Gonna Give You Up")
        search_bar.send_keys(Keys.ENTER)

        # Wait for the search results to load
        WebDriverWait(browser, 15).until(
            EC.presence_of_all_elements_located((By.ID, "video-title"))
        )

        # Get all video titles displayed in the search results
        video_titles = browser.find_elements(By.ID, "video-title")

        # Loop through the video titles to find the correct one
        found_video = None
        for video in video_titles:
            if "Never Gonna Give You Up" in video.get_attribute("title"):
                found_video = video
                break

        # Assert that the video was found and click on it
        assert found_video is not None, "Expected video not found in search results."
        found_video.click()

        # Optional: Wait for the video page to load and verify the video title
        WebDriverWait(browser, 15).until(
            EC.title_contains("Never Gonna Give You Up")
        )
        assert "Never Gonna Give You Up" in browser.title, "Video page title is incorrect"
        time.sleep(60)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        browser.quit()
