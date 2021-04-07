import pytest
from app.handling_second_service_database import SecondServiceDatabase
from src.bt_service_pages.main_page_and_menu_pages import MainPage, RidesPage, BillsPage, CompensationPage, PaymentsPage, AcquiringPage
from src.domain.employee_bt import Employee




class TestGetReportsBT(object):
    EMPLOYEE = Employee()

    @pytest.mark.skip()
    def test_main_page_title(self, login_as_employee):
        assert MainPage().at_page(self.EMPLOYEE.find_main_page_title)

    # @pytest.mark.skip()
    def test_save_rides_report_to_csv_file(self, login_as_employee):
        MainPage().go_to_rides_page().at_page(self.EMPLOYEE.find_rides_page_title)
        RidesPage().save_rides_report_to_csv_file()
        #SecondServiceDatabase().insert_document_to_rides_collection()
        #MainPage().log_out_of_account()

    @pytest.mark.skip()
    def test_save_bills_report_to_pdf_file(self, login_as_employee):
        MainPage().go_to_bills_page().at_page(self.EMPLOYEE.find_bills_page_title)
        BillsPage().save_bills_report_to_pdf_file()
        MainPage().log_out_of_account()

    @pytest.mark.skip()
    def test_compensation_is_not_present(self, login_as_employee):
        MainPage().go_to_compensation_page().at_page(self.EMPLOYEE.find_compensation_page_title)
        CompensationPage().check_compensation(self.EMPLOYEE.find_condition_text_for_compensation_page)
        MainPage().log_out_of_account()

    @pytest.mark.skip()
    def test_save_payments_report_to_pdf_file(self, login_as_employee):
        MainPage().go_to_payments_page().at_page(self.EMPLOYEE.find_payments_page_title)
        PaymentsPage().save_payments_report_to_pdf_file()
        SecondServiceDatabase().insert_document_to_payments_collection()
        MainPage().log_out_of_account()

    @pytest.mark.skip()
    def test_save_acquiring_statistics_to_csv_file(self, login_as_employee):
        MainPage().go_to_payments_page().at_page(self.EMPLOYEE.find_acquiring_page_title)
        AcquiringPage().get_acquiring_statistics()
        SecondServiceDatabase().check_transfer_funds()
        SecondServiceDatabase().check_total_amount()
        MainPage().log_out_of_account()
