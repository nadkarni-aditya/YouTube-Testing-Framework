from BasePage import BasePage
from Locators import Locators

class ResultsPage(BasePage):
    def get_video_titles(self):
        """Retrieve all video titles from the results page."""
        video_elements = self.find_elements(Locators.RESULTS_VIDEO_TITLES)
        if video_elements:
            return [element.text for element in video_elements if element.text.strip()]
        else:
            print("No video titles found.")
            return []

    def click_video_by_title(self, title):
        """Click on the first video matching the given title."""
        video_elements = self.find_elements(Locators.RESULTS_VIDEO_TITLES)
        if video_elements:
            for element in video_elements:
                if title.lower() in element.text.lower():
                    element.click()
                    print(f"Clicked on video with title: {title}")
                    return
        print(f"Video with title '{title}' not found.")
