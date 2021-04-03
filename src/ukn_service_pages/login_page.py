from selene.api import *
from selene.support.shared import browser
from base_page import BasePage
from src.geolocation_service_pages.main_page import MainPage


class LoginPageLocator:
    EMAIL = "//input[contains(@placeholder, 'Phone')]"
    PASSWORD = "//input[contains(@placeholder, 'Your password')]"
    SUBMIT_BTN = "//input[contains(@name, 'Login')]"


class LoginPage(LoginPageLocator):

    def __init__(self):
        super(LoginPage).__init__()
        self.base_page = BasePage()

    def open(self):
        browser.open(f'{self.base_page.unk_url}')
        return self

    def login_as(self, email, password):
        if self.at_login_page():
            s(by.xpath(self.EMAIL)).set_value(email)
            s(by.xpath(self.PASSWORD)).set_value(password)
            s(by.xpath(self.SUBMIT_BTN)).click()
            return MainPage()

    def at_login_page(self):
        locator = ss(by.xpath(self.EMAIL))
        return len(locator) > 0
