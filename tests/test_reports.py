import pytest
from selene import have, be
from selene.support.shared import browser, config
from src.domain.user import User, Admin
from src.pages.login_page import LoginPage
from src.pages.mileage_report_page import MileageReportPage



config.hold_browser_open = True


@pytest.mark.skip()
def test_logo_mileage_report_is_present():
    admin = User()
    logo = Admin()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    MileageReportPage().logo_text().should(have.exact_text(logo.mileage_logo))


@pytest.mark.skip()
def test_pick_mileage_report():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    MileageReportPage().switch_on_report_window().should(have.text('Отчет по пробегу'))
    browser.quit()


@pytest.mark.skip()
def test_insert_data_to_collection():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    MileageReportPage().insert_data_to_collection()


def test_save_report_to_csv():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    MileageReportPage().save_report_to_file()
