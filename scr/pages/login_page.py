from selene.support.shared.jquery_style import s
from selene.support.shared import browser
from scr.pages.main_page import MainPage


class LoginPage(object):
    def __init__(self):
        self.username_input = s('#tbLogin')
        self.password_input = s('#tbPassword')
        self.login_btn = s('#lbEnter')

    def open(self):
        browser.open('https://gps2.totalcontrol.ua/login.aspx?logout=true')
        return self

    def login_as(self, username, password):
        self.username_input.set_value(username)
        self.password_input.set_value(password)
        self.login_btn.click()
        return MainPage()


