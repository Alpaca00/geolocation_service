from selene import have
from selene.support.shared import browser
from scr.domain.user import User, Admin
from scr.pages.login_page import LoginPage

browser.config.browser_name = 'chrome'


def test_can_admin_login():
    admin = User()
    logo = Admin()
    (LoginPage().open().login_as(admin.get_admin_username(),
     admin.get_admin_password()).logo.should(have.text(logo.get_logo())))
