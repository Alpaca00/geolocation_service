from selene import by, query
from selene.support.shared.jquery_style import s
from src.domain.user import collection_admin
from src.pages.mileage_report_page import MileageReportPage


class MainPageLocators:
    LOGO = "//span[@class='x-tree-node-text  ']"
    BALANCE = "//label[@class='x-component x-box-item x-toolbar-item x-component-default']"
    REPORT_PERIOD_BTN = "//a[@data-componentid='button-1175']"
    WEEK_PERIOD_SELECT = "#menuitem-1181-textEl"

    CASCADING_MENU_BTN = "//a[@data-componentid='splitbutton-1229']"
    REPORTS = "//a[@id='menuitem-1233-itemEl']"
    RIDES_REPORT = "//span[@id='menuitem-1398-textEl']"
    MILEAGE = "//span[@id='menuitem-1400-textEl']"


class MainPage(MainPageLocators):
    def __init__(self):
        super(MainPage, self).__init__()


    def main_page_logo_text(self):
        return s(by.xpath(self.LOGO))

    def inspect_current_balance(self):
        my_balance = s(by.xpath(self.BALANCE)).get(query.text)
        if my_balance.startswith('Баланс: -'):
            collection_admin.insert_one({'negative_current_balance': my_balance})
        else:
            collection_admin.insert_one({'positive_current_balance': my_balance})

    def go_to_car_mileage_data(self):
        s(by.xpath(self.REPORT_PERIOD_BTN)).click().wait_until(s(self.WEEK_PERIOD_SELECT).click())
        s(by.xpath(self.CASCADING_MENU_BTN)).click()
        s(by.xpath(self.REPORTS)).double_click()
        s(by.xpath(self.RIDES_REPORT)).double_click()
        s(by.xpath(self.MILEAGE)).click()
        return MileageReportPage
