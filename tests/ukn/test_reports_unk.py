import pytest
from app.handling_first_service_database import FirstServiceDatabase
from src.ukn_service_pages.main_page import MainPage


@pytest.mark.skip()
def test_set_parameters_rides_report(login_as_admin_unk):
    MainPage().go_to_rides_page().set_parameters_of_rides_report()


@pytest.mark.skip()
def test_save_rides_report_to_excel_file(login_as_admin_unk):
    (MainPage().go_to_rides_page().set_parameters_of_rides_report()
     .save_rides_report_to_csv_file())
    FirstServiceDatabase().insert_document_rides_to_collection()


@pytest.mark.skip()
def test_save_payments_report_to_excel_file(login_as_admin_unk):
    (MainPage().go_to_payments_page().set_parameters_of_payments_report()
     .save_payments_report_to_excel_file())
    FirstServiceDatabase().insert_document_payments_to_collection()


@pytest.mark.skip()
def test_database_collection():
    FirstServiceDatabase.checking_collections()


