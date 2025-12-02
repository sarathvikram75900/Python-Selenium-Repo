import time

from pythonSeleniumBasics.BasicsSelenium import BasicsSelenium
from selenium import webdriver
from selenium.webdriver.common.by import By

class HandlingAlerts(BasicsSelenium):
    def verify_simple_alerts(self):
        self.driver.get("https://demoqa.com/alerts")
        simple_alert_button = self.driver.find_element(By.XPATH,"//button[@id='alertButton']")
        simple_alert_button.click()
        # Switch to alert and accept it
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        time.sleep(5)
        alert.accept()

        # time.sleep(10)

    def verify_confirm_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.XPATH, "//button[@id='confirmButton']").click()
        alert = self.driver.switch_to.alert
        # alert.accept()
        alert.dismiss()
        time.sleep(10)

    def verify_prompt_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        self.driver.find_element(By.XPATH,"//button[@id='promtButton']").click()
        alert = self.driver.switch_to.alert
        alert.send_keys("sarath vikram")
        alert.accept()
        time.sleep(10)


handling_alerts = HandlingAlerts()
handling_alerts.initializeBrowser()
# handling_alerts.verify_simple_alerts()
# handling_alerts.verify_confirm_alert()
handling_alerts.verify_prompt_alert()