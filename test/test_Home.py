from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utility.excelUtility import ExcelUtility
import time

class TestHome:
    def test_loginWithValidCredentials(self,browserinstance):
        self.driver = browserinstance
        excel_utility = ExcelUtility()
        username_value = excel_utility.read_user_data(2, 1)
        password_value = excel_utility.read_user_data(2, 2)
        self.driver.get("https://groceryapp.uniqassosiates.com/admin")

        # username = self.driver.find_element(By.XPATH,"//input[@name='username']")
        # username.send_keys(username_value)
        #
        # password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        # password.send_keys(password_value)
        #
        # signIn = self.driver.find_element(By.XPATH,"//button[text()='Sign In']")
        # signIn.click()

        login_page = LoginPage(self.driver)
        login_page.enter_username(username_value)
        login_page.enter_password(password_value)
        login_page.signin_click()

        time.sleep(5)

        # admin = self.driver.find_element(By.XPATH,"//img[@alt='User Image']")
        # admin.click()
        # time.sleep(3)
        # logout = self.driver.find_elements(By.XPATH,"//a[@class='dropdown-item']")
        # print(len(logout))
        # logout[1].click()

        homepage = HomePage(self.driver)
        homepage.enter_admin()
        time.sleep(3)
        homepage.enter_logout()

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/login"


