import pytest
from selene import have
from selene.core.query import text

from src.domain.user import User, Admin
from src.pages.login_page import LoginPage


@pytest.mark.skip()
def test_can_admin_login():
    admin = User()
    logo = Admin()
    (LoginPage().open().login_as(admin.get_admin_username(),
     admin.get_admin_password()).main_page_logo_text().should(have.text(logo.main_logo())))


@pytest.mark.skip()
def test_account_balance_is_displayed():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).inspect_current_balance()


def test_pick_mileage_report():
    admin = User()
    logo = Admin()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    (LoginPage().open().login_as(username, password).go_to_car_mileage_data()
     .logo_text().should(have.text(logo.mileage_logo())))
