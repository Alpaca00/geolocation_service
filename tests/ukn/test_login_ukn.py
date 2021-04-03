import pytest
from selene.api import config
from src.domain.employee_ukn import Admin
from src.ukn_service_pages.login_page import LoginPage
from src.ukn_service_pages.main_page import MainPage

config.hold_browser_open = True


@pytest.mark.skip()
def test_can_admin_login():
    admin = Admin()
    email, password = admin.find_email_ukn, admin.find_password_ukn
    LoginPage().open().login_as(email, password)
    MainPage().at_main_page()


