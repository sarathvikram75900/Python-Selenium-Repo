from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def enter_admin(self):
        admin = self.driver.find_element(By.XPATH, "//img[@alt='User Image']")
        admin.click()

    def enter_logout(self):
        logout = self.driver.find_elements(By.XPATH, "//a[@class='dropdown-item']")
        logout[1].click()