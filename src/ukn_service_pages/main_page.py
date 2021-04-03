from selene import have, be, by
from selene.support.shared.jquery_style import s
from src.ukn_service_pages.payments_page import PaymentsPage
from src.ukn_service_pages.rides_page import RidesPage


class MainPageLocator:
    LOGO = "//div[@class='user']/span"
    ACCOUNT_BTN = "//span[contains(text(), 'Account')]"
    FLEET_BTN = "//span[contains(text(), 'Fleet')]"
    REPORTS_BTN = "//*[contains(text(), 'Reports')]"
    RIDES_BTN = "//a[@title='Rides']"
    PAYMENTS_BTN = "//a[@title='Payments']"


class MainPage(MainPageLocator):
    def __init__(self):
        super(MainPage).__init__()

    def at_main_page(self):
        return s(self.LOGO).matching(be.visible)

    def go_to_rides_page(self):
        s(by.xpath(self.ACCOUNT_BTN)).click()
        s(by.xpath(self.FLEET_BTN)).click()
        s(by.xpath(self.REPORTS_BTN)).click()
        s(by.xpath(self.RIDES_BTN)).click()
        return RidesPage()

    def go_to_payments_page(self):
        s(by.xpath(self.ACCOUNT_BTN)).click()
        s(by.xpath(self.FLEET_BTN)).click()
        s(by.xpath(self.REPORTS_BTN)).click()
        s(by.xpath(self.PAYMENTS_BTN)).click()
        return PaymentsPage()
