from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username_value):
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys(username_value)
    def enter_password(self,password_value):
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(password_value)
    def signin_click(self):
        signIn = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        signIn.click()
