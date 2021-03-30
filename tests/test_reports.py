import allure
import pytest
from selene import have
from selene.support.shared import browser

from app.handling_data import StopsCollection
from src.domain.user import User, Admin
from src.pages.login_page import LoginPage
from src.pages.mileage_report_page import MileageReportPage
from src.pages.stops_report_page import StopsReportPage

# config.hold_browser_open = True


@pytest.mark.skip()
def test_logo_mileage_report_is_present():
    admin = User()
    logo = Admin()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    with allure.title('inspect logo at mileage page'):
        MileageReportPage().logo_text().should(have.exact_text(logo.mileage_logo))


@allure.step
@pytest.mark.skip()
def test_pick_mileage_report():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    MileageReportPage().switch_on_report_tab().should(have.text('Отчет по пробегу'))
    browser.quit()


@pytest.mark.skip()
def test_insert_data_to_mileage_collection():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    with allure.title('insert document to mileage_collection'):
        MileageReportPage().insert_data_to_mileage_collection()


@pytest.mark.skip()
def test_save_mileage_report_to_csv():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password).go_to_car_mileage_data()
    with allure.title('save mileage report to csv file'):
        MileageReportPage().save_report_to_file()


@allure.step
@pytest.mark.skip()
def test_pick_stops_report():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password)
    StopsReportPage().go_to_stops_report_page().switch_on_report_tab().should(have.text('Отчет по стоянкам'))


@pytest.mark.skip()
def test_insert_data_to_stops_collection():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password)
    with allure.title('insert document to stops_collection'):
        StopsReportPage().go_to_stops_report_page().switch_on_stops_car_report_tab()
        with allure.step('assert size collection'):
            assert StopsReportPage().insert_data_to_stops_collection() == StopsCollection().size_collection()


@pytest.mark.skip()
def test_save_stops_car_report_to_csv():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password)
    with allure.title('save stops car report'):
        StopsReportPage().go_to_stops_report_page().save_report_to_file()
