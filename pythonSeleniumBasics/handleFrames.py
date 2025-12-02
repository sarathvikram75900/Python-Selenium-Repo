from pythonSeleniumBasics.BasicsSelenium import BasicsSelenium
from selenium.webdriver.common.by import By
class HandleFrames(BasicsSelenium):
    def verifyFrames(self):
        self.driver.get("https://demoqa.com/frames")
        # Find all iframe elements
        total_frames = self.driver.find_elements(By.TAG_NAME, "iframe")
        # Print the number of frames
        print(len(total_frames))

        frame1 = self.driver.find_element(By.XPATH,"//iframe[@id='frame1']")
        self.driver.switch_to.frame(frame1) # to focus on iframe

        frame_text = self.driver.find_element(By.XPATH,"//h1[@id='sampleHeading']")
        print(frame_text.text)
        self.driver.switch_to.default_content() # to free up the focus


handle_frames = HandleFrames()
handle_frames.initializeBrowser()
handle_frames.verifyFrames()