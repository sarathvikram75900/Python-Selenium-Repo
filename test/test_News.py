from selenium.webdriver.common.by import By
import time

from pages.loginPage import LoginPage
from pages.newsPage import NewsPage
from utility.excelUtility import ExcelUtility

class TestNews:
    def test_news(self,browserinstance):
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

        # manage_news_tile = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        # manage_news_tile.click()
        news_page = NewsPage(self.driver)
        news_page.click_manage_news_tile()
        time.sleep(3)

        # new = self.driver.find_element(By.XPATH,"//a[@href='https://groceryapp.uniqassosiates.com/admin/news/add']")
        # new.click()
        news_page.set_new()
        time.sleep(3)

        # news_textarea = self.driver.find_element(By.XPATH, "//textarea[@id='news']")
        # news_textarea.send_keys("Learning pytest with python selenium...")
        news_page.set_news_textarea()
        time.sleep(3)

        # save = self.driver.find_element(By.XPATH,"//button[@name='create']")
        # save.click()
        news_page.set_save()

        alert = self.driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        assert "News Created Successfully" in alert.text

    def test_search_news(self,browserinstance):
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

        # manage_news_tile = self.driver.find_element(By.XPATH,
        #                                             "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        # manage_news_tile.click()

        news_page = NewsPage(self.driver)
        news_page.click_manage_news_tile()
        time.sleep(3)

        # search = self.driver.find_element(By.XPATH,"//a[@class='btn btn-rounded btn-primary']")
        # search.click()
        news_page.set_search()

        # news_title = self.driver.find_element(By.XPATH,"//input[@name='un']")
        # news_title.send_keys("Learning")
        news_page.set_news_title()

        # search_2 = self.driver.find_element(By.XPATH,"//button[@name='Search']")
        # search_2.click()
        news_page.set_search_2()

        nav = self.driver.current_url
        assert nav == "https://groceryapp.uniqassosiates.com/admin/news/index"