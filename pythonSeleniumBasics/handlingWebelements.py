from pythonSeleniumBasics.BasicsSelenium import BasicsSelenium
from selenium.webdriver.common.by import By


class HandlingWebelements(BasicsSelenium):
    def verifyWebElementsCommands(self):
        self.driver.get("https://selenium.qabible.in/simple-form-demo.php")
        messagebox = self.driver.find_element(By.XPATH,"//input[@id='single-input-field']")
        messagebox.send_keys("learning selenium")
        sub_button = self.driver.find_element(By.ID,"button-one")
        sub_button.click()
        show_msg = self.driver.find_element(By.XPATH,"//div[@id='message-one']")
        print(show_msg.text)
        print(show_msg.is_displayed())
        print(show_msg.is_enabled())
        messagebox.clear()


v = HandlingWebelements()
v.initializeBrowser()
v.verifyWebElementsCommands()




