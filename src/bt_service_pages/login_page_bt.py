from selene.api import *
from selenium import webdriver
from selene import Browser, Config
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
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
        # user_agent = UserAgent()
        # options.add_argument(f"user-agent={user_agent.random}")
        options = Options()
        prefs = {
            'download.default_directory': '/dev/shm/',
            'download.prompt_for_download': False,
            'download.directory_upgrade': True
         }
        options.add_experimental_option("prefs", prefs)
        browser.set_driver(webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities={
                'browserName': 'chrome',
                'platform': 'linux',
                }
            , options=options))
        config.timeout = 4
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
