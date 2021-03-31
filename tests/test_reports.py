import allure
import pytest
from selene import have
from selene.support.shared import browser
from selene.api import config
from app.handling_geo_database import VehicleStopsCollection, trash_remove, collection_vehicle_stops
from src.domain.user import User, Admin
from src.geolocation_service_pages.login_page import LoginPage
from src.geolocation_service_pages.main_page import MainPage
from src.geolocation_service_pages.vehicle_mileage_report_page import VehicleMileageReportPage
from src.geolocation_service_pages.vehicle_stops_report_page import VehicleStopsReportPage


# config.hold_browser_open = True


@pytest.fixture
def login_as_admin():
    admin = User()
    username, password = admin.get_admin_username(), admin.get_admin_password()
    LoginPage().open().login_as(username, password)
    yield
    browser.quit()


@pytest.mark.skip()
@allure.title('inspect logo at mileage page')
def test_logo_mileage_report_is_present(login_as_admin):
    logo = Admin()
    MainPage().go_to_vehicle_mileage_page()
    VehicleMileageReportPage().logo_text().should(have.exact_text(logo.mileage_logo))


@pytest.mark.skip()
def test_pick_mileage_report(login_as_admin):
    MainPage().go_to_vehicle_mileage_page()
    VehicleMileageReportPage().switch_on_report_tab().should(have.text('Отчет по пробегу'))


@pytest.mark.skip()
@allure.story('data collection')
@allure.title('insert document to mileage_collection')
def test_insert_document_to_mileage_collection(login_as_admin):
    MainPage().go_to_vehicle_mileage_page()
    VehicleMileageReportPage().insert_data_to_vehicle_mileage_collection()


@pytest.mark.skip()
@allure.story('data collection')
@allure.title('save mileage report to csv file')
def test_save_mileage_report_to_csv(login_as_admin):
    MainPage().go_to_vehicle_mileage_page()
    VehicleMileageReportPage().save_report_to_file()


@pytest.mark.skip()
@allure.title('table title is ... at frame')
def test_pick_stops_report(login_as_admin):
    with allure.step('check table title'):
        try:
            VehicleStopsReportPage().go_to_vehicle_stops_report_page().switch_on_vehicle_stops_report_tab().should(
                have.exact_text('Отчет по стоянкам'))
        except:
            allure.attach(body=browser.config.driver.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=allure.attachment_type.PNG, extension=(500, 600))
            raise


@pytest.mark.skip()
@allure.story('data collection')
@allure.title('insert document to vehicle stops collection')
def test_insert_document_to_vehicle_stops_collection(login_as_admin):
    VehicleStopsReportPage().go_to_vehicle_stops_report_page().switch_on_vehicle_stops_report_tab()
    trash_remove(collection_vehicle_stops)
    with allure.step('insert document to vehicle_stops_collection and check size collection'):
        assert VehicleStopsReportPage().insert_data_to_vehicle_stops_collection() == VehicleStopsCollection().size_collection()


@pytest.mark.skip()
@allure.story('data collection')
@allure.title('save vehicle stops report to csv file')
def test_save_vehicle_stops_report_to_csv(login_as_admin):
    VehicleStopsReportPage().go_to_vehicle_stops_report_page().save_report_to_file()
