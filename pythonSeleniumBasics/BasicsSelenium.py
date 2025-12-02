from selenium import webdriver
class BasicsSelenium:
    def __init__(self):
        self.driver = None
    def initializeBrowser(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://selenium.qabible.in/")
    def closeBrowser(self):
        #self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    base = BasicsSelenium()
    base.initializeBrowser()
    base.closeBrowser()