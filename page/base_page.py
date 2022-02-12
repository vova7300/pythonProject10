from .locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_calculator_page(self,search):
        input = self.browser.find_element(*BasePageLocators.SEARCH)
        input.send_keys(search)
        button = self.browser.find_element(*BasePageLocators.BUTTON)
        button.click()