from selene.api import *
from base_page import BasePage
from src.bt_service_pages.main_page_and_menu_pages import MainPage


class LoginPageLocators:
    EMAIL = "//input[@id='username']"
    PASSWORD = "//input[@id='password']"
    SUBMIT_BTN = "//button[@type='submit']"


class LoginPage(LoginPageLocators):
    def __init__(self):
        super(LoginPage).__init__()
        self.base_page = BasePage()

    def open(self):
        browser.open(self.base_page.bt_url)
        return self

    def at_login_page(self):
        locator = ss(by.xpath(self.EMAIL))
        return len(locator) > 0

    def login_as(self, email, password):
        if self.at_login_page():
            s(by.xpath(self.EMAIL)).set_value(email)
            s(by.xpath(self.PASSWORD)).set_value(password)
            s(by.xpath(self.SUBMIT_BTN)).click()
            return MainPage()
