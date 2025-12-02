import pytest

from pages.loginPage import LoginPage
from utility.excelUtility import ExcelUtility


class Test_login:
    @pytest.mark.run(order=1)
    def test_loginWithValidCredentials(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin")



        # username = self.driver.find_element(By.XPATH,"//input[@name='username']")
        # username.send_keys(username_value)
        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.signin_click()

        # password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        # password.send_keys(password_value)


        # signIn = self.driver.find_element(By.XPATH,"//button[text()='Sign In']")
        # signIn.click()


        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin"
        print("successful")

    @pytest.mark.run(order=2)
    def test_loginWithInvalidUsernameValidPassword(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(4, 1)
        password_value = excel_utility.read_user_data(4, 2)
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

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"
        print("successful")


    @pytest.mark.run(order=3)
    def test_loginWithValidUsernameInvalidPassword(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(3, 1)
        password_value = excel_utility.read_user_data(3, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin")

        # username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        # username.send_keys("admin")
        #
        # password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        # password.send_keys("pass")
        #
        # signIn = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        # signIn.click()

        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.signin_click()

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"
        print("successful")

    @pytest.mark.run(order=4)
    def test_loginWithInvalidUsernameInvalidPassword(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(5, 1)
        password_value = excel_utility.read_user_data(5, 2)
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

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"
        print("successful")

