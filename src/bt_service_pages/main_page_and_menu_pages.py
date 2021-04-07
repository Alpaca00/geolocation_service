import csv
import time

from selene.api import *
from selene.core.exceptions import ConditionNotMatchedError
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from new_objects.support import DownloadPending


class MainPageLocator:
    RIDES_BTN = "//a[text()='Мої поїздки']"
    RIDES_DOWNLOADS_CSV = "//a[text()='Завантажити CSV-файл']"

    BILLS_BTN = "//a[text()='Рахунки']"
    BILLS_PDF = "//table[@class='table table-striped table-hover m-b-md']//parent::tr/td[last()]/a"

    COMPENSATION_BTN = "//a[text()='Компенсації']"
    COMPENSATION_DATA_LOCATOR = "//table[@class='table table-striped table-hover m-b-md']//tr[2]/td"

    BALANCE_BTN = "//a[text()='Балансові звіти']"
    PAYMENTS_PDF = "//table[@class='table table-striped table-hover m-b-md']//tr[1]/td[2]/span/a"

    ACQUIRING_BTN = "//a[text()='Виплати']"
    ACQUIRING_STATISTICS = "//table[@class='table table-striped m-b-md']/tbody/tr[1]"

    EXIT_BTN = "//a[text()='Вийти']"


class MainPage(MainPageLocator):

    def __init__(self):
        super(MainPage).__init__()
        self.driver = config.driver
        self.wait = WebDriverWait(self.driver, 10)


    def at_page(self, title):
        try:
            return self.wait.until(EC.title_is(title))
        except TimeoutException:
            return False

    def go_to_rides_page(self):
        s(by.xpath(self.RIDES_BTN)).click()
        return RidesPage()

    def go_to_bills_page(self):
        s(by.xpath(self.BILLS_BTN)).click()
        return BillsPage()

    def go_to_compensation_page(self):
        s(by.xpath(self.COMPENSATION_BTN)).click()
        return CompensationPage()

    def go_to_payments_page(self):
        s(by.xpath(self.BALANCE_BTN)).click()
        return PaymentsPage()

    def go_to_acquiring_page(self):
        s(by.xpath(self.ACQUIRING_BTN)).click()
        return AcquiringPage()

    def log_out_of_account(self):
        s(by.xpath(self.EXIT_BTN)).double_click()
        self.confirm_exit()

    def confirm_exit(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to_alert()
            alert.accept()
        except TimeoutException:
            return True
        except NoAlertPresentException:
            return True


class RidesPage(MainPage):

    def save_rides_report_to_csv_file(self):
        s(by.xpath(self.RIDES_BTN)).click()
        s(by.xpath(self.RIDES_DOWNLOADS_CSV)).click()
        #DownloadPending(self.driver, timeout=3, rename=True)
        time.sleep(5)


class BillsPage(MainPage):

    def save_bills_report_to_pdf_file(self):
        s(by.xpath(self.BILLS_BTN)).click()
        s(by.xpath(self.BILLS_PDF)).double_click()
        DownloadPending(self.driver, timeout=3, rename=True)


class CompensationPage(MainPage):

    def check_compensation(self, condition):
        s(by.xpath(self.COMPENSATION_BTN)).click()
        data = s(by.xpath(self.COMPENSATION_DATA_LOCATOR))
        try:
            if data.get(query.text) == condition:
                pass
            else:
                data.get(query.screenshot('Compensation.png'))
        except ConditionNotMatchedError:
            return False


class PaymentsPage(MainPage):

    def save_payments_report_to_pdf_file(self):
        s(by.xpath(self.PAYMENTS_PDF)).double_click()
        DownloadPending(self.driver, timeout=3, rename=True)


class AcquiringPage(MainPage):

    def get_acquiring_statistics(self):
        s(by.xpath(self.ACQUIRING_BTN)).click()
        row = s(by.xpath(self.ACQUIRING_STATISTICS)).get(query.text)
        return self.write_file(row)


    @staticmethod
    def write_file(file_statistics):
        with open('acquiring.csv', mode='w') as file:
            writer = csv.writer(file, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(file_statistics)
