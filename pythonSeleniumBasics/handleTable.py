from selenium import webdriver
from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicsSelenium import BasicsSelenium


class HandleTable(BasicsSelenium):
    def verifyTables(self):
        self.driver.get("https://money.rediff.com/indices/nse")
        # vt = self.driver.find_element(By.XPATH,"//table[@id='dataTable']")
        # print(vt.text)
        # table_row = self.driver.find_element(By.XPATH, "//table[@id='dataTable']/tbody/tr[3]")
        # print("Third row text is ", table_row.text)  # Get the text of the row

        # table_col = self.driver.find_element(By.XPATH,"//table[@id='dataTable']//tbody/tr[3]/td[2]")
        # print("3rd row 2nd column is",table_col.text)
        #
        # table_row_last = self.driver.find_element(By.XPATH,"//table[@id='dataTable']/tbody/tr[last()]")
        # print(table_row_last.text)

        table_lastcolumn_thirdrow = self.driver.find_element(By.XPATH,"//table[@id='dataTable']/tbody/tr[3]/td[last()]")
        print(table_lastcolumn_thirdrow.text)

ht = HandleTable()
ht.initializeBrowser()
ht.verifyTables()
