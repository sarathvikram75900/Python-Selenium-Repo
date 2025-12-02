import time

import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pythonSeleniumBasics.BasicsSelenium import BasicsSelenium

class HandlingActions(BasicsSelenium):
    def verifyMouseHover(self):
        home_hover = self.driver.find_element(By.XPATH,"//a[text()='Home']")
        actions = ActionChains(self.driver)
        actions.move_to_element(home_hover).perform()
    def verifyRightClick(self):
        home_right_click = self.driver.find_element(By.XPATH, "//a[text()='Home']")
        actions = ActionChains(self.driver)
        actions.context_click(home_right_click).perform()

    def verifyDragAndDrop(self):
        self.driver.get("https://demoqa.com/droppable")
        drag = self.driver.find_element(By.XPATH,"//div[@id='draggable']")
        drop = self.driver.find_element(By.XPATH, "//div[@id='droppable']")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(drag,drop).perform()

    def verify_keyboard_action(self):
        # Simulate pressing Ctrl + T to open a new tab (using pyautogui)
        pyautogui.hotkey('ctrl', 't')
        time.sleep(2)  # Adding delay for visibility
        pyautogui.write('https://www.google.com')  # Typing URL
        pyautogui.press('enter')  # Pressing Enter



handle_actions = HandlingActions()
handle_actions.initializeBrowser()
# handle_actions.verifyMouseHover()
# handle_actions.verifyRightClick()
# handle_actions.verifyDragAndDrop()
handle_actions.verify_keyboard_action()