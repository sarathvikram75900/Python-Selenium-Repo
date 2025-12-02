from selenium.webdriver.common.by import By


class NewsPage:
    def __init__(self,driver):
        self.driver = driver

    def click_manage_news_tile(self):
        manage_news_tile = self.driver.find_element(By.XPATH,
                                                    "//a[@href='https://groceryapp.uniqassosiates.com/admin/list-news' and @class='small-box-footer']")
        manage_news_tile.click()
    def set_new(self):
        new = self.driver.find_element(By.XPATH, "//a[@href='https://groceryapp.uniqassosiates.com/admin/news/add']")
        new.click()
    def set_news_textarea(self):
        news_textarea = self.driver.find_element(By.XPATH, "//textarea[@id='news']")
        news_textarea.send_keys("Learning python selenium is easy...")
    def set_save(self):
        save = self.driver.find_element(By.XPATH, "//button[@name='create']")
        save.click()

    def set_search(self):
        search = self.driver.find_element(By.XPATH, "//a[@class='btn btn-rounded btn-primary']")
        search.click()
    def set_news_title(self):
        news_title = self.driver.find_element(By.XPATH, "//input[@name='un']")
        news_title.send_keys("Learning")
    def set_search_2(self):
        search_2 = self.driver.find_element(By.XPATH, "//button[@name='Search']")
        search_2.click()