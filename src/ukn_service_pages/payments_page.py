from selene.api import *
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import ActionChains
from new_objects.support import DownloadPending
from src.domain.employee_ukn import Employee


class PaymentsPageLocators:
    FROM = "//input[@name='StartDate']"
    TO = "//input[@name='EndDate']"
    DRIVER_ID = "//button[@data-id='driverid']"
    INPUT_ID = "//li[@data-original-index='2']//span[1]"
    VEHICLE = "//button[@data-id='vehicleid']"
    FILTER_BTN = "//input[@class='btn btn-primary uk-btn-primary']"
    TYPE_REPORT = "//button[@id='typesExport']"
    EXCEL_REPORT = "//ul[@id='exportData']/li/a[@class='text-lowercase']"


class PaymentsPage(PaymentsPageLocators):
    def __init__(self):
        super(PaymentsPage).__init__()
        self.driver = config.driver
        self.employee = Employee('10388')
        self.action = ActionChains(self.driver)

    def set_parameters_of_payments_report(self):
        s(by.xpath(self.FROM)).hover().set_value(self.employee.format_start_date_for_payments).press_enter()
        s(by.xpath(self.TO)).click().set_value(self.employee.format_end_date_for_payments).press_enter()

        select_id = self.driver.find_element_by_xpath(self.DRIVER_ID)
        self.action.move_to_element(select_id).click().send_keys('\ue015')\
            .send_keys('\ue015').send_keys('\ue015').send_keys('\ue015').send_keys('\ue007').perform()
        select_vehicle = self.driver.find_element_by_xpath(self.VEHICLE)
        self.action.move_to_element(select_vehicle).click().send_keys('\ue015')\
            .send_keys('\ue015').send_keys('\ue015').send_keys('\ue007').perform()
        s(by.xpath(self.FILTER_BTN)).click()
        return self

    def save_payments_report_to_excel_file(self):
        try:
            type_file = self.driver.find_element_by_xpath(self.TYPE_REPORT)
            excel = self.driver.find_element_by_xpath(self.EXCEL_REPORT)
            self.action.move_to_element(type_file).click(type_file).move_to_element(excel).click(excel).perform()
        except ElementNotInteractableException:
            return False
        finally:
            DownloadPending(self.driver, timeout=5, rename=True)
