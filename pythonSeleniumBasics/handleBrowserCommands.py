from pythonSeleniumBasics.BasicsSelenium import BasicsSelenium


class HandleBrowserCommand(BasicsSelenium):
    def verifyCommands(self):
        title = self.driver.title
        print(title)
        url = self.driver.current_url
        print(url)
        handle_id = self.driver.current_window_handle
        print(handle_id)
command = HandleBrowserCommand()
command.initializeBrowser()
command.verifyCommands()
