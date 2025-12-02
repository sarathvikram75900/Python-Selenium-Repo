from selenium.webdriver.common.by import By
import time

from pages.adminPage import AdminPage
from pages.loginPage import LoginPage
from utility.excelUtility import ExcelUtility


class TestAdmin:
    def test_return_to_home(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin")

        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        #
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        #
        # signIn = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # signIn.click()

        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.signin_click()

        time.sleep(3)

        # admin_users_tile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        # admin_users_tile.click()
        # time.sleep(3)
        # home_return = self.driver.find_element(By.XPATH,"//a[text()='Home']")
        # home_return.click()
        admin_page = AdminPage(self.driver)
        admin_page.click_admin_user_title()
        time.sleep(3)
        admin_page.click_home_return()

        final_nav = self.driver.current_url
        assert final_nav == "https://groceryapp.uniqassosiates.com/admin/home"

    def test_new_user(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin")

        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        #
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        #
        # signIn = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # signIn.click()
        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.signin_click()

        time.sleep(3)

        # admin_users_tile = self.driver.find_element(By.XPATH,
        #                                             "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        # admin_users_tile.click()
        admin_page = AdminPage(self.driver)
        admin_page.click_admin_user_title()
        time.sleep(3)

        # new = self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-danger']")
        # new.click()

        # user_name = self.driver.find_element(By.XPATH,"//input[@id='username']")
        # user_name.send_keys("kamala")

        # pass_word = self.driver.find_element(By.XPATH,"//input[@id='password']")
        # pass_word.send_keys("kamala")

        # dd = self.driver.find_element(By.XPATH,"//select[@id='user_type']")
        # select = Select(dd)
        # select.select_by_value('admin')

        # save = self.driver.find_element(By.XPATH,"//button[@name='Create']")
        # save.click()
        admin_page.click_new()
        admin_page.set_username()
        admin_page.set_password()
        admin_page.set_dropdown()
        admin_page.set_save()
        alert = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        assert "User Created Successfully" in alert.text

    def test_admin_reset(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin")

        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        #
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        #
        # signIn = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # signIn.click()
        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.signin_click()

        time.sleep(3)

        # admin_users_tile = self.driver.find_element(By.XPATH,
        #                                             "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        # admin_users_tile.click()
        admin_page = AdminPage(self.driver)
        admin_page.click_admin_user_title()
        time.sleep(3)

        # reset = self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-warning']")
        # reset.click()
        admin_page.set_reset()
        nav = self.driver.current_url
        assert nav == 'https://groceryapp.uniqassosiates.com/admin/list-admin'

    def test_admin_search(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin")

        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys(username_value)
        #
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys(password_value)
        #
        # signIn = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # signIn.click()
        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.signin_click()

        time.sleep(3)

        # admin_users_tile = self.driver.find_element(By.XPATH,
        #                                             "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-admin' and @class='small-box-footer']")
        # admin_users_tile.click()

        admin_page = AdminPage(self.driver)
        admin_page.click_admin_user_title()
        time.sleep(3)

        # search = self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        # search.click()
        admin_page.click_search()

        time.sleep(3)

        # user_name = self.driver.find_element(By.XPATH,"//input[@id='un']")
        # user_name.send_keys("sarath")
        admin_page.find_username()

        # dd_usertype = self.driver.find_element(By.XPATH,"//select[@id='ut']")
        # select = Select(dd_usertype)
        # select.select_by_value("admin")
        admin_page.set_find_dropdown()
        time.sleep(3)

        # search = self.driver.find_element(By.XPATH,"//button[@name='Search']")
        # search.click()
        admin_page.set_find_search()

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/user/index?un=sarath&ut=admin&Search=sr"

