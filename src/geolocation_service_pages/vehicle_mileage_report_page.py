import allure
from selene.core.wait import Wait
from selene.support import by
from selene.support.conditions.be import visible
from selene.support.shared import config
from selene.support.shared.jquery_style import s
from selene.api import *
from app.handling_geo_database import VehicleMileageCollection
from new_objects.support import DownloadPending


class VehicleMileageReportPageLocators:
    LOGO = "//span[@class='x-tree-node-text ']"
    RADIO_BTN_CONFIRM_OBJECT = "//div[@class=' x-tree-checkbox']"
    GENERATE_DATA = "//span[@id='rep_button-btnInnerEl']"
    FRAME_REPORT_TITLE = "//div[@id='pagetitle']"
    REPORT_TABLE = "//div[@id='repcontainer']//tr/td"

    CSV_FILE = "//input[@id='ibtCsv']"


class VehicleMileageReportPage(VehicleMileageReportPageLocators):

    def __init__(self):
        super(VehicleMileageReportPage).__init__()
        self.driver = config.driver
        self.vehicle_mileage_collection = VehicleMileageCollection()

    @allure.step('admin logo visible')
    def logo_text(self):
        main_tab = self.driver.current_window_handle
        self.tab_analyzer(main_tab)
        return s(by.xpath(self.LOGO))

    def tab_analyzer(self, tab):
        for id in self.driver.window_handles:
            if id != tab:
                self.driver.switch_to.window(id)
                break
        return self


    @allure.step
    def switch_on_report_tab(self):
        main_tab = self.driver.current_window_handle
        self.tab_analyzer(main_tab)
        s(by.xpath(self.RADIO_BTN_CONFIRM_OBJECT)).click()
        s(by.xpath(self.GENERATE_DATA)).click()
        ss(by.xpath(self.REPORT_TABLE)).should(be.visible, timeout=5)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        return s(by.xpath(self.FRAME_REPORT_TITLE))

    @allure.step('insert document to vehicle mileage collection')
    def insert_data_to_vehicle_mileage_collection(self):
        tab = self.driver.current_window_handle
        self.tab_analyzer(tab)
        self.driver.find_element_by_xpath(self.RADIO_BTN_CONFIRM_OBJECT).click()
        self.driver.find_element_by_xpath(self.GENERATE_DATA).click()
        ss(by.xpath(self.REPORT_TABLE)).should(be.visible, timeout=5)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        rows = ss(by.xpath(self.REPORT_TABLE))
        arr = []
        for row in rows:
            elem = row.get(query.text)
            arr.append(elem)
        self.vehicle_mileage_collection.insert_to_collection(arr)
        return self

    @allure.step('save mileage report to csv file')
    def save_report_to_file(self):
        tab = self.driver.current_window_handle
        self.tab_analyzer(tab)
        self.driver.find_element_by_xpath(self.RADIO_BTN_CONFIRM_OBJECT).click()
        self.driver.find_element_by_xpath(self.GENERATE_DATA).click()
        ss(by.xpath(self.REPORT_TABLE)).should(be.visible, timeout=5)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        s(by.xpath(self.CSV_FILE)).click()
        DownloadPending(self.driver, timeout=3, rename=True)

