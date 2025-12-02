from pythonSeleniumBasics.BasicsSelenium import BasicsSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HandleDropDowns(BasicsSelenium):
    def verifyDropdowns(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        dd1 = self.driver.find_element(By.ID,"dropdowm-menu-1")
        select = Select(dd1)
        # select.select_by_index(1)
        # select.select_by_value("python")
        select.select_by_visible_text("SQL")
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()

    def verifyCheckbox(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        cb = self.driver.find_element(By.XPATH,"//input[@value='option-1']")
        print(cb.is_selected())
        cb.click()
        print(cb.is_selected())
    def verifyRadiobuttons(self):
        self.driver.get("https://www.webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html")
        rb = self.driver.find_element(By.XPATH,"//input[@value='green']")
        rb.click()


handle_dropdowns = HandleDropDowns()
handle_dropdowns.initializeBrowser()
handle_dropdowns.verifyDropdowns()
handle_dropdowns.verifyCheckbox()
handle_dropdowns.verifyRadiobuttons()

