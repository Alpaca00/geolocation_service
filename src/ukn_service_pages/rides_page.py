from selene.api import *
from utils.support import DownloadPending
from src.domain.employee_ukn import Employee


class RidesPageLocator:
    FROM = "//input[@id='mat-input-0']"
    TO = "//input[@id='mat-input-1']"
    SIGNAL = "//input[@id='mat-input-2']"
    LICENSE_PLATE = "//input[@id='mat-input-3']"
    FILTER_BTN = "//button[@class='green-btn mat-stroked-button mat-button-base']"
    TABLE_RIDES = "//div[@id='content']//mat-table//mat-row"
    EXCEL_REPORT = "//*[@id='Layer_1']/.."


class RidesPage(RidesPageLocator):
    def __init__(self):
        super(RidesPage).__init__()
        self.driver = config.driver
        self.employee = Employee('10388')

    def set_parameters_of_rides_report(self):
        s(by.xpath(self.FROM)).set_value(self.employee.format_start_date_for_rides).press_enter()
        s(by.xpath(self.TO)).set_value(self.employee.format_end_date_for_rides).press_enter()
        s(by.xpath(self.SIGNAL)).set_value(self.employee).press_enter()
        s(by.xpath(self.LICENSE_PLATE)).set_value(self.employee.find_license_plate).press_enter()
        s(by.xpath(self.FILTER_BTN)).click()
        return self

    def save_rides_report_to_excel_file(self):
        s(by.xpath(self.EXCEL_REPORT)).click()
        DownloadPending(self.driver, timeout=5, rename=True)

