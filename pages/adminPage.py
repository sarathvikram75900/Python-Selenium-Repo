from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AdminPage:
    def __init__(self,driver):
        self.driver = driver

    def click_admin_user_title(self):
        admin_users_tile = self.driver.find_element(By.XPATH,
                                                    "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        admin_users_tile.click()
    def click_home_return(self):
        home_return = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        home_return.click()

    def click_new(self):
        new = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-danger']")
        new.click()

    def set_username(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='username']")
        user_name.send_keys("Ramachandran")

    def set_password(self):
        pass_word = self.driver.find_element(By.XPATH, "//input[@id='password']")
        pass_word.send_keys("Ramachandran")
    def set_dropdown(self):
        dd = self.driver.find_element(By.XPATH, "//select[@id='user_type']")
        select = Select(dd)
        select.select_by_value('admin')
    def set_save(self):
        save = self.driver.find_element(By.XPATH, "//button[@name='Create']")
        save.click()
    def set_reset(self):
        reset = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-warning']")
        reset.click()
    def click_search(self):
        search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        search.click()
    def find_username(self):
        user_name = self.driver.find_element(By.XPATH, "//input[@id='un']")
        user_name.send_keys("sarath")

    def set_find_dropdown(self):
        dd_usertype = self.driver.find_element(By.XPATH, "//select[@id='ut']")
        select = Select(dd_usertype)
        select.select_by_value("admin")
    def set_find_search(self):
        search = self.driver.find_element(By.XPATH, "//button[@name='Search']")
        search.click()