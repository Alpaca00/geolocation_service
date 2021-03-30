from datetime import date, timedelta
import allure
from selene.api import *

from new_objects.support import DownloadPending
from src.pages.main_page import MainPageLocators
from src.pages.mileage_report_page import MileageReportPageLocators, MileageReportPage
from app.handling_data import StopsCollection


class StopsReportPageLocator(MileageReportPageLocators, MainPageLocators):
    DATE_FROM = "//div[@id='fromdate-inputWrap']/input"
    STOPS_REPORT = "//span[@id='menuitem-1401-textEl']"
    REPORT_TABLE_STOPS = "//*[@id='repcontainer']//table//tr"


class StopsReportPage(StopsReportPageLocator):
    def __init__(self):
        super().__init__()
        self.driver = config.driver
        self.mileage_page = MileageReportPage()

    @property
    def generate_start_date(self):
        today_is = date.today()
        calc = today_is - timedelta(days=6)
        start = calc.strftime('%d.%m.%y')
        return start

    @allure.step('go to stops car report')
    @allure.step('check (input field start date) of report')
    def go_to_stops_report_page(self):
        s(by.xpath(MainPageLocators.REPORT_PERIOD_BTN)).click().wait_until(
                s(MainPageLocators.WEEK_PERIOD_SELECT).should(have.exact_text('Текущая неделя')).click())
        s(by.xpath(self.DATE_FROM)).should(be.not_.value(self.generate_start_date)).get(
            query.screenshot('/docs/start_date.png'))
        s(by.xpath(self.DATE_FROM)).should(be.not_.value(self.generate_start_date)).set_value(self.generate_start_date)
        s(by.xpath(MainPageLocators.CASCADING_MENU_BTN)).click()
        s(by.xpath(MainPageLocators.REPORTS)).double_click()
        s(by.xpath(MainPageLocators.RIDES_REPORT)).double_click()
        s(by.xpath(self.STOPS_REPORT)).click()
        return self

    @allure.step
    def switch_on_stops_car_report_tab(self):
        main_tab = self.driver.current_window_handle
        self.mileage_page.tab_analyzer(main_tab)
        s(by.xpath(self.RADIO_BTN_CONFIRM_OBJECT)).click()
        s(by.xpath(self.DATE_FROM)).should(be.not_.value(self.generate_start_date)).set_value(self.generate_start_date)
        s(by.xpath(self.GENERATE_DATA)).click()
        ss(by.xpath(self.REPORT_TABLE)).should(be.visible, timeout=5)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        return s(by.xpath(self.FRAME_REPORT_TITLE))

    @allure.step('insert document to mileage_collection')
    def insert_data_to_stops_collection(self):
        rows = browser.all(by.xpath(self.REPORT_TABLE_STOPS)).from_(2)
        start_of_parking = []
        end_of_parking = []
        time_of_stay = []
        starting_mileage = []
        ending_mileage = []
        address = []
        for row in rows.all('./td[7]'):
            elem = row.get(query.text)
            address.append(elem)

        for row in rows.all('./td[6]'):
            elem = row.get(query.text)
            ending_mileage.append('.'.join(elem.split(',')))

        for row in rows.all('./td[5]'):
            elem = row.get(query.text)
            starting_mileage.append('.'.join(elem.split(',')))

        for row in rows.all('./td[4]'):
            elem = row.get(query.text)
            time_of_stay.append(elem)

        for row in rows.all('./td[3]'):
            elem = row.get(query.text)
            end_of_parking.append(elem)

        for row in rows.all('./td[2]'):
            elem = row.get(query.text)
            start_of_parking.append(elem)

        StopsCollection().insert_to_collection(start_of_parking, end_of_parking,
                                               time_of_stay, starting_mileage, ending_mileage, address)
        return rows.get(query.size)

    @allure.step('save stops car report to csv file')
    def save_report_to_file(self):
        main_tab = self.driver.current_window_handle
        self.mileage_page.tab_analyzer(main_tab)
        s(by.xpath(self.RADIO_BTN_CONFIRM_OBJECT)).click()
        s(by.xpath(self.DATE_FROM)).should(be.not_.value(self.generate_start_date)).set_value(self.generate_start_date)
        s(by.xpath(self.GENERATE_DATA)).click()
        ss(by.xpath(self.REPORT_TABLE)).should(be.visible, timeout=5)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        s(by.xpath(self.mileage_page.CSV_FILE)).click()
        DownloadPending(self.driver, timeout=3, rename=True)
